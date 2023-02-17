#! usr/bin/env python3

"""
finds nouns by finding dative plurals, then producing root forms
"""

fp = open('poetryWords.txt', 'r')
words = fp.readlines()
words = [w.strip() for w in words]
fp.close()

fw = open('nouns.txt', 'w+')

fw.writelines([w[:-2]+'\n' for w in words if w.endswith('um')])
fw.close()
