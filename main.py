import openai
from openai import OpenAI
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
print(openai.api_key)
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)