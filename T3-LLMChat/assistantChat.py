"""
Two llms chating with each other here iam using ollama for both
This can be implemented as chat between different llms like chat bw claude and openai based on needs
"""
from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

messages = [{"role": "user", "content": "Hello"}]

def llmfirst(messages):
    response = openai.chat.completions.create(
        model="llama3.2",
        messages= messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "user", "content": reply})
    return reply

def llmsecond(messages):
    response = openai.chat.completions.create(
        model="llama3.2",
        messages= messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

for i in range(5):
    print("llmfirst:", llmfirst(messages))
    print("llmsecond`:", llmsecond(messages))

