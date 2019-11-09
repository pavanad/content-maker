# -*- coding: utf-8 -*-

import os

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
    for sentence in sentences:
        pass
