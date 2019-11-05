
# -*- coding: utf-8 -*-

import wikipedia


def fetch_content_from_wikipedia(content):
    print('> [text-collection] Starting...')
    print('> [text-collection] Fetching content from wikipedia')

    wikipedia_response = wikipedia.page(content['search_term'])
    content['source_content_original'] = wikipedia_response.content
    sanitize_content(content)

    print('> [text-collection] Fetching done')


def sanitize_content(content):
    print(content['source_content_original'])
