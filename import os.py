import openai
import os
openai.api_key = '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'
dominio = "argentina.gob.ar"

def chatGPT(dominio):
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": f"Este link es seguro? {dominio}"}],
    max_tokens=193,
    temperature=0,
    )
    return response

response = chatGPT(dominio)

print(response)
print(response["choices"][0]["message"]["content"])
