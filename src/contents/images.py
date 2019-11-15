# -*- coding: utf-8 -*-

import os

import requests
from googleapiclient.discovery import build

# google credentials
API_KEY = os.environ.get("GOOGLE_API_KEY")
CSE_KEY = os.environ.get("GOOGLE_CSE_KEY")

# create resource for request
resource = build("customsearch", "v1", developerKey=API_KEY).cse()


def fetch_images_from_google(content: dict):
    print("> [images-collection] Starting...")
    fetch_images_all_sentences(content)


def fetch_images_all_sentences(content: dict):
    sentences = content["sentences"]
    for i, sentence in enumerate(sentences):
        query = f"{content['search_term']} {sentence['keywords'][0]}"
        result = resource.list(q=query, cx=CSE_KEY, searchType="image").execute()
        print(f"> [images-collection] Querying Google Images with: {query}")
        sentence["images"] = [item["link"] for item in result["items"]]
        sentence["google_search_query"] = query

        download_images(sentence["images"], i)


def download_images(images: list, sentence_index: int):
    downloaded_images = []
    for i, url in enumerate(images):
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("Bad request in url of the image")
            if url in downloaded_images:
                raise Exception("Image already downloaded")

            with open(f"data/images/{sentence_index}.png", "wb") as image:
                image.write(response.content)
                image.close()

            downloaded_images.append(url)
            print(
                f"> [images-collection] [{sentence_index}][{i}] Image successfully downloaded: {url}"
            )
            break
        except Exception as e:
            print(f"> [images-collection] [{sentence_index}][{i}] Error ({url}): {e}")

