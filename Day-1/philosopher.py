# basic philosopher chat model using ollama llama3.2

from openai import OpenAI

openai = OpenAI(base_url = 'http://localhost:11434/v1' ,api_key = 'ollama')

def user_persona_chat(user_name, age, userMessage):
    systemMessage = (f"You are a proffessional philosopher, people chat with you is comes for proffessional treatment , treat like that.Name={user_name} & age={age}")
    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = [{"role": "system", "content": systemMessage},
        {"role": "user", "content": userMessage}]
    )
    print(response.choices[0].message.content)

user_name = "diya"
age = 19
userMessage = "hello"

user_persona_chat(user_name, age, userMessage)