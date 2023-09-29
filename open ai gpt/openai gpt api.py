from fastapi import FastAPI, HTTPException
import httpx
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera a chave de API da OpenAI do ambiente
api_key = os.getenv(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)

# Cria uma instância do aplicativo FastAPI
app = FastAPI()

# URL da API do ChatGPT da OpenAI
chatgpt_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

@app.post("/chatgpt/")
async def chatgpt_completion(prompt: str):
    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json",
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 50,  # Ajuste o número máximo de tokens conforme necessário
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(chatgpt_url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return {"response": result["choices"][0]["text"]}
        else:
            raise HTTPException(status_code=response.status_code, detail="Erro ao chamar a API do ChatGPT")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
