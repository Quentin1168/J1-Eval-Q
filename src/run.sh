CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
vllm serve Qwen/Qwen3.5-4B \
  --api-key EMPTY --port 8888 \
  --served-model-name Qwen3.5-4B 
  --tensor-parallel-size 8 \
  --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' \
  --max-model-len 131072