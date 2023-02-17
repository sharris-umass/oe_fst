#! usr/bin/env python3

"""
Calls control_module.py, which controls the entire FST.

:Return: a sentence that has been tagged for part of speech word-by-word.
"""

import control_module
from termcolor import colored
from prepositional_phrases_callable import PrepositionalPhrase
# import flatten


def go(sentence):
    # call the control module to process the words of the sentence
    result = control_module.work_on_words(sentence)

    # result is the memory address of a zip object, so turn it into a list
    temporary = list(result)

    for item in temporary:
        # item is a tuple
        # sometimes there are no values in item[1], so use TRY/EXCEPT
        word = item[0]
        try:
            pos1, pos2 = item[1]   # best guess is first element and next best guesses are second
        except ValueError:
            pos1, pos2 = '', ''

        # if we have a sure thing, it's a string
        # if we have a guess, it's a list
        print(colored(word, color='blue', attrs=['bold']), '\t', end='')

        if type(pos1) is str:
            print(colored(pos1, color='red'), '\t', end='')
            # if it's not a string, then it's a guess. Print it as well.
        print(pos2)


if __name__ == '__main__':
    # get a random sentence and send it to go()
    my_sentence = control_module.get_a_sentence('poetry')   # poetry, prose, gloss, bible
    print('\nSentence:', my_sentence, '\n')
    go(my_sentence)

    # check the sentence for prepositional phrases, which prints them in strings
    print(colored('\nPrepositional Phrases:', color='yellow'))
    PrepositionalPhrase(my_sentence)
