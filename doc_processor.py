from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



def load_file(file_path):    
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:        
        raise ValueError("Unsupported file type. Please upload a PDF.")
    
    return loader.load()

def process_file(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    return chunks

def save_to_vector_db(chunks, embeddings_model, vector_db_path):
    vector_db = FAISS.from_documents(documents=chunks, embedding=embeddings_model)
    vector_db.save_local(vector_db_path)


def search_info(query, vector_db_path, embeddings_model):
    vector_db = FAISS.load_local(vector_db_path, embeddings_model,allow_dangerous_deserialization=True)
    query_embedding = embeddings_model.embed_query(query)
    relevant_chunks = vector_db.similarity_search_by_vector(query_embedding, k=3)
    return relevant_chunks

def generate_answer(user_query, relevant_chunks, api_key):
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.2, google_api_key=api_key)

    prompt = "You are a seasoned legal assistant and are very good at providing accurate and relevant information from provided legal documents. \n\n"
    for i, chunk in enumerate(relevant_chunks):
        prompt += f"Legal Document {i+1}:\n{chunk.page_content}\n\n"
    
    prompt += f", Please provide a concise, relevant and accurate answer with respect to what user asked: {user_query}, based on the above information."

    prompt_template = ChatPromptTemplate.from_template(prompt)
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({})



# Load_file
# Load that file into a temp location
# provide a means to show the file to the user

#process_file
# Process the file and extract text 

#store_file
# chunk the text into smaller pieces
# embed the chunks into vectors using a pre-trained model
# Store the embedded vectors in a vector database

#search_info
# Take user query and convert it into a vector using the same pre-trained model
# Search the vector database for similar vectors to the user query vector
# Return the relevant vectors and send it to an llm to generate a response based on the retrieved information