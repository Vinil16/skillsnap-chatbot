#  SkillSnap - AI-Powered Customer Support Chatbot

SkillSnap is a conversational AI chatbot designed to assist users with queries related to the SkillSnap SaaS platform. It leverages LLMs (Gemini/OpenAI), LangChain, and Streamlit to provide intelligent, context-aware responses using a knowledge base.

## Folder Structure

```
.
├── app.py
├── chatbot_engine.py
├── requirements.txt
├── sample_input_output/
│   ├── sample_input.json
│   └── sample_output.json
├── knowledge_base/
├── README.md
```

##  Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/your-username/skillsnap-chatbot.git
cd skillsnap-chatbot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run app.py
```

Or use Docker:
```bash
docker build -t skillsnap-chatbot .
docker run -p 8501:8501 skillsnap-chatbot
```

##  Features

- Conversational chatbot UI via Streamlit
- Contextual knowledge base retrieval using LangChain
- Supports Gemini  model
- Modular and easy to extend
- Tracks unanswerable queries for analytics

##  Sample Input/Output

Check the `sample_input_output/` folder to see sample queries and responses.

##  Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Gemini LLM

## Knowledge Base

Located in `knowledge_base/` — add Markdown or plain text files here to build the vector database.

