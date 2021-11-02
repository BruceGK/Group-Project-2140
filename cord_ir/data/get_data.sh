# qrels-covid_d5_j0.5-5.txt
wget -N https://ir.nist.gov/covidSubmit/data/qrels-covid_d5_j0.5-5.txt
# topics-rnd5.xml
wget -N https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml
# docids-rnd5.txt
wget -N https://ir.nist.gov/covidSubmit/data/docids-rnd5.txt
# cord-19_2020-07-16.tar.gz
wget -N https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-07-16.tar.gz
tar xvf cord-19_2020-07-16.tar.gz
mkdir -p 2020-07-16/eval
mv qrels-covid_d5_j0.5-5.txt topics-rnd5.xml docids-rnd5.txt 2020-07-16/eval
cd 2020-07-16
tar xf document_parses.tar.gz
tar xvf cord_19_embeddings.tar.gz
rm document_parses.tar.gz
rm cord_19_embeddings.tar.gz
