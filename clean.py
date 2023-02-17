#! usr/bin/env python3

"""
Cleans up a sentence, returns string
"""
import regex as re


def cleanit(sentence):
    """
    Removes digits and punctuation, then lowercases it
    :return: string
    """
    newsentence = sentence
    newsentence = newsentence.lstrip()
    newsentence = re.sub(r'\d+', '', newsentence)
    newsentence = ''.join(ch for ch in newsentence if ch not in [',', ';', '.', '?', '"', ':', '/'])
    newsentence = newsentence.lower()

    return newsentence


def regularize(wordclasses):
    """
    Cleans up and regularizes the lists of parts-of-speech
    :param wordclasses: list
    :return: cleaned-up list
    """
    newclasses = []

    for guess in wordclasses:
        # if it's ok, ignore it
        rules = [guess == 'PRN',
                 guess == 'ADV',
                 guess == 'CNJ',
                 guess == 'VERB',
                 guess == 'NOUN',
                 guess == 'ADJ',
                 guess == 'PRP',
                 guess == 'INT',
                 guess == 'NUM']
        if any(rules):
            newclasses.append(guess)

        # take the first four letter
        # if len(guess) > 3:
        #     guess = guess[0:3]

        if re.findall('[0-9]', guess):
            newclasses.append(re.sub('[0-9]', '', guess))
        if re.findall(r'[a-z]', guess):
            newclasses.append(re.sub(r'[a-z]', '', guess))
        # if re.findall(r'  ', guess):
        #     newclasses.append(re.sub(r'  ', ' ', guess))

        # special cases:
        if re.findall(r'(.{1,4})\s.*', guess):
            newclasses.append(re.sub(r'(.{1,4})\s.*', r'\1', guess))
        if re.findall(r'VERB.*', guess):
            newclasses.append(re.sub(r'VERB.*', 'VERB', guess))

    # get rid of empty elements
    newclasses = list(filter(None, newclasses))

    # reduce to a set
    newclasses = set(newclasses)
    # restore to a list
    newclasses = list(newclasses)

    return newclasses
