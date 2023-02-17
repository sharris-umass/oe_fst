#! usr/bin/env python3

"""
Cleans DOE poetry corpus intolist of words
"""

import re
from termcolor import colored

poem = input("""Poem to search: \n[1] Beowulf [2] Judith [3] Genesis [4] Exodus 
[5] Daniel [6] Andreas [7] Christ & Satan """)

seek = input('Word to find: ')

if poem == '1':
    my_file = 'beowulf.txt'
if poem == '2':
    my_file = 'judith.txt'
if poem == '3':
    my_file = 'genesis.txt'
if poem == '4':
    my_file = 'exodus.txt'
if poem == '5':
    my_file = 'daniel.txt'
if poem == '6':
    my_file = 'andreas.txt'
if poem == '7':
    my_file = 'christandsatan.txt'

with open(my_file, 'r') as fh:
    text = fh.read()
    text = text.lower()

    words = text.split()

    bigrams = [seek,]

    for index, word in enumerate(words):
        if word == seek:
            if index == len(words):
                print(index, colored(word, 'red'),' is the last word')
            elif index < len(words)-1:
                print(index, colored(word, 'red'),
                colored(words[index+1], 'red'))
                bigrams.append(words[index+1])


print("_____________________\n\nInstances of {0}: {1}".format(seek, len(bigrams)))
print(bigrams)

# _____________NOTES
# 
#    instances = re.findall(r"\b{0}\b".format(word), words)


