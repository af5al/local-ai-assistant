import requests

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2:1b",
    "messages": [
        {"role": "user", "content": "is LLM easy to learn?"}
    ],
    "stream": False  # Waits for the full response before returning
}

response = requests.post(url, json=payload)
data = response.json()

# Accessing the response text:
print(data["message"]["content"])
