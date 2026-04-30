import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

models = [
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "microsoft/Phi-3-mini-4k-instruct",
    "Qwen/Qwen2.5-7B-Instruct",
    "google/gemma-1.1-7b-it"
]

for m in models:
    url = f"https://api-inference.huggingface.co/models/{m}/v1/chat/completions"
    res = requests.post(url, headers=headers, json={"messages": [{"role": "user", "content": "hi"}], "max_tokens": 10})
    print(m, res.status_code, res.text[:200])
