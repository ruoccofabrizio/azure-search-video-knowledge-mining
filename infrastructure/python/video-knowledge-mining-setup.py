import requests
import json
from pprint import pprint
from dotenv import load_dotenv
import os

# Azure Cognitive Search Configuration
load_dotenv()
search_key = os.environ["search_service"]
search_service = os.environ["search_api_key"]

headers = {
    'api-key' : search_key,
    'Content-Type' : 'application/json'
}

# Define Azure Cognitive Search - Main index
with open('./video-knowledge-mining-index.json') as json_file:
    data = json.load(json_file)

index_name = "video-knowledge-mining-index"

url = f"https://{search_service}.search.windows.net/indexes/{index_name}?api-version=2019-05-06"

response = requests.put(url=url, data= json.dumps(data), headers=headers)
pprint(response.json())

# Define Azure Cognitive Search - Time references index
with open('./video-knowledge-mining-index-time-references.json') as json_file:
    data = json.load(json_file)

index_name = "video-knowledge-mining-index-time-references"

url = f"https://{search_service}.search.windows.net/indexes/{index_name}?api-version=2019-05-06"

response = requests.put(url=url, data= json.dumps(data), headers=headers)
pprint(response.json())