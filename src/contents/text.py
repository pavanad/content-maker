
# -*- coding: utf-8 -*-

import wikipedia

def fetch_content_from_wikipedia(search_term):
    print('> [text-collection] Starting...')
    print('> [text-collection] Fetching content from wikipedia')
    wikipedia_response = wikipedia.page(search_term)
    print('> [text-collection] Fetching done')
    return wikipedia_response.content