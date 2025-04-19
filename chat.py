from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.mistral.ai/v1/chat/completions"

def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": user_input}],
        "model": "mistral-large-latest"
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        ai_response = get_ai_response(user_input)
        print("AI:", ai_response)