Legal Document Assistant Application with LangChain & LCEL
**Author - Venkat Movva**

Overview
This is a Retrieval-Augmented Generation (RAG) implementation developed using LangChain and LCEL for assisting Legal/HR professionals. This application analyzes the information present in the documents using an AI model and generates concised text from uploaded legal documents. This offloads a lot of emails between the legal department and general public on basic legal questions. 

Scenario
Legal professionals frequently deal with large volumes of complex documents such as contracts, NDAs, and terms of service. Reviewing these documents manually is timeintensive and prone to human error. A solution that leverages AI to help users understand, summarize, and query these legal documents can significantly improve
productivity and reduce legal risk. This assignment tasks you with building a web application that enables users to upload
legal documents and receive intelligent, context-aware assistance through modern language models.

Problem Statement
Lawyers and legal teams require an efficient tool to quickly review and understand the contents of legal documents. Manually identifying key clauses or summarizing lengthy
texts is inefficient and costly. There is a need for a user-friendly application that can extract text from legal PDFs, summarize key information, and answer document-specific
questions using Retrieval-Augmented Generation (RAG) and large language models.

Approach:-
Building a Legal Document Review Application with LangChain, LCEL and Streamlit, where users can:
- Upload legal documents in PDF format.
- Ingest the document by making chunks and embedding them.
- Save the document in FIASS db
- From then on, Answer user questions by querying FIASS DB
- Use Google’s Gemini 2.5 Flash model to reason and format the answers.

The application uses LangChain document loaders (PyPDFLoader) to extract text from legal documents, Gemini model to embed documents, FIASS vector DB to store embeds and LangChain’s LLMChain with a custom prompt to generate a structured analysis. Streamlit provides a user-friendly interface with custom styling for better readability.

Project Structure
- app.py: Main application code for the Legal Document Review Application.
- doc_processor.py: For modularity, to keep all the actual functions and complex logic away from main.py
- requirements.txt: List of dependencies required to run the application.
- temp folder: To save the uploaded files.
- venv/: Virtual environment directory (e.g., env for storing installed packages).

Setup Instructions:-
Create a Virtual Environment:
- Navigate to the project directory.
- Run: python -m venv venv (or env if preferred).
- Activate the virtual environment:
- Windows: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate

Install Dependencies:
- Ensure requirements.txt is in the project directory.
- Run: pip install -r requirements.txt

Run the Application Locally:
- Run: streamlit run app.py
- Open the provided URL (e.g., http://localhost:8501) in your browser to access the app.
- Give google API key in the left nav bar of streamlit UI

Deploying on Streamlit Cloud:-

Prepare Your Project:
- Ensure app.py, doc_processor.py, requirements.txt, and .env are in the project directory.
- Create a Streamlit Cloud account at https://streamlit.io/cloud.

Upload to Streamlit Cloud:
- Log in to Streamlit Cloud.
- Create a new app and connect it to your project directory (e.g., upload the files manually or link to a cloud storage service).
- Specify app.py as the main script.

Configure Environment Variables:
- In Streamlit Cloud, go to your app’s settings.
- Add the GOOGLE_API_KEY as a secret environment variable (do not include .env in the uploaded files for security).

Deploy the App:
- vClick “Deploy” in Streamlit Cloud.
- Once deployed, access the app via the provided URL (e.g., https://your-app-name.streamlit.app).

Test the Deployed App:
- Input job requirements, upload a resume, and analyze it.
- Verify that the analysis report is generated and downloadable.

Requirements
The requirements.txt file includes all necessary dependencies.

Usage
- Run the app locally or access the deployed version on Streamlit Cloud.
- Upload a legal document in PDF format.
- Click “Process Document and Get Answer” to generate the AI-driven analysis.
- Enter your legal question in the text area (e.g., skills, experience, qualifications).
- Click "Get Answer" button to get your response..

## 🚀 Features

- Upload legal docs in PDF formats
- Extract and analyze content using Google Gemini model
- Chunk and Embed content using Google Gemini model
- Store embeds results in a FIASS vector store
- View structured AI-generated responses faster.

---

## 📦 Tech Stack

- **LangChain** for building chains, embeddings, and document processing
- **LangChain Expression Language (LCEL)** for modular pipeline workflows
- **Streamlit** for the frontend web interface
- **Google Generative AI** (Gemini & Embeddings) for LLM and vector representations
- **FIASS** as a persistent vector store
- **dotenv** for API key and environment config

---

## 🛠️ Setup Instructions
````

1. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**
   Create a `.env` file in the project root and add:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 📄 File Structure

```plaintext
├── app.py                  # Main Streamlit app
├── doc_processor.py        # Functionality/ Functions needed for main.py file
├── fiass_store/            # Folder to store vector DB files
├── temp/                   # Folder to store uploaded files
├── .env                    # Contains API key (not committed)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 📚 LangChain Concepts Used

* ✅ **Components & Modules**: PromptTemplate, LLM, Output Parsers
* 📄 **Document Loaders**: PDF via LangChain community
* ✂️ **Text Splitting**: RecursiveCharacterTextSplitter
* 🧠 **Embeddings**: GoogleGenerativeAIEmbeddings
* 🗃️ **Vector DB**: FIASS for persistent storage
* 🧩 **LCEL**: RunnableMap, pipes (`|`), and chain composition
* 🧪 **Chains**: Custom chain for job/resume comparison
* 📤 **Deployment**: Streamlit as the UI layer

---

## 📈 Example Output

```
Structured Analysis:
- Strengths: Relevant information from uploaded docs, Fast and easy as teh document is indexed and stored locally in DB.
- Weaknesses: Cannot get any information that is not in the uploaded doc.

```

---

## 🧑‍💼 Ideal For

* Legal and HR professionals
* Legal Document automation tools
* Educational and project demos for RAG, LangChain and LCEL
