#! usr/bin/env python3
"""
Like control.py, which is for testing, but called by another python script. Execute this with work_on_words(prompt)
Needs a PROMPT: either 'random' or a sentence.
Controls FST: get-morphology. Gets morphology from Bosworth-Toller, then
gets morphology from RULES. 
"""

# _______________________________ IMPORTS
import data_bt_closed_class
import data_sjh_closed_class
import get_text
import steve_openClass
from itertools import zip_longest
# import flatten
import rank

# import go_online_bt

from termcolor import colored
import re

# _______________________________ DEFS


def get_usertext():
    path = get_text.user_choice()
    if path is None:
        text = input('Enter text: ')
    else:
        whole_text = get_text.load_text(path)
        text = whole_text.split()
    return text


def check_stevelist(term):
    # optional list is data_steve_list.json but that one won't allow for multiple POSs

    result = data_sjh_closed_class.get_pos(term)
    return result


def check_btjson(unknown_word):

    # bt_link = go_online_bt.get_link(open_class_word)
    # return bt_link

    reply = data_bt_closed_class.get_pos(unknown_word)
    return reply


def check_rawbt(unknown):
    # checks the raw Bosworth-Toller, which is in bytes, not strings.

    last_chance = data_bt_closed_class.get_rawentry(unknown)
    return last_chance


def check_brights(notknown):

    brights = data_bt_closed_class.get_brights(notknown)
    return brights


def check_texas(subject):

    texas = data_bt_closed_class.get_texas(subject)
    return texas


def check_clark(whatchamacallit):   # will become ClarkGood when it is fully edited

    ch = data_bt_closed_class.get_clark(whatchamacallit)
    return ch


def check_steveOpenClass(query):
    soc = steve_openClass.open_classGuess(query)
    return soc


def process_items_serially(query):
    """
    Checks the wordlists serially (one at a time) until a value is found.

    param query: the word to look for
    :return: tuple of original word (string) and its part of speech (string)
    """
    wordclass = []

    if wordclass == []:
        wordclass = (check_btjson(query))  # checks JSON version of Bosworth-Toller

    if wordclass == []:
        wordclass = (check_rawbt(query))  # checks raw data version of Bosworth-Toller

    if wordclass == []:
        wordclass = (check_brights(query))

    if wordclass == []:
        wordclass = (check_texas(query))

    if wordclass == []:
        wordclass = (check_clark(query))

    if wordclass == []:
        wordclass = (check_steveOpenClass(query))

    return query, wordclass


def process_items_comprehensively(query):
    """
    Takes a word and checks all word lists. It appends every result to a long list.
    It is comprehensive in its search, since it checks every list no matter what.
    This allows rank.py to add weights to all the guesses.
    param query: the word to look for
    :return: tuple of original word (string) and all possible parts of speech (list)
    """

    wordclass = []

    wordclass.append((check_stevelist(query)))  # checks my closed-class list

    wordclass.append((check_btjson(query)))  # checks JSON version of Bosworth-Toller

    wordclass.append((check_rawbt(query)))  # checks raw data version of Bosworth-Toller

    wordclass.append((check_brights(query)))  # checks Brights OE glossary

    wordclass.append((check_texas(query)))  # checks an onoline glossary from Texas

    wordclass.append((check_clark(query)))  # checks edited online verison of Clark-Hall

    wordclass.append((check_steveOpenClass(query)))  # guesses at word class by inflection

    return query, wordclass


def get_a_sentence(genre):
    thisOne = get_text.random_sentence(genre)     # gets a random sentence from poetry, prose, bible, ...
    return thisOne

# this_text = get_text.user_choice()              #  gets a user-defined text to feed into the parser


def work_on_sentence(genre):
    this_text = get_a_sentence(genre)
    this_text = this_text.strip()
    this_text = re.sub('[\\\/\"\'\(\)\.\,\;0-9]', '', this_text)

    print('\n', colored(this_text, 'blue', attrs=['underline']), '\n')

    each_word = this_text.split()

    return each_word


def work_on_words(prompt):
    totalwords = 0
    foundwords = 0

    if prompt == 'random':
        each_word = work_on_sentence('prose')
    else:
        each_word = prompt.split()

    # array for holding formatted results
    fancy_word = []
    fancy_pos = []

    for word in each_word:
        totalwords += 1
        gotsomething = False

        # the quick way is to return the first value found; use process_items_serially for that
        # _, item2 = process_items_serially(item1, item2)
        # if item2 != []:
        # foundwords += 1

        item1, item2 = process_items_comprehensively(word)

        # put the word into the first element of the results-tuple
        fancy_word.append(item1)

        found_something = any(len(elem) > 0 for elem in item2)
        if found_something:
            foundwords += 1   # used for testing
            gotsomething = True

        # flat_list = flatten.flatten(item2)
        ranking, likely = rank.rank(item2)

        if gotsomething is True:
            # put the likeliest parts of speech into the second element of the results-tuple
            fancy_pos.append(likely)
        else:
            pass

    # zip the two lists and return them to the calling script; make sure the lists are equally long
    fancydan = zip_longest(fancy_word, fancy_pos, fillvalue='')
    return fancydan

    # for testing:
    # print(colored('\nFOUND {} of {} words'.format(foundwords, totalwords), 'green', attrs=['bold']))
