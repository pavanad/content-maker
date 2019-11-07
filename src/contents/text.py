# -*- coding: utf-8 -*-

import re
import wikipedia


def fetch_content_from_wikipedia(content):
    print("> [text-collection] Starting...")
    print("> [text-collection] Fetching content from wikipedia")

    wikipedia_response = wikipedia.page(content["search_term"])
    content["source_content_original"] = wikipedia_response.content
    sanitize_content(content)

    print("> [text-collection] Fetching done")


def sanitize_content(content):
    # remover markdown wikipedia and single space
    source_content_sanitize = re.sub(r"=.*", " ", content["source_content_original"])
    source_content_sanitize = re.sub(r"\s+", " ", source_content_sanitize)

    content["source_content_sanitize"] = source_content_sanitize

