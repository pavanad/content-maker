# -*- coding: utf-8 -*-

from contents.text import fetch_content_from_wikipedia
from contents.input import ask_search_term, ask_prefix

def main():

    # data struct
    content = {}

    # ask search term and prefix
    ask_search_term(content)
    ask_prefix(content)

    # fetch content wikipedia
    fetch_content_from_wikipedia(content)    

if __name__ == "__main__":
    main()