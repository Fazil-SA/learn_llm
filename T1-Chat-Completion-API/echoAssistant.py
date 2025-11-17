# Repeat as echo of whatever user tells

from openai import OpenAI

openai = OpenAI(base_url = "http://localhost:11434/v1", api_key = "ollama")

def echoAssistant(userMessage):
    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = [
            {"role": "system", "content": "Act as echo of user, tell back whatever the user tells"},
            {"role": "user", "content": userMessage}
        ]
    )
    print(response.choices[0].message.content)

echoAssistant("I'm echo assistant")