# -*- coding: utf-8 -*-

import os

import requests
from colorama import Fore
from googleapiclient.discovery import build

# google credentials
API_KEY = os.environ.get("GOOGLE_API_KEY")
CSE_KEY = os.environ.get("GOOGLE_CSE_KEY")

# create resource for request
resource = build("customsearch", "v1", developerKey=API_KEY).cse()


def fetch_images_from_google(content: dict):
    print(f"\n> {Fore.CYAN}[images-collection]{Fore.RESET} Starting...")
    fetch_images_all_sentences(content)


def fetch_images_all_sentences(content: dict):
    sentences = content["sentences"]
    for i, sentence in enumerate(sentences):
        query = f"{content['search_term']} {sentence['keywords'][0]}"
        result = resource.list(q=query, cx=CSE_KEY, searchType="image").execute()
        print(
            f"> {Fore.CYAN}[images-collection]{Fore.RESET} Querying Google Images with: {Fore.YELLOW}{query}{Fore.RESET}"
        )
        sentence["images"] = [item["link"] for item in result["items"]]
        sentence["google_search_query"] = query

        references = content["references"]
        download_images(references, sentence["images"], i)


def download_images(references: list, images: list, sentence_index: int):
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

            references.append(url)
            downloaded_images.append(url)
            print(
                f"> {Fore.CYAN}[images-collection]{Fore.RESET} [{sentence_index}][{i}] Image {Fore.GREEN}successfully{Fore.RESET} downloaded: {url}"
            )
            break
        except Exception as e:
            print(
                f"> {Fore.CYAN}[images-collection]{Fore.RESET} [{sentence_index}][{i}] {Fore.RED}Error{Fore.RESET} ({url}): {Fore.RED}{e}{Fore.RESET}"
            )
