import json
from openai import OpenAI
from requests.exceptions import ConnectionError, Timeout, RequestException
import os
import httpx
from dotenv import load_dotenv
import traceback

load_dotenv()


# Set vllm serve api and url
vllm_api_url = {
    'base_url': "http://localhost:8000/v1",
    "api_key": "EMPTY"
}

# Set OpenAI api and url
api_key = os.environ["OPENROUTER_API_KEY"]
api_base = "https://api.openai.com/v1"

os.environ['OPENAI_API_KEY'] = api_key
os.environ['OPENAI_API_BASE'] = api_base

LLM_Type = "Qwen3-4B"
#LLM_Type = "qwen3-grpo-200"

AGENTS = {
    # the model under test: trained checkpoint on local vLLM
    "eval": {
        "base_url": "http://localhost:8000/v1",
        "api_key": "EMPTY",
        "model": LLM_Type,          
        "is_vllm": True,
    },
    # environment agents: GPT-4o via OpenAI
    "test": {
        "base_url": "https://api.openai.com/v1",
        "api_key": os.environ["OPENAI_API_KEY"],   
        "model": "gpt-4o-2024-11-20",
        "is_vllm": False,
    },
}


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def save_json(data, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

clients = {}
def select_client(agent):
    if agent not in clients:                      # reuse — a client per call leaks sockets
        cfg = AGENTS[agent]
        clients[agent] = OpenAI(
            api_key=cfg["api_key"], base_url=cfg["base_url"],
            http_client=httpx.Client(
                limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
            ),
        )
    return clients[agent]


def get_completion(prompt, history, flag, agent = "eval"):
    cfg = AGENTS[agent] 
    client = select_client(agent)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            messages = [{"role": "system", "content": "你是一个得力的助手。"}]
            for h in history:
                messages.append({"role": "user", "content": h[0]})
                messages.append({"role": "assistant", "content": h[1]})
            messages.append({"role": "user", "content": prompt})   

            kwargs = dict(
                messages=messages, model=cfg["model"],
                max_tokens=4096, temperature=0, timeout=1200,
            )
            if flag == 1:
                kwargs["response_format"] = {"type": "json_object"}
            if cfg["is_vllm"]:                      # vLLM-only knob; OpenAI would reject/ignore it
                kwargs["extra_body"] = {"chat_template_kwargs": {"enable_thinking": False}}

            response = client.chat.completions.create(**kwargs).choices[0].message.content
            history.append((prompt, response))
            return response, history
        
        except (ConnectionError, Timeout) as e:
            print(f"Network error occurred: {e}. Retrying {attempt + 1}/{max_retries}...")
            if attempt == max_retries - 1:
                raise
                
        except RequestException as e:
            print(f"An error occurred: {e}.")
            raise 
        except Exception as e:
            traceback.print_exc()
            
    return "Unable to get a response after several attempts."