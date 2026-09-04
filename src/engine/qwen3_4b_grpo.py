


from transformers import AutoTokenizer, AutoModelForCausalLM
from vllm import LLM, SamplingParams
import torch
import os
from abc import abstractmethod
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

from utils.register import register_class
from utils.utils_func import vllm_api_url
from .base_engine import Engine
import time
import torch._dynamo
import json
from openai import OpenAI
from requests.exceptions import ConnectionError, Timeout, RequestException
import os

import httpx

#MODEL_NAME = "qwen3-grpo-200"
MODEL_NAME = "Qwen3-4B"

torch._dynamo.config.suppress_errors = True

@register_class(alias="Engine.qwen3_4b_grpo")
class qwen3_4b_grpo(Engine):
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new qwen3_4b_grpo instance", flush=True)
            cls._instance = super(qwen3_4b_grpo, cls).__new__(cls)
            cls._instance._initialized = False
        else:
            print("Reusing existing qwen3_4b_grpo instance", flush=True)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        
        self.model_path = MODEL_NAME
        self.api_key = vllm_api_url['api_key']
        self.base_url = vllm_api_url['base_url']
        self.model_name = MODEL_NAME
        
        self.client = OpenAI(
            api_key = self.api_key,
            base_url = self.base_url,
            http_client=httpx.Client(
        limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        headers={"Connection": "close"}
    )
        )
       
    def get_response(self, messages):
        max_retries = 2
        for attempt in range(max_retries):
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model_name,
                    max_tokens=16384,
                    timeout=1200.0,
                    temperature=0.0,
                    extra_body={
                        "chat_template_kwargs": {"enable_thinking": False},
                        },

                    )

                response = chat_completion.choices[0].message.content
                return response
            
            except (ConnectionError, Timeout) as e:
                print(f"Network error occurred: {e}. Retrying {attempt + 1}/{max_retries}...")
                if attempt == max_retries - 1:
                    raise
                
            except RequestException as e:
                print(f"An error occurred: {e}.")
                raise 
            
            except Exception as e:
                print(e)
                
        return "Unable to get a response after several attempts."
