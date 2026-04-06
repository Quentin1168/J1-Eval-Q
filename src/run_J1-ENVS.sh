#!/bin/bash
set -e

python run.py --scenario J1Bench.Scenario.KQ --trainee Agent.Trainee.ConsultQwen3_32B --general_public Agent.General_public.ConsultQwen3_32B --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/KQ_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.LC --trainee Agent.Trainee.LC_Qwen3_32B --general_public Agent.General_public.LC_Qwen3_32B --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/LC_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CD --lawyer Agent.Lawyer.Qwen3_32B --specific_character Agent.Specific_character.Qwen332B_CD --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/CD_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.DD --lawyer Agent.Lawyer.Qwen3_32B_DD --specific_character Agent.Specific_character.Qwen332B_DD --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/DD_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CI --judge Agent.Judge.Qwen3_32B_CI --plaintiff Agent.Plaintiff.Qwen3_32B_CI --defendant Agent.Defendant.Qwen3_32B_CI --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/CI_dialog_history.jsonl"
#python run.py --scenario J1Bench.Scenario.CR --judge Agent.Judge.Qwen3_32B_CR --lawyer Agent.Lawyer.Qwen3_32B_CR --defendant Agent.Defendant.Qwen3_32B_CR --procurator Agent.Procurator.Qwen3_32B_CR --save_path "/root/projects/J1Bench/src/data/dialog_history/Qwen/CR_dialog_history.jsonl"