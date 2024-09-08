import json
import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import ( VectorStoreIndex, SimpleDirectoryReader ,
                               StorageContext, load_index_from_storage, )
from llama_index.readers.json import JSONReader

load_dotenv()
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.1)


documents = SimpleDirectoryReader('data').load_data()
#documents = reader.load_data(input_file='data/support_tickets.json', extra_info={})
index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine()
response = query_engine.query("How do I reset my password?")
print(response)