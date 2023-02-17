#! usr/bin/env python3

"""
Finds titles and bibliographic info in ASPR glosses
"""

import re
from termcolor import colored, cprint

def clean(dirty):
    ready = re.sub(r"START_TEXT", "", dirty)
    ready = ready.lower()
    return ready

i = 1
text = { 
    'short_title': 'none',
    'bib': 'none'
}

pattern1 = re.compile(r"START_TEXT")
pattern2 = re.compile(r"END_TEXT")

with open('glosses_clean.txt', 'r') as fp:
    the_whole_text = fp.read()
    lines = the_whole_text.split('\n')

    for index, thisLine in enumerate(lines):
        if pattern1.findall(thisLine):		# finds the start of a text
            start = index
            if start < len(lines):
                print(i, ' ', end = '')
                short_title = lines[index+1]
                bib = lines[index+2]
                print(colored(short_title, 'magenta', attrs=['underline']), "\t", bib,)
                i = i + 1

#        if pattern2.findall(thisLine):		# finds the end of a text
#            end = index
#            start = start + 3        # start after bib info
#            for x in lines[start:end]:
#                new = clean(x)

#    print('{number} {title}. Ed. {editor}\n'.format(**poems))
# cprint(flag+1, 'red', attrs=['bold'])

# TODO:
#
# make this into part of a class to call up titles and text numbers
