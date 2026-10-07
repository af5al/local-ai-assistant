import requests
import json

class OllamaProvider:
    def __init__(self, base_url: str = "http://localhost:11434"):
     self.base_url = base_url
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

      for line in response.iter_lines():
        if line:
         chunk = json.loads(line)
         content = chunk.get("message", {}).get("content", "")
         yield content

   


     