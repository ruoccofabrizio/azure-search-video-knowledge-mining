import logging
import azure.functions as func
import os
import requests
import urllib.parse
from datetime import datetime, timedelta
from azure.storage.blob import generate_container_sas
from azure.identity import ManagedIdentityCredential, AzureCliCredential, ChainedTokenCredential

# Function triggered by Blob Storage Input
def main(event: func.EventGridEvent):
    # Generate Shared Access Signature to access the video on Azure Blob Storage
    event_data = event.get_json()
    url = event_data['url']
    logging.info(f"Python blob trigger function processed blob: {url}")
    name = url.split('/')[-1]
    sas_url = get_sas_url(url)
    logging.info(sas_url)
    # Call Video Indexer service with Shared Access Signature to index the video
    video_result = start_video_indexing(name ,sas_url)
    logging.info(video_result)

# Define function to create Shared Access Signature
def get_sas_url(uri: str):
    # Get Azure Blob Storage configuration
    blob_account            = os.environ["blob_account"]
    blob_key                = os.environ["blob_key"]
    blob_container_source   = os.environ["blob_container_source"]

    # Generate Shared Access Signature with read permission
    sas_token = generate_container_sas(blob_account,blob_container_source, blob_key, permission="r", expiry=datetime.utcnow() + timedelta(hours=3))
    return uri + '?' + sas_token
    

# Call Video Indexer to perform video processing
def start_video_indexing(video_name: str, video_url: str):
    # Get Video Indexer configuration
    endpoint        = os.environ["video_indexer_endpoint"]
    account_id      = os.environ["video_indexer_account_id"]
    location        = os.environ["video_indexer_location"]
    resource_id     = os.environ["video_indexer_resource_id"]

    # Get Azure Function URL to set as callback from video indexer
    function_url    = os.environ["function_url"]
    
    # Get access token to AVAM using ManagedIdentity from Azure Function or AzureCLI when executing locally
    credential = ChainedTokenCredential(ManagedIdentityCredential(), AzureCliCredential())
    access_token = credential.get_token("https://management.azure.com")
    url = f"https://management.azure.com{resource_id}/generateAccessToken?api-version=2021-10-18-preview"
    headers = {
        "Authorization" : f"Bearer {access_token.token}"
    }
    body = {
    "permissionType": "Contributor",
    "scope": "Account"
    }
    response = requests.post(url, headers=headers, json=body)




    # Retrieve access token to perform operation on Video Indexer
    access_token = response.json()['accessToken']

    # Call Video Indexer to start processing the video
    video_url = urllib.parse.quote(video_url)
    video_name = video_name.split('/')[-1] # extract just video name, remove container and folder path
    video_name = urllib.parse.quote(video_name)
    function_url = urllib.parse.quote(function_url)
    privacy = "Private" # Set visibility for the video [Private, Public]

    upload_video_url = f"{endpoint}/{location}/Accounts/{account_id}/Videos?accessToken={access_token}&name={video_name}&videoUrl={video_url}&privacy={privacy}&callbackUrl={function_url}&language=auto"
    logging.info(upload_video_url)
    upload_result = requests.post(upload_video_url)

    return upload_result.json()