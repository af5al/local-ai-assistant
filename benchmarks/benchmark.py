import time
import json
import requests
import psutil
import pandas as pd

MODELS = ["llama3.2:1b", "llama3.2:3b", "qwen2.5:3b"]
TASKS = [
    {"type": "chat", "prompt": "Explain what a database index is in 1 sentence."},
    {"type": "json", "prompt": 'Extract to JSON with keys "name" and "city": "Afsal lives in Dubai." Return JSON only.'}
]

results = []

for model in MODELS:
    for task in TASKS:
        ram_used_mb = psutil.virtual_memory().used / (1024 * 1024)
        start = time.perf_counter()
        api = 'http://localhost:11434/api/chat'

        res = requests.post(api, json= {
            "model": model,
            "messages": [{"role": "user", "content": task["prompt"]}],
            "stream": False
        })

        # fetching data
        duration = time.perf_counter() - start
        data = res.json()
        tokens = data.get("eval_count", 0)
        eval_ns = data.get("eval_duration", 1)
        tps = tokens / (eval_ns / 1e9)

        # validating json
        content = data.get("message", {}).get("content", "")
        try:
            json.loads(content)
            is_valid_json = True
        except Exception:
            is_valid_json = False

        results.append({
            "model": model,
            "task_type": task["type"],
            "tokens": tokens,
            "duration_sec": round(duration, 2),
            "tps": round(tps, 2),
            "ram_mb": round(ram_used_mb, 1),
            "valid_json": is_valid_json,
        })     

#save and display
df = pd.DataFrame(results)
df.to_csv("benchmarks/results.csv", index=False)
print(df)

