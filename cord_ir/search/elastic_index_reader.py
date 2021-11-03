
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ES_HOST = getenv("ES_URL")


class IndexReader:
    def __init__(self) -> None:
        self.es = Elasticsearch(ES_HOST)

    def info(self):
        return self.es.info()

    def search(self, index_name, query):
        return self.es.search(index=index_name, _source=False,
                              fields=["title"],
                              query={"query_string": {"query": query}})


def main():
    reader = IndexReader()
    res = reader.search(
        "cord_test", "will SARS-CoV2 infected people develop immunity? Is cross protection possible?")
    print(res)


if __name__ == '__main__':
    main()
