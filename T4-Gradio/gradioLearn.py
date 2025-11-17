# Experimenting with simple function

import gradio as gr

def shout(text):
    print(f"Shout has been called with input {text}")
    return text.upper()

""" gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch() """

# share=True host the interface to huggingface ,be careful while doing this since from that public link others can reach to our local machine where runs code, technically speaks http tunnelling.
""" gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(share=True) """

# inbrowser=True opens the interface in browser instead of terminal
""" gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True) """

# adding authentication where ed is the username and banana is the password
""" gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True, auth=("ed","banana")) """

# Adding a little more
message_input = gr.Textbox(label="Your Message:", info="Enter a message to be shouted", lines=7)
message_output = gr.Textbox(label="Response:", lines =8)

view = gr.Interface(
    fn=shout,
    inputs=[message_input],
    outputs=[message_output],
    examples=["hello", "howdy"],
    flagging_mode="never"
)

view.launch()