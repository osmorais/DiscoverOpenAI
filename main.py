from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

question = input(">> ")

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content" : "Você é o morpheus, Responda todas as perguntas usando a forma de escrita leet (1337)"
        },
        {
            "role" : "user",
            "content" : question
        }
    ],
    model="gpt-4"
)

print(resposta.choices[0].message.content)

# "O que morpheus fala para Neo sobre o que é a Matrix?"