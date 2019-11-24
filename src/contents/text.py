# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from heapq import nlargest
from string import punctuation

import wikipedia
from colorama import Fore
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize


def fetch_content_from_wikipedia(content: dict):
    print(f"\n> {Fore.CYAN}[text-collection]{Fore.RESET} Starting...")
    print(f"> {Fore.CYAN}[text-collection]{Fore.RESET} Fetching content from wikipedia")

    # set language for search
    wikipedia.set_lang(content["language"])

    # fech content from wikipedia
    wikipedia_response = wikipedia.page(content["search_term"])
    content["source_content_title"] = wikipedia_response.title
    content["source_content_original"] = wikipedia_response.content
    content["references"] = [wikipedia_response.url]

    # sanitize and convert to sentences
    sanitize_content(content)
    content_to_sentences(content)

    print(
        f"> {Fore.CYAN}[text-collection]{Fore.RESET} Fetching {Fore.GREEN}done{Fore.RESET}"
    )


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
    language = {"en": "english", "pt": "portuguese"}.get(content["language"], "english")
    stopwords_list = set(stopwords.words(language) + list(punctuation))

    words_without_stopwords = get_keywords(
        content["source_content_sanitize"], stopwords_list
    )

    frequency = FreqDist(words_without_stopwords)
    important_sentences = defaultdict(int)

    for index, sentence in enumerate(sentences):
        for w in word_tokenize(sentence.lower()):
            if w in frequency:
                important_sentences[index] += frequency[w]

    # get 20% of sentences for resume
    resume_size = int(len(sentences) * 0.2)
    idx_important_sentences = nlargest(
        resume_size, important_sentences, important_sentences.get
    )

    # save in struct
    for index in sorted(idx_important_sentences):
        keywords = get_keywords(sentences[index], stopwords_list)
        content_sentences.append(
            {"text": sentences[index], "keywords": keywords, "images": []}
        )

    content["sentences"] = content_sentences


def get_keywords(sentence: str, stopwords_list: set) -> list:
    words = word_tokenize(sentence.lower())
    return [w for w in words if w not in stopwords_list]
