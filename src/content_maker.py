# -*- coding: utf-8 -*-

from contents.images import fetch_images_from_google
from contents.input import ask_prefix, ask_search_term
from contents.text import fetch_content_from_wikipedia


def main():

    # data struct
    content = {}

    # ask search term and prefix
    ask_search_term(content)
    # ask_prefix(content)

    # fetch content wikipedia and google images
    fetch_content_from_wikipedia(content)
    fetch_images_from_google(content)


if __name__ == "__main__":
    main()
