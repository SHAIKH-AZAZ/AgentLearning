from ast import If
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
import os

pdf_path = Path(__file__).parent / "node-dev.pdf"
load_dotenv()

# Correct env variable name
API_KEY = os.getenv("OPENAI_API_KEY")
print("api loading done ✔️ ")
# load this file in python program 
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=API_KEY
)

vectore_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
    force_recreate=True,   # recreate with this embedding size
)

print("Indexing of Documents are done ....")
