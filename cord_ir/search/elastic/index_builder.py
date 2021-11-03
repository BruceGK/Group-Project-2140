from elasticsearch import Elasticsearch, helpers
import requests
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_loader import DataLoader
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ES_HOST = getenv("ES_URL")

class IndexBuilder:
    def __init__(self) -> None:
        self.es = Elasticsearch(ES_HOST)

    def info(self):
        return self.es.info()
    
    def create_index(self, name):
        return self.es.indices.create(index=name, ignore=400)
    
    def delete_index(self, name):
        return self.es.indices.delete(index=name, ignore=400)

    def insert_docs(self, docs):
        payload = []
        for doc in docs:
            payload.append()
            
        return helpers.bulk(self.es, payload)

def main():
    builder = IndexBuilder()
    print(builder.info())
    res = builder.create_index("cord_test")
    print(res)
    res = builder.delete_index("cord_test")
    print(res)

if __name__ == "__main__":
    main()
