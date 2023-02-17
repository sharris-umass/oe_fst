#! usr/bin/env python3

"""
Takes an unidentified word and isolates likely inflections, then RETURNs possible POS.
Duplicated in morphology.py
"""


def open_classGuess(word):

    import re

    pos = []

    verb = re.compile(r'(.*)(eð$|eþ$|ie$|enne$|ende$|iaþ$|iað$|ian$|ean$|aþ$|að$|st$|ode$|odon$)')
    verb_stem = re.search(verb, word)

    verb3 = re.compile(r'(.*)(est$|on$|en$|t$|ð$|þ$|an$|ed$)')
    verb3_stem = re.search(verb3, word)

    noun = re.compile(r'(.*)(es$|as$|um$|ena$|u$|nysse$|nesse$|scipe$|scype$)')
    noun_stem = re.search(noun, word)

    noun3 = re.compile(r'(.*)(e$|a$|an$)')
    noun3_stem = re.search(noun3, word)

    adj4 = re.compile(r'(.*)(ra$|re$|ost$|ene$)')
    adj4_stem = re.search(adj4, word)

    adj3 = re.compile(r'(.*)(ne$|e$|res$|a$|as$|um$|ena$|u$|an$|a$)')
    adj3_stem = re.search(adj3, word)

    adv = re.compile(r'(.*)(lic$)')
    adv_stem = re.search(adv, word)

    if noun_stem:
        pos.append("NOUN 4")
    if noun3_stem:
        pos.append("NOUN 3")
    if re.search(r'ig$', word, re.I):
        pos.append("ADJ 5")
    if adj4_stem:
        pos.append("ADJ 4")
    if adj3_stem:
        pos.append("ADJ 3")
    if verb_stem:
        pos.append("VERB 4")
    if verb3_stem:
        pos.append("VERB 3")
    if adv_stem:
        pos.append("ADV 5")

    return pos
