# In this project creating gradio ui interface with  chat llm streaming(like we can see letters generating)

from openai import OpenAI
import gradio as gr

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def streamChat(message):
    stream = openai.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that responds in markdown without code blocks"},
            {"role": "user", "content": message}
        ],
        stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

input_message= gr.Textbox(label="Your Message:", info="Enter message", lines=7)
output_message= gr.Textbox(label="Response:", lines=7)

view = gr.Interface(
    fn=streamChat,
    inputs=[input_message],
    outputs=[output_message],
    examples=["What is transformers in llm"],
    flagging_mode="never"
)

view.launch()