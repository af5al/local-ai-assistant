import requests

class OllamaProvider:
    def __init__(self, base_url: str = "http://localhost:11434"):
     self.base_url = base_url
    def get_models(self):
       response = requests.get(f"{self.base_url}/api/tags", {})
       data = response.json()
       return [model["name"] for model in data.get("models", [])]

     