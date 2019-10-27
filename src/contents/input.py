# -*- coding: utf-8 -*-

from pick import pick

def ask_search_term():
    return input('Type a Wikipedia search term: ')

def ask_prefix():
    title = 'Please choose on option: '
    options = ['Who is', 'What is', 'The history of']
    option, index = pick(options, title)
    return option