#!/bin/bash
set -e

python /root/projects/J1Bench/src/Eval/bench/KQ/KQ.py
python /root/projects/J1Bench/src/Eval/bench/LC/LC.py
python /root/projects/J1Bench/src/Eval/bench/CD/CD.py
python /root/projects/J1Bench/src/Eval/bench/DD/DD.py
python /root/projects/J1Bench/src/Eval/bench/CI/CI.py
python /root/projects/J1Bench/src/Eval/bench/CR/CR.py