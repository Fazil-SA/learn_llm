import gradio as gr

def chat(message, history):
    return f"Displaying the message itself since only ui integrated: {message}"

gr.ChatInterface(fn=chat, type="messages").launch()

