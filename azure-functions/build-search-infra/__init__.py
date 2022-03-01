import datetime, logging, os, json, requests
import azure.functions as func

def create_index():
    #   GET https://[servicename].search.windows.net/indexes/[index name]?api-version=[api-version]  
    #       Content-Type: application/json  
    #       api-key: [admin key]   

    url = f"https://{os.getenv('search_account')}.search.windows.net/indexes/{os.getenv('search_index')}?api-version={os.getenv('search_api_version')}"

    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv('search_api_key')
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 404:
    #   PUT https://[servicename].search.windows.net/indexes/[index name]?api-version=[api-version]
    #       Content-Type: application/json
    #       api-key: [admin key]

        url = f"https://{os.getenv('search_account')}.search.windows.net/indexes/{os.getenv('search_index')}?api-version={os.getenv('search_api_version')}"

        with open(r'./build-search-infra/infrastructure/video-knowledge-mining-index.json') as file:
            body = json.load(file)

        r = requests.put(url, headers=headers, json=body)

        
        url = f"https://{os.getenv('search_account')}.search.windows.net/indexes/{os.getenv('search_index')}-time-references?api-version={os.getenv('search_api_version')}"
        with open(r'./build-search-infra/infrastructure/video-knowledge-mining-index-time-references.json') as file:
            body = json.load(file)

        r = requests.put(url, headers=headers, json=body)

    else:
        logging.info(f"Index set up done. {r.status_code}")


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')
    
    create_index()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

