from langchain.prompts import PromptTemplate
from langchain import hub
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables import RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv


load_dotenv()

# load the file
embed_model = "mistral-embed"
file_path = "Data\cookbook.pdf"
loader = PyPDFLoader(file_path=file_path)
documents = loader.load()

# split the file into chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=30, separator="\n")
docs = text_splitter.split_documents(documents=documents)

# embed the files
embeddings = MistralAIEmbeddings(model=embed_model)

# store the data chunks into FAISS memory vector database
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local('index_faiss')

# load the vector database from local to memory
new_vectorstore = FAISS.load_local('index_faiss',
                                   embeddings,
                                   allow_dangerous_deserialization=True)

def run_llm(query):

  # create llm object
  llm                = ChatMistralAI()

  # The result will be prompted and sent to llm to answer the user query
  qa_chat_prompt     = hub.pull("langchain-ai/retrieval-qa-chat")

  # the retrival can get multiple documents back from vector db. stuff them together and send to LLM
  combine_docs_chain = create_stuff_documents_chain(llm, qa_chat_prompt)

  # retrival chain to fetch data
  retrival_chain     = create_retrieval_chain(
                                          retriever          = vectorstore.as_retriever(),
                                          combine_docs_chain = combine_docs_chain
                                        )

  result = retrival_chain.invoke(input = {'input' : query})

  return result['answer']