# -*- coding: utf-8 -*-

import nltk
from colorama import Fore

from contents.article import create_pdf_article
from contents.images import fetch_images_from_google
from contents.input import (
    ask_proceed_fetch_download_nltk,
    ask_proceed_fetch_images,
    ask_proceed_publish_google,
    ask_search_term,
)
from contents.publish import publish_content
from contents.text import fetch_content_from_wikipedia


def main():

    # data struct
    content = {}

    try:

        # download data packages nltk
        if ask_proceed_fetch_download_nltk():
            nltk.download("punkt")
            nltk.download("stopwords")

        ask_search_term(content)

        # fetch content wikipedia and google images
        fetch_content_from_wikipedia(content)

        if ask_proceed_fetch_images():
            fetch_images_from_google(content)

        # create article
        create_pdf_article(content)

        # publish content
        if ask_proceed_publish_google():
            publish_content(content)

    except Exception as e:
        print(
            f"\n> {Fore.CYAN}[content-maker]{Fore.RESET} {Fore.RED}{str(e)}{Fore.RESET}\n"
        )
        print(str(e))


if __name__ == "__main__":
    main()
