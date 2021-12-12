from flask import Flask
from flask import request
from search.ml_rank import MlRanker
from search.elastic_index_reader import IndexReader
from search.data_loader import DataLoader
from os import getenv

app = Flask(__name__)
DATA_DIR = getenv("CORD_DIR")
loader = DataLoader(DATA_DIR if DATA_DIR else '../data/2020-07-16')
loader.load_metadata_mappings(loader.load_metadata())
ranker = MlRanker("../data/models/ranker.joblib",
                  '../data/models/tfidf.joblib',
                  "../data/models/docMatrix.joblib")


@app.route("/")
def test():
    return "Test"


@app.route("/search")
def search():
    query = request.args.get("q")
    start = request.args.get("start")
    reader = IndexReader()
    start = request.args.get("start")
    result = reader.search("cord_test", query, start_from=start)
    return result['hits']


@app.route("/mlsearch")
def mlsearch():
    query = request.args.get("q")
    start = request.args.get("start")
    if start == None:
        start = 0
    if int(start) > 180:
        return 'Due to server limitation, we can only process the top 200 documents in ML mode', 400
    start = int(start)
    reader = IndexReader()
    result = reader.search("cord_test", query, size=200)
    reranked = ranker.rank(query, result['hits']['hits'], loader)
    result['hits']['hits'] = reranked[start:start+20]
    result['hits']['total']['value'] = min(
        result['hits']['total']['value'], 200)
    return result['hits']


@app.route("/details/<paperId>")
def detail(paperId):
    data = loader.load_paper_data(paperId)
    return data


if __name__ == "__main__":
    app.run()
