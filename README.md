### Work-In Progress

# Bangali-Pola

A quirky and knowledgeable AI assistant powered by Mistral-7B-Instruct-v0.3-GGUF model. Baal-Chera can answer questions, search the web, and look up stock prices.

## Features

- Conversational AI using local Mistral model
- Web search capabilities
- Stock price lookup
- Interactive command-line interface

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the model (automatically handled on first run)

## Usage

Run the main script:
```bash
python main.py
```

Enter your queries in the interactive prompt. Type 'exit' or 'quit' to stop.

## Dependencies

- llama-cpp-python
- huggingface-hub
- ddgs (DuckDuckGo search)
- yfinance
- gradio
- python-dotenv

## Project Structure

- `app.py`: Llama model wrapper
- `main.py`: Main application loop
- `generate_prompts.py`: Prompt management
- `tools/`: Utility tools for search functions
- `models/`: Directory for downloaded models