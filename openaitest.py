import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "content": "Hi! How can I assist you today?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)