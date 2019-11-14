# -*- coding: utf-8 -*-

from contents.article import create_pdf_article
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

    # create article
    create_pdf_article(content)


if __name__ == "__main__":
    main()

