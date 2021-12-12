# cord-19_2021-03-08.tar.gz
# 170231 useful records
wget -N https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2021-03-08.tar.gz
tar xvf cord-19_2021-03-08.tar.gz
cd 2021-03-08
tar xf document_parses.tar.gz
# tar xvf cord_19_embeddings.tar.gz
rm document_parses.tar.gz
rm cord_19_embeddings.tar.gz
