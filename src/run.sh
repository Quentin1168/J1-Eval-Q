CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
vllm serve Qwen/Qwen3-4B \
  --api-key EMPTY --port 8000 \
  --served-model-name Qwen3-4B \
  --enable-lora \
 # --lora-modules qwen3-grpo-200=/workspace/J1-Eval-Q/0200 \
  --max-lora-rank 16 \
  --max-model-len 32768