from os import path
import pandas as pd
from tqdm import tqdm
import sys
import json

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
        res = pd.read_csv(path.join(self.subfolder, 'metadata.csv'), dtype=str)
        return res

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
    
    def load_paper_data(self, row):
        file_path = ''
        if isinstance(row, str):
            file_path = row
        elif not pd.isna(row['pdf_json_files']):
            file_path = row['pdf_json_files']
        elif not pd.isna(row['pmc_json_files']):
            file_path = row['pmc_json_files']
        else:
            return None
        with open(path.join(self.subfolder, file_path), 'r') as f:
            data = json.load(f)
            return data
        
    def get_full_body_text(self, paperData):
        body = paperData['body_text']
        return ' '.join(map(lambda e : e['text'], body))

if __name__ == '__main__':
    loader = DataLoader('../data/2020-7-16')
    print('relevance:', len(loader.load_relevance()))
    print('docids:', len(loader.load_valid_docids()))
    metadata = loader.load_metadata()
    print('metadata:', metadata.shape)
    tqdm.pandas()
    metadata.progress_apply(lambda r: loader.get_full_body_text(loader.load_paper_data(r)), axis=1)


