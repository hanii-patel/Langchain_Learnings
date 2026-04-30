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
    "Qwen/Qwen2.5-72B-Instruct"
]

url = "https://router.huggingface.co/v1/chat/completions"

for m in models:
    res = requests.post(url, headers=headers, json={"model": m, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 10})
    print(m, res.status_code, res.text[:200])
