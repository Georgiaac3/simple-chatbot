# Simple AI Chatbot

A Python-based chatbot that uses the Mistral AI API to provide intelligent responses. The bot can answer general questions and has specialized knowledge about Mistral AI documentation through web scraping.

## Features

- 🤖 **AI-powered responses** using Mistral AI's large language model
- 📚 **Documentation integration** - automatically scrapes and uses Mistral AI docs for relevant queries
- 💬 **Interactive command-line interface**
- 🔍 **Smart context detection** - automatically includes documentation when Mistral-related keywords are detected

## Prerequisites

- Python 3.7+
- Mistral AI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd simple-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file and add your Mistral AI API key
   echo "API_KEY=your_mistral_ai_api_key_here" > .env
   ```

## Configuration

Create a `.env` file in the project root with your Mistral AI API key:

```env
API_KEY=your_mistral_ai_api_key_here
```

To get an API key:
1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Sign up or log in
3. Generate an API key
4. Add it to your `.env` file

## Usage

### Command Line Interface

Run the chatbot:

```bash
python chat.py
```

Type your questions and press Enter. Type 'quit' or 'exit' to end the conversation.

### Example Questions

- "What is Mistral AI?"
- "How do I use the Mistral API?"
- "Tell me about Mistral's completion models"
- "What are the available Mistral models?"

## Project Structure

```
simple-chatbot/
├── chat.py           # Core chatbot logic and CLI interface
├── interface.py      # Streamlit interface for chatbot
├── requirements.txt  # Python dependencies
├── README.md         # This file
├── .env              # Environment variables (not in git)
├── .gitignore        # Git ignore rules
└── __pycache__/      # Python cache files
```

## How It Works

1. **User Input**: Questions are received through the command line
2. **Context Detection**: The system checks for Mistral AI-related keywords
3. **Documentation Scraping**: If relevant, it scrapes Mistral AI documentation
4. **AI Processing**: Queries are sent to Mistral AI API with appropriate context
5. **Response**: AI-generated responses are displayed to the user

## Dependencies

- `python-dotenv`: Environment variable management
- `requests`: HTTP client for API calls
- `beautifulsoup4`: Web scraping for documentation

## Development

### Adding New Features

1. **New documentation sources**: Add URLs to the `docs_urls` list in `scrape_mistral_docs()`
2. **Enhanced prompts**: Modify the prompt templates in `get_ai_response()`
3. **Additional keywords**: Update the `mistral_keywords` list for better context detection

### Code Structure

- `scrape_mistral_docs()`: Fetches and processes Mistral AI documentation
- `get_ai_response()`: Handles API calls and context management
- Main loop: Provides interactive CLI experience

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `.env` file contains a valid Mistral AI API key
2. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Network Issues**: Check your internet connection for API calls and web scraping

### Error Messages

- `Error: 401 Unauthorized`: Invalid or missing API key
- `Error scraping [URL]`: Network issue or website changes
- `ModuleNotFoundError`: Missing dependencies - run `pip install -r requirements.txt`

