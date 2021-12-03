gdown --id $INDEX_ID -o data.zip
unzip data.zip
cp -r data/nodes /var/lib/elasticsearch
chown -R elasticsearch:elasticsearch /var/lib/elasticsearch
