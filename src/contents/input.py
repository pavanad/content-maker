# -*- coding: utf-8 -*-

import sys

from colorama import Fore


def ask_search_term(content: dict):
    resp = input("\n> Choose language for search [en/pt] ").lower().strip()
    if resp not in ["en", "pt"]:
        print(
            f"\n> {Fore.CYAN}[content-maker]{Fore.RESET} {Fore.RED}Language not supported{Fore.RESET}\n"
        )
        sys.exit(0)

    content["language"] = resp
    content["search_term"] = input("\n> Type a Wikipedia search term: ")


def ask_yes_or_no(question):
    resp = input(f"\n{question} [Y/n] ").lower().strip()
    if resp[0] == "y":
        return True
    return False


def ask_proceed_fetch_download_nltk():
    return ask_yes_or_no("> Proceed with download data packages (nltk)")


def ask_proceed_fetch_images():
    return ask_yes_or_no("> Proceed with fetch images")


def ask_proceed_publish_google():
    return ask_yes_or_no("> Proceed with publish in google drive")


def ask_prefix(content: dict):
    title = "> Please choose on option: "
    options = ["Who is", "What is", "The history of"]
    # option, index = pick(options, title)
    content["prefix"] = option
