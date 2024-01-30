from openai import OpenAI
import os

client = OpenAI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="""
        De tudo, ao meu amor serei atento
        Antes, e com tal zelo, e sempre, e tanto
        Que mesmo em face do maior encanto
        Dele se encante mais meu pensamento.
    """,
)

response.stream_to_file("output.mp3")