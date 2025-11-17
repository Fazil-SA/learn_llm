import gradio as gr
from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1" , api_key="ollama")

def chatStreamBot(message,history):
    system_message = "You are a chatbot assistant"
    history= [{"role": h["role"], "content": h["content"]} for h in history] 
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    stream = openai.chat.completions.create(
        model="llama3.2",
        messages=messages,
        stream=True
    )
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chatStreamBot, type="messages").launch()