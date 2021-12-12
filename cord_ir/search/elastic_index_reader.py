
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ES_HOST = getenv("ES_URL")


class IndexReader:
    def __init__(self) -> None:
        self.es = Elasticsearch(
            ES_HOST, request_timeout=60, max_retries=10, retry_on_timeout=True)

    def info(self):
        return self.es.info()

    def search(self, index_name, query, start_from=0, size=20, fields=["title"], highlight=True):
        reserved = '+ - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /'.split(' ')
        for char in reserved:
            query = query.replace(char, '\\' + char)
        highlight_config = {"fields": {
            "main_text": {
                "number_of_fragments": 1,
                "fragment_size": 150
            },
            "abstract": {
                "number_of_fragments": 1,
                "fragment_size": 150
            },
            "title": {
                "number_of_fragments": 1,
                "fragment_size": 150
            }
        }} if highlight else None
        return self.es.search(
            index=index_name,
            _source=False,
            from_=start_from,
            size=size,
            highlight=highlight_config,
            fields=fields,
            query={"query_string": {"query": query}}
        )

    def boolean_search(self, index_name, query, start_from=0, size=20, fields=["title"], highlight=True):
        reserved = '+ - = && || > < ! ( ) { } [ ] ^ " ~ * ? : \ /'.split(' ')
        highlight_config = {"fields": {
            "main_text": {
                "number_of_fragments": 1,
                "fragment_size": 150
            },
            "abstract": {
                "number_of_fragments": 1,
                "fragment_size": 150
            },
            "title": {
                "number_of_fragments": 1,
                "fragment_size": 150
            }
        }} if highlight else None
        return self.es.search(
            index=index_name,
            _source=False,
            from_=start_from,
            size=size,
            highlight=highlight_config,
            fields=fields,
            query=query
        )

    def tokenize(self, sentence, index_name='cord_test'):
        return self.es.indices.analyze(
            index=index_name,
            body={
                "tokenizer": "standard",
                "text": sentence,
            })


def main():
    reader = IndexReader()
    res = reader.search(
        "cord_test", "will SARS-CoV2 infected people develop immunity? Is cross protection possible?")
    print(res)


if __name__ == '__main__':
    main()
