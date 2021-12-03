
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

    def search(self, index_name, query, start_from=0):
        return self.es.search(
            index=index_name,
            _source=False,
            from_=start_from,
            size=20,
            highlight={"fields": {"main_text": {
                "number_of_fragments": 1, "fragment_size": 500}}},
            fields=["title"],
            query={"query_string": {"query": query}}
        )


def main():
    reader = IndexReader()
    res = reader.search(
        "cord_test", "will SARS-CoV2 infected people develop immunity? Is cross protection possible?")
    print(res)


if __name__ == '__main__':
    main()
