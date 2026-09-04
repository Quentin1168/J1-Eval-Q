#!/bin/bash
set -e

#python run.py --scenario J1Bench.Scenario.KQ --trainee Agent.Trainee.ConsultQwen3_4B_GRPO --general_public Agent.General_public.ConsultGPT --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/KQ_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.LC --trainee Agent.Trainee.LC_Qwen3_4B_GRPO  --general_public Agent.General_public.LC_GPT --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/LC_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CD --lawyer Agent.Lawyer.Qwen3_4B_GRPO --specific_character Agent.Specific_character.GPT_CD --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/CD_dialog_history.jsonl"
python run.py --scenario J1Bench.Scenario.DD --lawyer Agent.Lawyer.Qwen3_4B_GRPO_DD --specific_character Agent.Specific_character.GPT_DD --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/DD_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CI --judge Agent.Judge.Qwen3_32B_CI --plaintiff Agent.Plaintiff.Qwen3_32B_CI --defendant Agent.Defendant.Qwen3_32B_CI --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/CI_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CR --judge Agent.Judge.Qwen3_32B_CR --lawyer Agent.Lawyer.Qwen3_32B_CR --defendant Agent.Defendant.Qwen3_32B_CR --procurator Agent.Procurator.Qwen3_32B_CR --save_path "/workspace/J1-Eval-Q/src/data/dialog_history/QwenGRPO/CR_dialog_history.jsonl"