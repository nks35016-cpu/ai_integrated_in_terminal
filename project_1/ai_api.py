import requests
import os
from dotenv import load_dotenv

load_dotenv("api.env")
key = os.getenv("GROQ_API_KEY")
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
messages = [
    {"role": "system", "content": "You are a helpful assistant named Arjun. Keep replies short and clear."}
]
while True:
    user_input=input(" ")
    if user_input.lower()=="quit":
        print("Bye!")
        break
    messages.append({"role": "user", "content": user_input})
    body = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }
    response=requests.post("https://api.groq.com/openai/v1/chat/completions",
                        headers=headers,
                        json=body)
    data=response.json()
    
    reply = data["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print(f"Bot: {reply}\n")