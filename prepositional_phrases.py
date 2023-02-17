#! usr/bin/env python3
"""
Identifies prepositional phrases in a sentence.
All prepositional phrases (PP) are composed of PRP + NP
where NP is optional [DEM | ADJ | DEM ADJ] and N
"""

import regex as re
from termcolor import colored

import get_text

# _____________________________________________ declarations

text = get_text.random_sentence('poetry')     # gets a random sentence
# text = """x"""
words = text.split()
print(colored(text, 'blue'))
length = len(words)
print('\nNumber of words: ', length, '\n')

preps = ['abutan', 'abuten', 'abuton', 'æfter', 'æthindan',
         'amang', 'anforngean', 'begeonde', 'beheonan', 'beheonon',
         'behindan', 'behwon', 'beneoðan', 'betweoh', 'betweohs',
         'betwux', 'betweonan', 'betweonum', 'betweox', 'betweoxn',
         'betwih', 'betwisc', 'bewestan', 'binnan', 'butan', 'æt', 'for',
         'foranto', 'in', 'innan', 'into', 'mid', 'of', 'ofer', 'on',
         'onforan', 'oninnan', 'onmiddan', 'onufan', 'onuppan', 'uppon', 'uppan',
         'from', 'fram', 'to', 'toeacan', 'toforan', 'toforen', 'toforon', 'towiðere',
         'towiðre', 'ðurhut', 'þurh', 'ðurh', 'wið', 'wiðer', 'wiðforan',
         'wiðgeondan', 'wiðutan', 'ymb', 'ymbe', 'ymbutan'
         ]
pronouns_nominative = ['ic', 'we', 'ðu', 'þu', 'eow', 'he', 'seo', 'hit', 'hi']
datacc_pronouns = ['me', 'unc', 'us', 'þe', 'ðe', 'inc', 'eow', 'hine', 'him', 'hit', 'hie', 'hy',
                   'hyra', 'hiere', 'heo']
datacc_demonstratives = ['þisne', 'ðisne', 'þissum', 'ðissum', 'þis',
                         'ðis', 'þas', 'ðas', 'þisse', 'ðisse', 'þas', 'ðas', 'þæs', 'ðæs',
                         'þone', 'ðone', 'þæm', 'þam', 'ðæm', 'ðam', 'þæt', 'þat',
                         'ðæt', 'ðat', 'þa', 'ða', 'þære', 'þare', 'ðære', 'ðare']
pro_adjs = ['oðre', 'oþre', 'oðrum', 'oþrum', 'oðra', 'oþra', 'eall', 'eallum', 'ealle', 'ealla',
            'ealles', 'sum', 'sume', 'an', 'anne', 'anre']
conjunctions = ['ond', 'and', 'oððe', 'oþþe', 'ac']
noun_strong = re.compile(r'[^r]e$|as$|u$|[^r]a$|um$|æ$')
noun_weak = re.compile(r'an$')
adj_strong = re.compile(r'ne$|um$|e$|re$|ra$|u$|[^r]a$')
adj_weak = re.compile(r'e$|an$|um$')
genitives = ['min', 'minre', 'uncer', 'ure', 'his', 'hiere', 'þin', 'ðin', 'þinre', 'ðinre', 'incer', 'eower', 'hiera',
             'ðæs', 'þæs', 'ðære', 'þære', 'ðisses', 'þisses', 'ðisse', 'ðisse', 'ðara', 'þara', 'ðissa', 'þissa']
genitive_pattern = re.compile(r'es$')

# ________________________________________________ defs
# define likely objects, but double-check them in the if statements


def maybe_theobject(test):
    if test in datacc_pronouns:
        return True
    if test in pronouns_nominative:
        return False
    if re.search(noun_strong, test):
        return True
    if re.search(noun_weak, test):
        return True


def check_next(test2):
    if test2 in datacc_pronouns:
        return True
    if test2 in pronouns_nominative:
        return False
    if test2 in pro_adjs:
        return True
    if re.search(noun_strong, test2):
        return True
    if re.search(noun_weak, test2):
        return True
    if re.search(adj_strong, test2):
        return True
    if re.search(adj_weak, test2):
        return True


def check_genitive(test3):
    if test3 in genitives:
        return True
    if re.search(genitive_pattern, test3):
        return True


for index, word in enumerate(words):
    word = re.sub(r'\p{P}', '', word)   # clean out punctuation

    if word in preps:  # found preposition, let's do this thing
        print('\n', colored(word, 'red'), end=' ')
        this_pp = word

        # special cases

        if index == length:     # then PRP is the last word, so break
            break
        if index + 1 < length:    # check for idiomatic forþamþe
            if word == 'for' and re.search(r'(ð|þ)a(m|n)', words[index + 1]):
                print(colored(words[index + 1], 'red'), end=' ')
                if index + 2 < length:
                    if words[index + 2] == 'ðe' or words[index + 2] == 'þe':
                        print(colored(words[index + 2], 'red'), end=' ')
                continue
            if re.search(r'n(e|y|i)sse$', words[index +1]):  # check for words ending in -nysse
                print(colored(words[index + 1], 'red'), end=' ')
                continue
        if index + 2 < length:  # check for reflexive pronoun
            if re.search(r'selfe', words[index + 2]):
                print(colored(words[index + 2], 'red'), end=' ')

        # look right of the PRP

        if index + 1 < length:  # There is another word, so check PP-2nd word for POS

            if words[index + 1] in datacc_pronouns:  # a dat/acc pronoun always terminates a PP
                print(colored(words[index + 1], 'red'))
                continue

            if words[index + 1] in datacc_demonstratives:  # if PP-2nd is a demonstrative, check 3rd word etc
                print(colored(words[index + 1], 'yellow'), end=' ')
                if index + 2 < length:  # ensure there is a 3rd word
                    if maybe_theobject(words[index + 2]):
                        print(colored(words[index + 2], 'yellow'), end=' ')
                        if index + 3 < length and check_next(words[index + 3]):
                            print(colored(words[index + 3], 'yellow'), end=' ')
                        continue
                    elif check_next(words[index + 2]):
                        print(colored(words[index + 2], 'yellow'))
                        continue
                else:
                    continue

            if maybe_theobject(words[index + 1]):  # if 2nd word is the object of the preposition, check 3rd
                print(colored(words[index + 1], 'cyan'), end=' ')
                if index + 2 < length and check_next(words[index + 2]):
                    print(colored(words[index + 2], 'cyan'))
                    continue
                continue

            if check_next(words[index + 1]):  # if 2nd word is not object, but something else, check 3rd
                print(colored(words[index + 1], 'magenta'), end=' ')
                if index + 2 < length and check_next(words[index + 2]):
                    print(colored(words[index + 2], 'magenta'))
                    continue
                continue

            if check_genitive(words[index + 1]):   # if 2nd word genitive
                print(colored(words[index + 1], 'green'), end=' ')
                if index + 2 < length and check_next(words[index + 2]):
                    print(colored(words[index + 2], 'green'))
                    continue

            if re.search(adj_weak, words[index + 1]):   # if 2nd word weak adj, see if PP-3rd word is too
                print(colored(words[index + 1], 'green'), end=' ')
                if index + 2 < length and re.search(adj_weak, words[index + 2]):
                    print(colored(words[index + 2], 'green'))
                    continue

            if index + 1 < length:      # if all else fails, the 2nd word is likely the object
                print(colored(words[index + 1], 'grey'), end=' ')


# TODO: Make this into a callable module
