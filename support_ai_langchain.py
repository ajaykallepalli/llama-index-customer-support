from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI customer support agent. Answer the questions with the most accurate information. If you don't know the answer, say 'I don't know'."),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()




loader = TextLoader('./data/support_tickets_3.txt')

data = loader.load()

embeddings = OpenAIEmbeddings()

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(data)
vectorstore = FAISS.from_documents(documents, embeddings)


print(documents)