# -*- coding: utf-8 -*-

from contents.text import fetch_content_from_wikipedia
from contents.input import ask_search_term, ask_prefix

def main():

    # ask search term and prefix
    search_term = ask_search_term()
    prefix = ask_prefix()

    # fetch content wikipedia
    wikipedia_content = fetch_content_from_wikipedia(search_term)

if __name__ == "__main__":
    main()