#! usr/bin/env python3
"""
Controls the entire FST: get-morphology. Gets morphology from Bosworth-Toller, then
gets morphology from RULES.

To import the methods, use control_module.py
"""

# _______________________________ IMPORTS
import data_bt_closed_class
import data_sjh_closed_class
import get_text
import steve_openClass
import flatten
import rank

# import html

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
    # optional list is data_steve_list.json but it won't allow for multiple POSs

    result = data_sjh_closed_class.get_pos(word)
    return result


def check_btjson(unknown_word):

    # bt_link = go_online_bt.get_link(open_class_word)
    # return bt_link

    reply = data_bt_closed_class.get_pos(unknown_word)
    return reply


def check_rawbt(unknown):

    last_chance = data_bt_closed_class.get_rawentry(unknown)
    return last_chance


def check_brights(notknown):

    brights = data_bt_closed_class.get_brights(notknown)
    return brights


def check_texas(subject):

    texas = data_bt_closed_class.get_texas(subject)
    return texas


def check_clark(whatchamacallit):   # will become ClarkGood

    ch = data_bt_closed_class.get_clark(whatchamacallit)
    return ch


def check_steveOpenClass(query):
    soc = steve_openClass.open_classGuess(query)
    return soc


def process_items_serially(query, wordclass):

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
        print('* ', end='')

    return query, wordclass


def process_items_comprehensively(query):

    wordclass = []

    wordclass.append((check_stevelist(query)))  # checks my closed-class list

    wordclass.append((check_btjson(query)))  # checks JSON version of Bosworth-Toller

    wordclass.append((check_rawbt(query))) # checks raw data version of Bosworth-Toller

    wordclass.append((check_brights(query)))

    wordclass.append((check_texas(query)))

    wordclass.append((check_clark(query)))

    wordclass.append((check_steveOpenClass(query)))

    return query, wordclass


def get_a_sentence(genre):
    thisOne = get_text.random_sentence(genre)     # gets a random sentence from poetry
    return thisOne

# this_text = get_text.user_choice()                   #  gets a user-defined text to feed into the parser


totalwords = 0
foundwords = 0

this_text = get_a_sentence('prose')
this_text = this_text.strip()
this_text = re.sub('[\\\/\"\'\(\)\.\,\;0-9]', '', this_text)

print('\n', colored(this_text, 'blue', attrs=['underline']), '\n')

each_word = this_text.split()

# array for holding formatted results
fancy_word = []
fancy_pos = []

for word in each_word:

    totalwords += 1
    gotsomething = False

    # _, item2 = process_items_serially(item1, item2)
    # if item2 != []:
    #     foundwords += 1

    item1, item2 = process_items_comprehensively(word)

    fancy_word.append(item1)

    found_something = any(len(elem) > 0 for elem in item2)
    if found_something:
        foundwords += 1
        gotsomething = True

    # prepare data for printing
    flat_list = flatten.flatten(item2)
    ranking, likely = rank.rank(item2)

    if gotsomething is True:
        print(colored(item1, 'red'), flat_list, colored(ranking, 'yellow', attrs=['bold']), likely)
        fancy_pos.append(likely)
    else:
        print(colored(item1, 'blue'))

    #   list of words, then list of best guesses, then regularize them and zip them

print(colored('\nFOUND {} of {} words'.format(foundwords, totalwords), 'green', attrs=['bold']))

fancydan = zip(fancy_word, fancy_pos)
print(*fancydan)

# html.make_html(display_results)
