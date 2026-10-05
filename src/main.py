from fastapi import FastAPI
from src.provider import OllamaProvider

app = FastAPI()
 
provider = OllamaProvider()

@app.get('/models')
def list_models():
    return {"models": provider.get_models()}