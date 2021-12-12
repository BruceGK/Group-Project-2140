gdown --id $INDEX_ID
unzip index.zip
cp -r data/nodes /var/lib/elasticsearch
chown -R elasticsearch:elasticsearch /var/lib/elasticsearch
