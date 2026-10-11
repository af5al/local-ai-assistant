from fastapi import responses
import requests
import json
import pandas as pd
import os

class BaseProvider:
    def get_benchmark_reports(self):
        try:
            csv_path = "benchmarks/results.csv"
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                return df.to_dict(orient="records")
            return []
        except Exception as err:
            print(err)
            return []

class OllamaProvider(BaseProvider):
    def __init__(self, base_url: str = None):
     self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    def get_models(self):
       response = requests.get(f"{self.base_url}/api/tags", {})
       data = response.json()
       return [model["name"] for model in data.get("models", [])]

    def chat_stream(self, model, messages: list[dict]):
      response = requests.post(f"{self.base_url}/api/chat", json=
      {
        "model": model,
        "messages": messages,
        "stream": True  # Waits for the full response before returning
      }, stream=True)

      if response.status_code != 200:
        yield f"Error from Ollama ({response.status_code}): {response.text}"
        return

      for line in response.iter_lines():
        if line:
         chunk = json.loads(line)
         content = chunk.get("message", {}).get("content", "")
         yield content

class GroqProvider(BaseProvider):
    def __init__(self, api_key: str = None):
        key = api_key or os.getenv("GROQ_API_KEY", "")
        self.api_key = key.strip("'\"")
        self.base_url = "https://api.groq.com/openai/v1"

    def get_models(self):
        return ["openai/gpt-oss-20b", "qwen/qwen3.8-27b", "openai/gpt-oss-120b"]

    def chat_stream(self, model, messages: list[dict]):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": messages,
            "stream": True
        }
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload,
            stream=True
        )

        if response.status_code != 200:
            yield f"Error from Groq ({response.status_code}): {response.text}"
            return

        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: ") and decoded != "data: [DONE]":
                    try:
                        chunk = json.loads(decoded[6:])
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content:
                            yield content
                    except Exception:
                        continue
