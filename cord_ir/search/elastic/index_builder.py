from elasticsearch import Elasticsearch
import requests
from search.data_loader import DataLoader
from dotenv import load_dotenv

load_dotenv()

class IndexBuilder:
    def __init__(self) -> None:
        self.es = Elasticsearch()
    
    def create_index(self):
        requests.put()
    

