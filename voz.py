from openai import OpenAI
import os

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

message = """
        Olá, tudo bem? Gostaria de ouvir minha mensagem em voz alta.
    """


response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=message,
)

#Voices:
# Alloy
# Echo
# Fable
# Onyx
# Nova
# Shimmer

response.stream_to_file("output.mp3")