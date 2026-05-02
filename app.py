import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from doc_processor import generate_answer, load_file, process_file, save_to_vector_db, search_info

load_dotenv()

# setup streamlit
st.set_page_config(page_title="LangChain and LCEL Example", page_icon=":contract:", layout = "centered")
st.title(" Legal Document Review App")
st.markdown("Upload your legal document, so you can ask questions about it and get relevant answers based on the content of the document.")

with st.sidebar:
    st.header("Authentication")
    google_api_key = st.text_input("Google API Key", type="password")
    st.info("Your key is used only for this session and is not stored.")

uploaded_file = st.file_uploader("Upload a legal document (PDF Only):", type=["pdf"])

if st.button("Process Document and Get Answer") and uploaded_file and google_api_key:
    embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=google_api_key)
    with st.spinner("Processing document and generating answer..."):
        temp_file_path = os.path.join("temp",uploaded_file.name)
        open(temp_file_path, "wb").write(uploaded_file.getbuffer())

        with st.spinner("Loading document..."):
            docs = load_file(temp_file_path)

        with st.expander("Document Content Preview"):
            st.text(docs[0].page_content)  # Show the first page

        with st.spinner("Chunking document..."):
            chunks = process_file(docs)

        with st.spinner("Storing in vector database..."):
            save_to_vector_db(chunks, embeddings_model, "legal_faiss_index")

st.success("Document processed and ready for your questions to be answered!")

# User should be able to ask questions without uploading a document if it was previously uploaded and processed.
legal_question = st.text_area("Enter your legal question:", height=100)      

if st.button("Get Answer") and legal_question and google_api_key:
    embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=google_api_key)
    with st.spinner("Generating answer..."):
        relevant_chunks = search_info(legal_question, "legal_faiss_index", embeddings_model)
        response = generate_answer(legal_question, relevant_chunks, google_api_key)

        st.subheader("AI Response:")
        st.write(response)
    
            
    

