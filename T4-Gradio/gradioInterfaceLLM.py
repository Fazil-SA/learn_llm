# In this project creating gradio ui interface with  chat llm

from openai import OpenAI
import gradio as gr

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def chatLLM(message):
    response = openai.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

input_message= gr.Textbox(label="Your Message:", info="Enter message", lines=7)
output_message= gr.Textbox(label="Response:", lines=7)

view = gr.Interface(
    fn=chatLLM,
    inputs=[input_message],
    outputs=[output_message],
    examples=["What is saudi 2030 vision"],
    flagging_mode="never"
)

view.launch()