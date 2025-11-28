from unittest import result
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore 
from openai import OpenAI
import os



load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# creating openAI client 
openAi_Client = OpenAI()

# Vector Embeddings 
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# take user input 
user_query = input("Ask Something ➡️:")

# relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content : {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: { result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT1 = f"""
    You are a helpfull AI Assistant who answers user query based on the available context retrived from a PDF file along with page_contents and page number.
    You should only answer the user based on the following context and navigate the user to open the right  page number and to know more.
    
    Context:
    {context}
"""


response  = openAi_Client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        { "role": "system" , "content": SYSTEM_PROMPT1} , 
        { "role" : "user"  , "content" : user_query }
    ]
)

print(f"🤖: {response.choices[0].message.content}")