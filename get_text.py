#! usr/bin/env python3
"""
Get a random sentence from the OE Corpus or present user with an interface to choose text
"""

import os


def user_choice():

    path = os.getcwd()

    print(""" 
Select text:
    1. Glosses \t2. Beowulf \t3. Judith \t4. Andreas \t5. Genesis \t6. Exodus \t7. Rood \t8. Chr&Sat
    9. Aelfric \t10. Wulfstan \t11. Chronicles \t12. Homilies \t13. All Poetry \t14. All Prose
    """)

    choice = input('Number? ')

    if choice == '1':
        path += '/glosses/glosses_clean.txt'
    if choice == '2':
        path += '/poetry/beowulf.txt'
    if choice == '3':
        path += '/poetry/judith.txt'
    if choice == '4':
        path += '/poetry/andreas.txt'
    if choice == '5':
        path += '/poetry/genesis.txt'
    if choice == '6':
        path += '/poetry/exodus.txt'
    if choice == '7':
        path += '/poetry/rood.txt'
    if choice == '8':
        path += '/poetry/christandsatan.txt'
    if choice == '9':
        path += '/prose/pr_aelfric.txt'
    if choice == '10':
        path += '/prose/pr_wulfstan.txt'
    if choice == '11':
        path += '/prose/pr_chron.txt'
    if choice == '12':
        path += '/prose/pr_hom.txt'
    if choice == '13':
        path += '/poetry/POETRY.txt'
    if choice == '14':
        path += '/prose/PROSE.txt'

    return path


def load_text(selected_path):

    with open(selected_path, 'r') as fp:
        all_text = fp.read()
        return all_text


def random_sentence(genre):     # takes poetry or prose or gloss or bible

    path = os.getcwd()

    import random
    import re
    if genre == 'poetry':
        path += '/poetry/POETRY.txt'
    elif genre == 'prose':
        path += '/prose/PROSE.txt'
    elif genre == 'gloss':
        path += '/glosses/GLOSSES.txt'
    elif genre == 'bible':
        path += '/bible/BIBLE.txt'
    else:
        path += '/poetry/POETRY.txt'

    got_a_sentence = False

    with open(path, 'r') as fp:
        all_text = fp.read()
        sentences = all_text.split('\n')

        def get_new_sentence():
            x = random.randrange(2, 9532)
            sentence = sentences[x]
            return sentence

        while got_a_sentence == False:

            sen = get_new_sentence()

            if re.search(r'(TEXT)', sen):
                sen = get_new_sentence()
            if re.search('_', sen):
                sen = get_new_sentence()
            if len(sen) < 15:
                sen = get_new_sentence()
                got_a_sentence = True

        sen = re.sub(r'\d', '', sen)
        sen = re.sub(r'\.', '', sen)
        sen = re.sub(r',', '', sen)
        sen = re.sub(r';', '', sen)
        sen = re.sub(r':', '', sen)
        sen = re.sub(r'\&', 'ond', sen)

        return sen

