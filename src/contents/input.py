# -*- coding: utf-8 -*-

from pick import pick


def ask_search_term(content):
    content["search_term"] = input("Type a Wikipedia search term: ")


def ask_prefix(content):
    title = "Please choose on option: "
    options = ["Who is", "What is", "The history of"]
    option, index = pick(options, title)
    content["prefix"] = option
