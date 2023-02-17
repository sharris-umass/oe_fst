#! usr/bin/env python3

"""
Splits corpus wrods into lists, removes duplicates
"""

from collections import OrderedDict

with open('prose_words.txt', 'r') as fp:
    allText = fp.read()
    allWords = allText.split()
    words = sorted(allWords)
    uniques = list(OrderedDict.fromkeys(words))

# print(uniques)

fp2 = open('proseWordsUniq.txt', 'w+')
print(uniques, file=fp2)
fp2.close()
