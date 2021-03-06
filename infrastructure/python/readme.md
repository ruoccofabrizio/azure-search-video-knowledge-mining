# Infrastructure setup

This script creates the following resources:  
* [Resource Group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview)
* [Azure Storage Account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview)
* [Azure Cognitive Search](https://docs.microsoft.com/en-us/azure/search/search-what-is-azure-search)

The script provisions twor different containers within Azure Blob Storage Account:
* video-drop: for uploading videos to be indexed by Azure Video Indexer
* video-insights: for uploading insights extracted by Azure Video Indexer

Useful python sdk resources:
* [Python - Azure Resource Manager](https://github.com/Azure-Samples/resource-manager-python-resources-and-groups)
* [Python - Azure Storage Account](https://docs.microsoft.com/en-us/samples/azure-samples/storage-python-manage/storage-python-manage/)
* [Python - Create Resource Group](https://docs.microsoft.com/en-us/samples/azure-samples/resource-manager-python-resources-and-groups/manage-azure-resources-and-resource-groups-with-python/#create-resource)
* [Python - Blob Storage SDK](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python#create-a-container)
