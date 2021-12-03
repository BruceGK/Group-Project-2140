from flask import Flask
from flask import request
from search.elastic_index_reader import IndexReader
from search.data_loader import DataLoader
from os import getenv

app = Flask(__name__)
DATA_DIR = getenv("CORD_DIR")
loader = DataLoader(DATA_DIR if DATA_DIR else '../data/2020-07-16')
loader.load_metadata_mappings(loader.load_metadata())


@app.route("/")
def test():
    return "Test"


@app.route("/search")
def search():
    query = request.args.get("q")
    start = request.args.get("start")
    reader = IndexReader()
    result = reader.search("cord_test", query, start_from=start)
    return result['hits']


@app.route("/details/<paperId>")
def detail(paperId):
    data = loader.load_paper_data(paperId)
    return data


if __name__ == "__main__":
    app.run()
