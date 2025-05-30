# AI Order Tracking Assistant using RAG, LangChain, and MySQL


A smart chatbot that uses LangChain, Ollama (Gemma 4B), MySQL, and ChromaDB to answer customer questions and track real-time order statuses.

## Features
- 🧠 Uses RAG (Retrieval-Augmented Generation) for accurate answers.
- 💬 Chat-like interface that responds to customer queries.
- 🔍 Real-time order tracking by connecting to a MySQL database.
- 📦 Custom knowledge base powered by ChromaDB.
- ⚡ Runs fully locally with the Gemma 4B model via Ollama.

## Setup
1. Clone this repository

2. Create and activate a virtual environment

3. Install requirements
   pip install -r requirements.txt

4. Start Ollama with the model
   ollama run gemma:4b
   ollama run mxbai-embed-large

6. Configure your MySQL credentials
   Update order_tracking.py or the relevant config file with your MySQL connection details.

7. Run the bot
   python main.py


👨‍💻 Author

Built with ❤️ by Sahan  Rajapakshe 
LinkedIn: https://www.linkedin.com/in/sahan-rajapakshe-ab63092b8/ 
GitHub: https://github.com/SSARROW
