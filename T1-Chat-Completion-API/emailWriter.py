# chatbot for writing emails proffesionally from a topic

from openai import OpenAI

openai = OpenAI(base_url= "http://localhost:11434/v1", api_key= "ollama")

def emailWriter(sender, reciever, subject):
    systemMessage = "You are a professional email writer. I will give you the subject, and the sender and receiver names. Your job is to write a clear, polished, and professional email based on that information."
    userMessage = (f"sender={sender},reciever={reciever},subject={subject}")
    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = [
            {"role": "system", "content": systemMessage},
            {"role": "user", "content": userMessage}
        ]
    )
    print(response.choices[0].message.content)

emailWriter("Fazil", "Ahmed", "Inform him that i will be on vacation on next 7 days")