from os import path
import pandas as pd
from tqdm import tqdm
import sys
import json


class DataLoader:
    def __init__(self, subfolder):
        self.subfolder = subfolder
        super().__init__()

    def load_valid_docids(self) -> list:
        res = []
        with open(path.join(self.subfolder, 'eval', 'docids-rnd5.txt'), 'r') as f:
            for line in f:
                res.append(line)
        return res

    def load_metadata(self) -> pd.DataFrame:
        res = pd.read_csv(path.join(self.subfolder, 'metadata.csv'), dtype=str)
        return res

    def load_relevance(self) -> list:
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

    def load_paper_data(self, row) -> dict:
        file_path = ''
        if isinstance(row, str):
            file_path = row
        elif not pd.isna(row['pdf_json_files']):
            file_path = row['pdf_json_files'].split(';')[0]
        elif not pd.isna(row['pmc_json_files']):
            file_path = row['pmc_json_files'].split(';')[0]
        else:
            return None
        with open(path.join(self.subfolder, file_path), 'r') as f:
            data = json.load(f)
            data['main_text'] = self.get_full_body_text(data)
            return data

    def get_full_body_text(self, paperData) -> str:
        if paperData is None:
            return None
        body = paperData['body_text']
        return ' '.join(map(lambda e: e['text'], body))


def main():
    loader = DataLoader('../../data/2020-7-16')
    print('relevance:', len(loader.load_relevance()))
    print('docids:', len(loader.load_valid_docids()))
    metadata = loader.load_metadata()
    print('metadata:', metadata.shape)
    tqdm.pandas()
    paper_data = []
    empty_count = 0
    total_len = 0

    def process_row(r):
        nonlocal empty_count
        nonlocal total_len
        row_data = loader.load_paper_data(r)
        if row_data is not None:
            # paper_data.append(row_data)
            total_len += (len(row_data['main_text']))
        else:
            empty_count += 1
    metadata.progress_apply(process_row, axis=1)
    print("empty count:", empty_count)
    print("total count:", total_len)
    # print(paper_data[0])


if __name__ == '__main__':
    main()
