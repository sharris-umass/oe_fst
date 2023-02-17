#! usr/bin/env python3
"""
Searches the corpus for prepositional phrases and stores them
"""

import regex as re
from termcolor import colored


class PrepositionalPhrase:

    def __init__(self, sentence):
        self.sentence = sentence

        preps = ['abutan', 'abuten', 'abuton', 'æfter', 'æthindan',
                 'amang', 'anforngean', 'begeonde', 'beheonan', 'beheonon',
                 'behindan', 'behwon', 'beneoðan', 'betweoh', 'betweohs',
                 'betwux', 'betweonan', 'betweonum', 'betweox', 'betweoxn',
                 'betwih', 'betwisc', 'bewestan', 'binnan', 'butan', 'æt',
                 'foranto', 'in', 'innan', 'into', 'mid', 'of', 'ofer', 'on',
                 'onforan', 'oninnan', 'onmiddan', 'onufan', 'onuppan', 'uppon', 'uppan',
                 'from', 'fram', 'to', 'toeacan', 'toforan', 'toforen', 'toforon', 'towiðere',
                 'towiðre', 'ðurhut', 'þurh', 'ðurh', 'wið', 'wiðer', 'wiðforan',
                 'wiðgeondan', 'wiðutan', 'ymbe', 'ymbutan'
                 ]

        datacc_pronouns = ['me', 'unc', 'us', 'þe', 'ðe', 'inc', 'eow', 'hine', 'him', 'hit', 'hie', 'hiere', 'heo']
        datacc_demonstratives = ['þisne', 'ðisne', 'þissum', 'ðissum', 'þis',
                                 'ðis', 'þas', 'ðas', 'þisse', 'ðisse', 'þas', 'ðas',
                                 'þone', 'ðone', 'þæm', 'þam', 'ðæm', 'ðam', 'þæt', 'þat',
                                 'ðæt', 'ðat', 'þa', 'ða', 'þære', 'þare', 'ðære', 'ðare']
        conjunctions = ['ond', 'and', 'oððe', 'oþþe', 'ac']
        noun_strong = re.compile(r'[^r]e$|as$|u$|[^r]a$|um$|[bcdfghlmnprstw]$')
        noun_weak = re.compile(r'e$|an$|um$')
        adj_strong = re.compile(r'ne$|um$|e$|re$|ra$|u$|[^r]a$')
        adj_weak = re.compile(r'e$|an$|um$')
        genitives = ['min', 'uncer', 'ure', 'his', 'hiere', 'þin', 'ðin', 'þinre', 'ðinre', 'incer', 'eower', 'hiera',
                     'ðæs',
                     'þæs', 'ðære', 'þære', 'ðisses', 'þisses', 'ðisse', 'ðisse', 'ðara', 'þara', 'ðissa', 'þissa']
        genitive_pattern = re.compile(r'es$')

        def maybesecondword(self, test2):
            if test2 in datacc_demonstratives:
                return True
            if test2 in adj_strong:
                return True
            if test2 in adj_weak:
                return True
            if test2 in genitives:
                return True
            if test2 in genitive_pattern:
                return True

        def isitanobject(self, test):
            if test in datacc_pronouns:
                return True
            if test in noun_strong:
                return True


        right_edge = False
        words = sentence.split()
        length = len(words)

        for index, word in enumerate(words):
            word = re.sub(r'\p{P}', '', word)

            if word in preps:  # found preposition
                print('\n', colored(word, 'red'), end=' ')
                this_pp = word

                if index + 1 == length:     # then PRP is the last word
                    break

                if index + 1 < length:  # We're OK, so check 2nd word for POS
                    # print(words[index+1], end=' ')

                    if words[index + 1] in datacc_pronouns:  # stop if 2nd word is dat or acc prn
                        print(colored(words[index + 1], 'red'), end=' ')
                        continue

                    if index + 2 < length:  # if 2nd word is another PRP, then combine with first PRP
                        if words[index + 2] in preps:
                            print(colored(words[index + 1], 'red'), end='')
                            print(colored(words[index + 2], 'red'))
                            if index + 3 < length:
                                pass
                            continue

                    if index + 2 < length:  # if a CNJ, check 4th
                        if words[index + 2] in conjunctions:
                            if re.search(noun_strong, words[index + 2]):      # check if following word is d/a noun
                                print(colored(words[index + 1], 'red'), end=' ')  # print the CNJ
                                print(colored(words[index + 2], 'red'), end=' ')
                            continue

                    if words[index + 1] in datacc_demonstratives:  # if next is article, check 3rd word
                        print(colored(words[index + 1], 'yellow'), end=' ')
                        if index + 2 < length:  # ensure there is a 3rd word
                            if re.search(noun_strong, words[index + 2]):
                                right_edge = True
                                print(colored(words[index + 2], 'yellow'))
                                continue
                            elif re.search(noun_weak, words[index + 2]):
                                right_edge = True
                                print(colored(words[index + 2], 'yellow'))
                                continue
                        else:
                            continue

                    if re.search(adj_weak, words[index + 1]):  # if next is wk adj, check 3rd for N
                        print(colored(words[index + 1], 'green'), end=' ')
                        if index + 2 < length:  # ensure there is a 3rd word
                            if re.search(noun_weak, words[index + 2]):
                                print(colored(words[index + 2], 'green'))
                                right_edge = True
                                continue
                            else:
                                right_edge = True
                                continue
                        else:
                            continue

                    if re.search(adj_strong, words[index + 1]):  # if next is str adj, check 3rd for str N
                        print(colored(words[index + 1], 'yellow'), end=' ')
                        if index + 2 < length:  # ensure there is a 3rd word
                            if re.findall(noun_strong, words[index + 2]):
                                print(colored(words[index + 2], 'yellow'))
                                right_edge = True
                                continue
                            else:
                                right_edge = True
                                continue

                    if words[index + 1] in genitives:  # if next is genitive, check 3rd for N
                        print(colored(words[index + 1], 'magenta'), end=' ')
                        if index + 2 < length:  # ensure there is a 3rd word
                            if re.search(noun_strong, words[index + 2]):
                                print(colored(words[index + 2], 'magenta'))
                                right_edge = True
                                continue
                            elif re.search(noun_weak, words[index + 2]):
                                print(colored(words[index + 2], 'magenta'))
                                right_edge = True
                                continue
                    elif re.search(genitive_pattern, words[index + 1]):
                        print(colored(words[index + 1], 'magenta'), end=' ')
                        if index + 2 < length:
                            print(colored(words[index + 2], 'magenta'))
                            continue

                    elif re.search(r'[^e$|um$|an$|ne$|as$|a$]', words[index+1]):  # if next not inflected, check 3rd
                        print(colored(words[index + 1], 'magenta'), end=' ')
                        if index + 2 < length:  # ensure there is a 3rd word
                            if re.search(noun_strong, words[index + 2]):
                                print(colored(words[index + 2], 'magenta'))
                                continue

# TODO: add support for conjunctions (ond, oþþe, ac, etc.)
