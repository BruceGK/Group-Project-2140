import sys
import os
from elasticsearch import Elasticsearch, helpers
from data_loader import DataLoader
from tqdm import tqdm
from os import getenv
from dotenv import load_dotenv

load_dotenv()
ES_HOST = getenv("ES_URL")
DATA_DIR = getenv("CORD_DIR")

class IndexBuilder:
    def __init__(self) -> None:
        self.es = Elasticsearch(ES_HOST, request_timeout=90)

    def info(self):
        return self.es.info()

    def create_index(self, name):
        return self.es.indices.create(index=name, ignore=400)

    def delete_index(self, name):
        return self.es.indices.delete(index=name, ignore=400)

    def insert_docs(self, index_name, doc_type, docs):
        payload = []
        for doc in docs:
            payload.append({
                "_index": index_name,
                "_id": doc['docno'],
                "_op_type": "create",
                "_source": doc['data']
            })

        return helpers.bulk(self.es, payload)


def main():
    builder = IndexBuilder()
    print(builder.info())
    try:
        res = builder.delete_index("cord_test")
        print(res)
    except Exception as e:
        print(e)
    res = builder.create_index("cord_test")
    print(res)
    loader = DataLoader(DATA_DIR if DATA_DIR else '../../data/2020-07-16')
    metadata = loader.load_metadata()
    tqdm.pandas()
    cum_count = 0
    cum_data = []

    uidset = set()

    def process_row(r):
        nonlocal cum_count
        nonlocal cum_data
        row_data = loader.load_paper_data(r)
        if row_data is not None and row_data['docno'] not in uidset:
            uidset.add(row_data["docno"])
            cum_data.append(row_data)
            cum_count += 1
            if cum_count % 6000 == 0:
                # flush to index
                builder.insert_docs("cord_test", "paper", cum_data)
                cum_data = []
    metadata.progress_apply(process_row, axis=1)
    if len(cum_data) != 0:
        builder.insert_docs("cord_test", "paper", cum_data)
        cum_data = []
    print('%s documents processed' % cum_count)

    # res = builder.delete_index("cord_test")
    # print(res)


if __name__ == "__main__":
    main()
