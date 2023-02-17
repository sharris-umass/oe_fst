#! usr/bin/env python3

"""
Finds titles and bibliographic info in ASPR
"""

import re
from termcolor import colored, cprint

def clean(dirty):
    ready = re.sub(r"START_TEXT", "", dirty)
    ready = ready.lower()
    return ready

#def collect(poem):
    whole_poem = [''.join(x) for x in words]
    ready = re.sub(r"\n", "\s", whole_poem)
    steady = ready.split()
    return steady

i = 1
poems = { 
    'number': 0,
    'title': 'none',
    'editor': 'none'
}
words = []

pattern1 = re.compile(r"START_TEXT")
pattern2 = re.compile(r"END_TEXT")

with open('POETRY.txt') as fp:
    text = fp.read()
    lines = text.split('\n')

    for index, thisLine in enumerate(lines):
        if pattern1.findall(thisLine):		# finds the start of a poem
            start = index
            if start < len(lines):
                print(i, ' ', end = '')
                title = lines[index+2]
                ed = lines[index+3]
#                poems['number'] = i
#                poems['title'] = title
#                poems['editor'] = ed
                print(colored(title, 'magenta', attrs=['underline']), "Ed.", ed,)
                i = i + 1
        if pattern2.findall(thisLine):		# finds the end of a poem
            end = index
            start = start + 4        # start after bib info
            for x in lines[start:end]:
                new = clean(x)
                words.append(new)
#                print(words)
                words.clear()

#    print('{number} {title}. Ed. {editor}\n'.format(**poems))
# cprint(flag+1, 'red', attrs=['bold'])

# TODO:
#
# put number, title, poem into a library or library of tuples
#
# make this into part of a class to call up titles and text numbers
