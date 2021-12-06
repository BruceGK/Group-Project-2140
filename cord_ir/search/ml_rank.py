import lightgbm as lgb
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import coo_matrix, hstack, vstack


class MlRanker():
    def __init__(self, model_path, tfidf_path, docMat_path) -> None:
        self.ranker = joblib.load(model_path)
        self.vectorizer = joblib.load(tfidf_path)
        # docMat = joblib.load(docMat_path)
        # self.docMatrix = docMat['matrix']
        # self.cordIds = docMat['cordIds']

    def rank(self, query, retrieved, loader):
        query_vec = self.vectorizer.transform([query])
        # get all the main text of retrieved documents
        all_text = []
        res_list = []
        for doc in retrieved:
            paper_data = loader.load_paper_data(doc['_id'])
            if paper_data:
                main_text = paper_data['data']['main_text']
                all_text.append(main_text)
                res_list.append(doc)
        text_vec = self.vectorizer.transform(all_text)
        del all_text
        testInput = hstack(
            [text_vec, vstack([query_vec for i in range(len(res_list))])])
        scores = self.ranker.predict(testInput)
        rank_indexes = sorted(
            range(scores.shape[0]), key=lambda k: scores[k], reverse=True)
        return [res_list[i] for i in rank_indexes]

    # def whole_rank(self, query, loader, size=20):
    #     query_vec = self.vectorizer.transform([query])
    #     text_vec = self.docMatrix
    #     testInput = hstack(
    #         [text_vec, vstack([query_vec for i in range(text_vec.shape[0])])])
    #     scores = self.ranker.predict(testInput)
    #     rank_indexes = sorted(
    #         range(scores.shape[0]), key=lambda k: scores[k], reverse=True)
    #     paper_data = []
    #     for i in rank_indexes[:size]:
    #         paper = loader.load_paper_data(self.cordIds[i])
    #         if paper:
    #             paper_data.append({
    #                 "_id": self.cordIds[i],
    #                 "fields": {"title": paper['data']['title']}
    #             })
    #     return paper_data


if __name__ == '__main__':
    from data_loader import DataLoader
    ranker = MlRanker("../../data/models/ranker.joblib",
                      "../../data/models/tfidf.joblib",
                      "../../data/models/docMatrix.joblib")
    print(ranker.ranker)
    print(ranker.vectorizer)
    loader = DataLoader('../../data/2020-07-16')
    loader.load_metadata_mappings(loader.load_metadata())
    # ranker.whole_rank('vaccine', loader)
