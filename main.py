import openai
from openai import OpenAI
import os

#openai.api_key = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY_2")
#openai.api_key = os.environ.get("OPENAI_API_KEY_2")

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

# pip freeze > 1.txt
# pip uninstall -y -r 1.txt

