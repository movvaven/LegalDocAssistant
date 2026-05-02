# Legal Doc Assistant with LangChain & LCEL
**Author - Venkat Movva**

**Overview**  
This is a Retrieval-Augmented Generation (RAG) implementation developed using LangChain and LCEL for assisting Legal/HR professionals. This application analyzes the information present in the documents using an AI model and generates concised text from uploaded legal documents. This offloads a lot of emails between the legal department and general public on basic legal questions. 

**Scenario 1 - for Legal Professionals**  
Legal professionals frequently deal with large volumes of complex documents such as contracts, NDAs, and terms of service. Reviewing these documents manually is timeintensive and prone to human error. A solution that leverages AI to help users understand, summarize, and query these legal documents can significantly improve
productivity and reduce legal risk. This assignment tasks you with building a web application that enables users to upload
legal documents and receive intelligent, context-aware assistance through modern language models.

**Scenario 2 - for HR Professionals**  
HR teams need an efficient way to handle routine, repetitive employee inquiries. This tool enables HR professionals to focus on higher-value work while providing employees with immediate, self-service access to common information—eliminating delays associated with email responses. Typical queries include topics such as adding a spouse to healthcare coverage, understanding sick leave policies, and determining PTO rollover limits.

## 🚀 Features

- Upload legal docs in PDF formats
- Extract and analyze content using Google Gemini model
- Chunk and Embed content using Google Gemini model
- Store embeded results in a FIASS vector store
- View structured AI-generated responses faster.

---

## 📦 Tech Stack

- **LangChain** for building chains, embeddings, and document processing
- **LangChain Expression Language (LCEL)** for modular pipeline workflows
- **Streamlit** for the frontend web interface
- **Google Gemini** Google’s Gemini 2.5 Flash model LLM for reasoning
- **Gemini Embedding Model** Gemini Embeddings generator with 3072-dimensional vectors
- **FIASS** as a persistent vector store
- **Python** as the base coding language
- **PyPDFLoader** for loading PDF & extract text
- **dotenv** for API key and environment config

---

## 🛠️ Setup Instructions


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
- Strengths: Relevant information from uploaded docs, Fast and easy as the document is indexed and stored locally in DB.
- Weaknesses: May hallucinate to some extent, but the most part is contained as it is tightly setup to read from uploaded Document.

```

---

## 🧑‍💼 Ideal For

* Legal and HR professionals
* Legal Document automation tools
* Educational and project demos for RAG, Persistent Vector DB, LangChain and LCEL
