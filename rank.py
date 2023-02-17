#! usr/bin/env python3
"""
Takes the parts of speech generated for a word and RETURNs a ranking
"""

import re
import flatten

def rank(pos_list):

    value = 0

    pos_list = flatten.flatten(pos_list)        # turns the list into a string

    most_likely = ''
    less_likely = []

    for item in pos_list:

        item_string = str(item)
        item_string = item_string.upper()

        # ___________________________________ Sure Things

        if re.search('5', item_string):
            value = 5
            most_likely = item_string
            break

        if 'PRP' in item_string:
            value = 5
            most_likely = item_string

        if 'NUM' in item_string:
            value = 5
            most_likely = item_string

        if 'CNJ' in item_string:
            value = 5
            most_likely = item_string

        if 'PRN' in item_string:
            value = 5
            most_likely = item_string

        if 'pron' in item_string:
            value = 5
            most_likely = item_string

        # ___________________________________ Likely Things

        if value < 5:

            if re.search('4', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('N (m|f|n)', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('N (M|F|N)', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('m|n|f', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('ppl|PPL', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('V wk', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('wk', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('str', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('irr', item_string):
                value = 4
                less_likely.append(item_string)

            if re.search('3', item_string) and not re.search('4', item_string):
                value = 3
                less_likely.append(item_string)

        # ________________________________________ Possible

        # send to syntax.py to get nearby words






    likely = (most_likely, less_likely)

    return value, likely

# TODO: return best guess in first element, then all other guesses, ranked, in second element
# these ranks are had by COntrol, and written up in "start_here.py"
