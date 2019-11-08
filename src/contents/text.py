# -*- coding: utf-8 -*-

import re
from string import punctuation

import wikipedia
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def fetch_content_from_wikipedia(content: dict):
    print("> [text-collection] Starting...")
    print("> [text-collection] Fetching content from wikipedia")

    wikipedia_response = wikipedia.page(content["search_term"])
    content["source_content_original"] = wikipedia_response.content
    sanitize_content(content)
    content_to_sentences(content)

    print("> [text-collection] Fetching done")


def sanitize_content(content: dict):
    """Sanitize content from wikipedia"""

    # remover markdown wikipedia and single space
    source_content_sanitize = re.sub(r"=.*", " ", content["source_content_original"])
    source_content_sanitize = re.sub(r"\s+", " ", source_content_sanitize)

    content["source_content_sanitize"] = source_content_sanitize


def content_to_sentences(content: dict):
    """Converting text to sentences"""

    content_sentences = []
    sentences = sent_tokenize(content["source_content_sanitize"])
    stopwords_list = set(stopwords.words("english") + list(punctuation))

    for sentence in sentences:
        keywords = get_keywords(sentence, stopwords_list)
        content_sentences.append({"text": sentence, "keywords": keywords, "images": []})

    content["sentences"] = content_sentences


def get_keywords(sentence: str, stopwords_list: set) -> list:
    words = word_tokenize(sentence)
    return [w for w in words if w not in stopwords_list]
