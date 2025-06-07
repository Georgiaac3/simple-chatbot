from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.mistral.ai/v1/chat/completions"

def scrape_mistral_docs():
    """Scrape basic Mistral AI documentation content"""
    docs_urls = [
        "https://docs.mistral.ai/getting-started/quickstart/",
        "https://docs.mistral.ai/capabilities/completion/",
        "https://docs.mistral.ai/api/",
    ]
    
    docs_content = []
    for url in docs_urls:
        try:
            # GET the page content
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            content = soup.get_text()
            docs_content.append(f"Source: {url}\n{content[:2000]}...")  # Limit content to 2000 characters
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    
    return "\n\n---\n\n".join(docs_content)

def get_ai_response(user_input, include_docs=False):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Check if user is asking about Mistral AI documentation
    mistral_keywords = ["mistral", "documentation", "api", "model", "completion"]
    if include_docs or any(keyword.lower() in user_input.lower() for keyword in mistral_keywords):
        docs_content = scrape_mistral_docs()
        enhanced_prompt = f"""You are a helpful assistant with access to Mistral AI documentation. 
                            Use the following documentation to answer questions about Mistral AI:

                            {docs_content}

                            User question: {user_input}

                            Please provide an accurate answer based on the documentation above."""
        
        data = {
            "messages": [{"role": "user", "content": enhanced_prompt}],
            "model": "mistral-large-latest",
            "max_tokens": 1000
        }
    else:
        data = {
            "messages": [{"role": "user", "content": user_input}],
            "model": "mistral-large-latest"
        }
    
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Mistral AI Chatbot - Ask me about Mistral AI documentation!")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        try:
            ai_response = get_ai_response(user_input)
            print("AI:", ai_response)
        except Exception as e:
            print(f"Error: {e}")
        print()