import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings  # Changed to Gemini-compatible
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import google.generativeai as genai
import os

st.set_page_config(page_title="SkillSnap - Gemini Chatbot", layout="wide")

# API Key input
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    st.title("🤖 SkillSnap - Your Team Learning Buddy")
    st.markdown("Ask me anything about skill building, team development, or workplace learning.")

    # Load and index knowledge base (only once)
    if "vectorstore" not in st.session_state:
        loader = DirectoryLoader("SkillSnap__KnowledgeBase", glob="*.md")
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Gemini-compatible embeddings
        vectorstore = FAISS.from_documents(docs, embeddings)

        st.session_state.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Session history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Show chat history
    for role, message in st.session_state.history:
        if role == "user":
            st.markdown(f"**👤 You:** {message}")
        else:
            st.markdown(f"**🤖 SkillSnap:** {message}")

    # Chat input at bottom
    user_input = st.chat_input("Ask your next question here...")

    if user_input:
        st.session_state.history.append(("user", user_input))
        with st.spinner("Thinking..."):
            docs = st.session_state.retriever.get_relevant_documents(user_input)
            context = "\n".join([doc.page_content for doc in docs])
            prompt = f"Answer the following based on the knowledge base:\n{context}\n\nQuestion: {user_input}"
            response = model.generate_content(prompt)
            bot_reply = response.text.strip()
            st.session_state.history.append(("bot", bot_reply))
        st.rerun()  # So new prompt appears immediately
