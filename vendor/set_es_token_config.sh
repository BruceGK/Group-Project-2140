curl -X PUT \
   --header 'Content-Type: application/json' \
   --data '{"index":{"analyze":{"max_token_count": 2000000}}}' \
   http://127.0.0.1:9200/cord_test/_settings
curl -X PUT \
   --header 'Content-Type: application/json' \
   --data '{"index" : {"highlight.max_analyzed_offset" : 60000000}}' \
   http://127.0.0.1:9200/cord_test/_settings
