import openai
from openai import OpenAI
import os

#"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"
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