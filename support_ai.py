import json
import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core import ( VectorStoreIndex, SimpleDirectoryReader ,
                               StorageContext, load_index_from_storage, )
from llama_index.readers.json import JSONReader
from llama_parse import LlamaParse

load_dotenv()
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.1)

PERSIST_DIR = './storage'


if not os.path.exists(PERSIST_DIR):
    #load the documents and create the index
    documents = SimpleDirectoryReader('data').load_data(show_progress=True)
    #documents = LlamaParse(result_type='text').load_data('data/support_tickets_3.json')
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    #load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()

response = query_engine.query("Chechnia and Russia are not the same thing.")
print(response)