# Group-Project-2140
Final Project for INFSCI 2140 INFORMATN STORAGE &amp; RETRIEVAL

Production site: https://2140.miguch.com

## Development
1. clone the repo from Github
2. Use script from `vendor` to download elasticsearch
3. Start elasticsearch server
4. Use script `get_data_prod.sh` from `data` to get the data
5. Enter `cord_ir/search` folder and use `python3 elastic_index_builder.py` to build the ES index.
6. In `cord_ir` folder, use `FLASK_ENV=development FLASK_APP=main.py flask run` to start the development server.
7. In `frontend/covidsearch` folder, change the proxy in `vue.config.js` to localhost, then use `yarn serve` to start the frontend

## ML model training
1. Use script `get_data.sh` from `data` to get the training data from TREC-COVID
2. Enter `cord_ir/search` folder and use `CORD_DIR=../../data/2020-07-16 python3 elastic_index_builder.py` to build the ES index for training data.
3. Use the jupyter notebook in `cord_ir/learning/training.ipynb` to train the model.
4. Model data will be exported to `data/models` folder

## Production
1. In `cord_ir` folder, use `FLASK_APP=main.py FLASK_ENV=production python3 -m flask run` to start the production server.
2. In `frontend/covidsearch` folder, use `yarn build` to start the frontend
3. Use Caddy or Nginx to serve the static files from `frontend/covidsearch/dist`, and reverse proxy the location `/api/*` to the python server on localhost:5000.
