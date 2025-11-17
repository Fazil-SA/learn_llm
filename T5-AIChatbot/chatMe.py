import gradio as gr
from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# callback function for api
def chat(message, history):
    system_message = "You are a chatbot assistant"
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(
        model="llama3.2",
        messages=messages,
    )
    return response.choices[0].message.content

# gradio ui with function invoke
gr.ChatInterface(fn=chat, type="messages").launch()



