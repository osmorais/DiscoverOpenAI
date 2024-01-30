from openai import OpenAI
import os

client = OpenAI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
  model="dall-e-3",
  prompt="medieval bard playing heavy metal",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)