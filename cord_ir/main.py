from flask import Flask
from flask import request
from search.elastic_index_reader import IndexReader
from search.data_loader import DataLoader

app = Flask(__name__)
loader = DataLoader('../data/2020-07-16')
loader.load_metadata_mappings(loader.load_metadata())

@app.route("/")
def test():
    return "Test"

@app.route("/search")
def search():
    query = request.args.get("q")
    reader = IndexReader()
    return reader.search("cord_test", query)

@app.route("/details/<paperId>")
def detail(paperId):
    data = loader.load_paper_data(paperId)
    return data

if __name__ == "__main__":
    app.run()