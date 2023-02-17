#! usr/bin/env python3
"""
Matches inflectional morphology of term, returning all guesses with likelihoods
"""

import re


def scan(term):
    morphology = []
    if re.match(r'.{2,15}um$', term):
        morphology.append('ADJ S M DAT PL 4')
        morphology.append('ADJ S N DAT PL 4')
        morphology.append('ADJ S F DAT PL 4')
        morphology.append('ADJ W M DAT PL 4')
        morphology.append('ADJ W N DAT PL 4')
        morphology.append('ADJ W F DAT PL 4')
        morphology.append('ADJ S M DAT S 2')
        morphology.append('ADJ S N DAT S 2')
    if re.match(r'.{2,15}ra$', term):
        morphology.append('ADJ CMP 3')
        morphology.append('ADJ S M GEN PL 3')
        morphology.append('ADJ S N GEN PL 3')
        morphology.append('ADJ S F GEN PL 3')
        morphology.append('ADJ W M GEN PL 3')
        morphology.append('ADJ W N GEN PL 3')
        morphology.append('ADJ W F GEN PL 3')
    if re.match(r'ena$', term):
        morphology.append('ADJ W M GEN PL 4')
        morphology.append('ADJ W N GEN PL 4')
        morphology.append('ADJ W F GEN PL 4')
    if re.match(r'.{1,15}ne$', term):
        morphology.append('ADJ S M ACC S') 
    if re.match(r'es$', term):
        morphology.append('ADJ S M GEN S 4')
        morphology.append('ADJ S N GEN S 4')
    if re.match(r'.{2,15}u$', term):
        morphology.append('ADJ S F NOM S 3')
        morphology.append('ADJ S N NOM PL 3')
        morphology.append('ADJ S N ACC PL 3')
    if re.match(r'.{2,15}re$', term):
        morphology.append('ADJ S F GEN S 4')
        morphology.append('ADJ S F DAT S 4')
        morphology.append('ADJ S F INS S 4')
    if re.match(r'.[bcdfghlmpstw]e$', term):
        morphology.append('ADJ S M NOM PL 3')
        morphology.append('ADJ S M ACC PL 3')
        morphology.append('ADJ S F ACC S 3')
        morphology.append('ADJ S M INS S 3')
        morphology.append('ADJ S N INS S 3')
        morphology.append('ADJ S F NOM PL 3')
        morphology.append('ADJ S F ACC PL 3')
    if re.match(r'.[bcdfghlmpstw]a$', term):
        morphology.append('ADJ W M NOM S 3') 
    if re.match(r'.{2,15}an$', term):
        morphology.append('ADJ W M ACC S 2')
        morphology.append('ADJ W M GEN S 2')
        morphology.append('ADJ W M DAT S 2')
        morphology.append('ADJ W M INS S 2')
        morphology.append('ADJ W M NOM PL 2')
        morphology.append('ADJ W M ACC PL 2')
        morphology.append('ADJ W F ACC S 2')
        morphology.append('ADJ W F GEN S 2')
        morphology.append('ADJ W F DAT S 2')
        morphology.append('ADJ W F INS S 2')
        morphology.append('ADJ W F NOM PL 2')
        morphology.append('ADJ W F ACCPL 2')
        morphology.append('ADJ W N GEN S 2')
        morphology.append('ADJ W N DAT S 2')
        morphology.append('ADJ W N INS S 2')
        morphology.append('ADJ W N NOM PL 2')
        morphology.append('ADJ W N ACC PL 2')
    if re.match(r'[bcdfghlmnprstw]$', term):
        morphology.append('ADJ S M NOM S 2')
        morphology.append('ADJ S N NOM S 2')
        morphology.append('ADJ S N ACC S 2')
    if re.match(r'ræden$', term):
        morphology.append('N W F NOM S 3')
    if re.match(r'um$', term):
        morphology.append('N S M DAT PL 4')
        morphology.append('N S N DAT PL 4')
        morphology.append('N S F DAT PL 4')
        morphology.append('N W M DAT PL 4')
        morphology.append('N W N DAT PL 4')
        morphology.append('N W F DAT PL 4')
    if re.match(r'ena$', term):
        morphology.append('N W M GEN PL 4')
        morphology.append('N W N GEN PL 4')
        morphology.append('N W F GEN PL 4')
        morphology.append('N S F GEN PL 4')
    if re.match(r'.{1,15}es$', term):
        morphology.append('N S M GEN S 4')
        morphology.append('N S N GEN S 4')
    if re.match(r'.{1,15}as$', term):
        morphology.append('N S M NOM PL 4')
        morphology.append('N S M ACC PL 4')
    if re.match(r'.{2,15}u$', term):
        morphology.append('N S F NOM S 4')
        morphology.append('N S N NOM PL 4')
        morphology.append('N S N ACC PL 4')
    if re.match(r'.(b|c|d|ð|f|g|h|l|m|n|p|s|t|þ|w|x)e$', term):
        morphology.append('N S M DAT S 2')
        morphology.append('N S N DAT S 2')
        morphology.append('N S F DAT S 2')
        morphology.append('N S F ACC S 2')
        morphology.append('N S F GEN S 2')
        morphology.append('N S F NOM PL 2')
        morphology.append('N S F ACC PL 2')
        morphology.append('N W F NOM S 2')
        morphology.append('N W N NOM S 2')
        morphology.append('N W N ACC S 2')
    if re.match(r'.(b|c|d|ð|f|g|h|l|m|n|p|s|t|þ|w|x)a$', term):
        morphology.append('N S M GEN PL 2')
        morphology.append('N S N GEN PL 2')
        morphology.append('N S F NOM PL 2')
        morphology.append('N S F ACC PL 2')
        morphology.append('N S F GEN PL 2')
        morphology.append('N W M NOM S 2')
    if re.match(r'.(b|c|d|ð|f|g|h|l|m|n|p|r|s|t|þ|w|x)an$', term):
        morphology.append('N W M ACC S 2')
        morphology.append('N W M GEN S 2')
        morphology.append('N W M DAT S 2')
        morphology.append('N W M NOM PL 2')
        morphology.append('N W M ACC PL 2')
        morphology.append('N W F ACC S 2')
        morphology.append('N W F GEN S 2')
        morphology.append('N W F DAT S 2')
        morphology.append('N W F NOM PL 2')
        morphology.append('N W F ACC PL 2')
        morphology.append('N W N GEN S 2')
        morphology.append('N W N DAT S 2')
        morphology.append('N W N NOM PL 2')
        morphology.append('N W N ACC PL 2')
    if re.match(r'.(b|c|d|ð|f|g|h|l|m|n|p|r|s|t|þ|w|x)$', term):
        morphology.append('N S M NOM S 2')
        morphology.append('N S M ACC S 2')
        morphology.append('N S N NOM S 2')
        morphology.append('N S N ACC S 2')
        morphology.append('N S N NOM PL 2')
        morphology.append('N S N ACC PL 2')
    if re.match(r'st$', term):
        morphology.append('V 2 S PRES IND 3:')
    if re.match(r'ende$', term):
        morphology.append('V PPL PRES 5')
    if re.match(r'enne$', term):
        morphology.append('V GER PRES 5')
    if re.match(r'a[ð|þ]$', term):
        morphology.append('V 1 P PRES IND 3')
        morphology.append('V 2 P PRES IND 3')
        morphology.append('V 3 P PRES IND 3')
        morphology.append('V IMP P 3')
    if re.match(r'e[ð|þ]$', term):
        morphology.append('V 3 S PRES IND 4')
    if re.match(r'ede$', term):
        morphology.append('V 1 S PRES IND 4')
        morphology.append('V 3 S PRES IND 4')
        morphology.append('V 1 S PRES SBJ 3')
        morphology.append('V 2 S PRES SBJ 3')
        morphology.append('V 3 S PRES SBJ 3')
    if re.match(r'ode$', term):
        morphology.append('V 1 S PRT IND 4')
        morphology.append('V 3 S PRT IND 4')
        morphology.append('V 1 S PRT SBJ 2')
        morphology.append('V 2 S PRT SBJ 2')
        morphology.append('V 3 S PRT SBJ 2')  
    if re.match(r'.{2,15}e$', term):
        morphology.append('V 1 S PRES IND 2')
        morphology.append('V 1 S PRES SBJ 2')
        morphology.append('V 2 S PRES SBJ 2')
        morphology.append('V 3 S PRES SBJ 2')
        morphology.append('V 1 S PRT SBJ 2')
        morphology.append('V 2 S PRT SBJ 2')
        morphology.append('V 3 S PRT SBJ 2')
        morphology.append('V 1 S IMP 2')
        morphology.append('V 2 S IMP 2')
        morphology.append('V 3 S IMP 2')
    if re.match(r'.{2,15}a$', term):
        morphology.append('V 1 S IMP 1')
        morphology.append('V 2 S IMP 1')
        morphology.append('V 3 S IMP 1')
    if re.match(r'en$', term):
        morphology.append('V 1 P PRES SBJ 3')
        morphology.append('V 2 P PRES SBJ 3')
        morphology.append('V 3 P PRES SBJ 3')
        morphology.append('V 1 P PRT SBJ 3')
        morphology.append('V 2 P PRT SBJ 3')
        morphology.append('V 3 P PRT SBJ 3')
    if re.match(r'.*on$', term):
        morphology.append('V 1 P PRT IND 4')
        morphology.append('V 2 P PRT IND 4')
        morphology.append('V 3 P PRT IND 4')

    return morphology
