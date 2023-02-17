#! usr/bin/env python3

"""
Splits corpus words into lists, removes duplicates
"""

from collections import OrderedDict

with open('poetryWordUniq.txt', 'r') as fp:
    allText = fp.read()
    allWords = allText.split()
    words = sorted(allWords)
    uniques = list(OrderedDict.fromkeys(words))

# print(uniques)

fp2 = open('glossWords.txt', 'w+')
print(uniques, file=fp2)
fp2.close()
