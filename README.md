---
page_type: sample
languages:
- python
products:
- azure
description: "Video Knowledge Mining Solution"
urlFragment: azure-search-video-knowledge-mining
---

# Azure Cognitive Search - Video Knowledge Mining Extension

![architecture](./architecture.JPG "Archicture diagram")

# Demo site
[Video Knowledge Mining Demo](https://video-knowledge-mining.azurewebsites.net/)

# Extend Azure Cognitive Search
Extend [Azure Cognitive Search](https://docs.microsoft.com/azure/search/cognitive-search-concept-intro) capabilities enabling video transcripts and insights search, through an integration with [Azure Video Indexer](https://docs.microsoft.com/en-us/azure/media-services/video-indexer/video-indexer-get-started).

## Video insights
* Face detection: Detects and groups faces appearing in the video.
* Celebrity identification: Video Indexer automatically identifies over 1 million celebrities—like world leaders, actors, actresses, athletes, researchers, business, and tech leaders across the globe. The data about these celebrities can also be found on various websites (IMDB, Wikipedia, and so on).
* Account-based face identification: Video Indexer trains a model for a specific account. It then recognizes faces in the video based on the trained model. For more information, see Customize a Person model from the Video Indexer website and Customize a Person model with the Video Indexer API.
* Thumbnail extraction for faces ("best face"): Automatically identifies the best captured face in each group of faces (based on quality, size, and frontal position) and extracts it as an image asset.
* Visual text recognition (OCR): Extracts text that's visually displayed in the video.
* Visual content moderation: Detects adult and/or racy visuals.
* Labels identification: Identifies visual objects and actions displayed.
* Keyframe extraction: Detects stable keyframes in a video.

This repo is a collection of two skills:  
* [start-video-indexing](azure-functions/start-video-indexing) (trigger a video indexing starting from a video upload in Azure Blob Storage)  
![architecture-start-video-indexing](azure-functions/start-video-indexing/start-video-indexer.png "Archicture diagram")

* [video-indexer-callback](azure-functions/video-indexer-callback) (callback from Azure Blob Storage and push data to Azure Cognitive Search and Azure Blob Storage)
![architecture-video-indexer-callback](azure-functions/video-indexer-callback/video-indexer-callback.png "Archicture diagram")
