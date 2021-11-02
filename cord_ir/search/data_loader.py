from os import path


class DataLoader:
    def __init__(self, subfolder):
        self.subfolder = subfolder
        super().__init__()

    def load_valid_docids(self):
        res = []
        with open(path.join(self.subfolder, 'eval', 'docids-rnd5.txt'), 'r') as f:
            for line in f:
                res.append(line)
        return res

    def load_metadata(self):
        pass

    def load_relevance(self):
        res = []
        with open(path.join(self.subfolder, 'eval', 'qrels-covid_d5_j0.5-5.txt'), 'r') as f:
            for line in f:
                query_id, round_no, docid, relevance = line.split(' ')
                res.append({
                    query_id: query_id,
                    round_no: round_no,
                    docid: docid, 
                    relevance: relevance
                })
        return res
    

if __name__ == '__main__':
    loader = DataLoader('../data/2020-7-16')
    print('relevance:', len(loader.load_relevance()))
    print('docids:', len(loader.load_valid_docids()))



