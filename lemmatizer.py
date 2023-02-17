#! usr/bin/env python3

"""
Takes an unidentified word and isolates a likely inflectionsal category,
then generates a lemma based on that inflection.

sælig -> finds -ig and guesses ADJ -> returns sælig since dictionaries lemmatize adj's
singeð -> finds -eð and guesses verb -> returns infinitive form singan
stanum -> finds -um and guesses noun -> returns stan
"""

import os
import regex as re

import control_module

# test input
testword = input("Input word: ")


def parse(wordtoparse):
    """Takes a string, then looks for suffixes by dropping from the most unusual to usual; returns 2 strings"""

    pos = ''
    possible_root = ''
    got_it = False

    while got_it is False:
        # the most obvious endings first

        adj = re.compile(r'(.*)ig$')
        adj_stem = re.search(adj, wordtoparse)
        if adj_stem:
            pos = 'adj'
            possible_root = adj_stem.group()  # dictionaries lemmatize -ig adjectives with -ig
            got_it = True
            continue

        adj2 = re.compile(r'(.*)(ra$|re$|ost$|ene$)')  # comparative, superlative, accusative
        adj2_stem = re.search(adj2, wordtoparse)
        if adj2_stem:
            pos = 'adj'
            possible_root = adj2_stem.group(1)
            got_it = True
            continue

        # verb infinitives look just like weak noun oblique cases: -an
        # so deal with them before firing this method
        # very difficult to distinguish strong from weak verbs, esp. strng verbs with ð in their root

        verb = re.compile(r'(.*)(e[ðþ]$|en[nd]e$|[ia[ðþ]$)') # subjunctives
        verb_stem = re.search(verb, wordtoparse)
        if verb_stem:
            pos = 'verb'
            possible_root = verb_stem.group(1)
            got_it = True
            continue

        verb2 = re.compile(r'(.*)(a[ðþ]$|[ae]st$|ode$|odon$)')  # indicatives
        verb_stem2 = re.search(verb2, wordtoparse)
        if verb_stem2:
            pos = 'verb'
            possible_root = verb_stem2.group(1)
            got_it = True
            continue

        noun = re.compile(r'(.*)(n[ye]sse$|sc[iy]pe$)')  # abstract feminine nouns
        noun_stem = re.search(noun, wordtoparse)
        if noun_stem:
            pos = 'noun'
            possible_root = noun_stem.group(1)
            got_it = True
            continue

        noun2 = re.compile(r'(.*)([ae]s$|[bcdfghlmnprstvw]a$|um$|ena$|u$)')  # strong nouns
        # if it is a noun stem that ends in a vowel, it will be a lemma and this method won't fire
        noun_stem2 = re.search(noun2, wordtoparse)
        if noun_stem2:
            pos = 'noun'
            possible_root = noun_stem2.group(1)
            got_it = True
            continue

        # weak noun endings are too common to isolate, make_root() takes care of them

        adv = re.compile(r'(.*)(lic$|lice$)')
        adv_stem = re.search(adv, wordtoparse)
        if adv_stem:
            pos = 'adv'
            possible_root = adv_stem.group(1)
            got_it = True
            continue

    return pos, possible_root


def get_root_shape(guess):
    rootshape = ''
    print(guess)

    # variables for defining the phonemic shape of an Old English root, e.g. CVC, CVCC
    v = {'æ', 'a', 'e', 'i', 'o', 'u', 'y'}  # use set notation and check for membership
    c = {'b', 'c', 'd', 'f', 'g', 'h', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'z', 'ð', 'þ'}
    convert = {'k': 'c', 'j': 'i', 'q': 'c'}

    for letter in guess:
        letter = letter.rstrip()
        if letter in convert:
            letter = convert[letter]
        if letter in v:
            rootshape += 'V'
        if letter in c:
            rootshape += 'C'
        if letter is None:
            continue

    print(rootshape)

    return 0


def make_root(word='', pos='', poss_root=''):
    """takes a word, its part of speech, and its possible root and de-inflects it accordingly"""
    root = poss_root
    root_shape = get_root_shape(root)

    if pos == 'noun' or pos == 'adj':
        print('De-inflecting {} as {}'.format(word, poss_root))
        if re.search(r'C$', root_shape):  # we have a consonant stem
            print('Consonant stem: {}'.format(root_shape))
        if re.search(r'V$', root_shape):  # we have a vowel stem
            print('Vowel stem: {}'.format(root_shape))

    if pos == 'verb':
        print('Got a verb')
        if len(word) > 4:
            if re.search(r'^ge', word) and re.search(r'ian$', word):
                root = word[2:-3]
                print('\nPossible root: {}'.format(root))
                test = get_root_shape(root)
                print(test)
            elif re.search(r'^ge', word) and re.search(r'an$', word):
                root = word[2:-2]
                print('\nPossible root: {}'.format(root))
        # strong verbs: use 7 ablaut series and substitute infinitive vowel

    if pos == 'adv':
        print('Got an adverb')

    return root


def check_wordlists(dirpath, lemma):
    with open(dirpath) as wl:
        allwords = wl.read().split()    # get all the words that start with the same letter
        if lemma in allwords:
            return True
        else:
            return False


def check_for_runes(possible_rune):
    if possible_rune.lower() == 'þ':
        return 'th'
    if possible_rune.lower() == 'ð':
        return 'th'
    if possible_rune.lower() == 'æ':
        return 'ae'
    else:
        return possible_rune


def lemmatize(word):
    """The main function: takes a word, finds its p.o.s. & root, makes lemma, then searches wordlists for lemma"""

    thisword = word.lower()
    is_a_lemma = False

    path = os.getcwd()

    # get the correct file to search, based on the first letter of the word, so 'cwen' -> c.txt
    first_letter = re.findall(r'^\w', thisword)
    path_letter = first_letter[0]

    # check for runic letters and transform them into English ones, otherwise leave it alone
    path_letter = check_for_runes(path_letter)

    modified_path = path + '/wordlists/{}.txt'.format(path_letter)
    print('\nChecking file: {}'.format(modified_path))

    # now check the correct word list for the lemma
    is_a_lemma = check_wordlists(modified_path, thisword)

    # if thisword is not in the wordlists, then check other possibiities
    if not is_a_lemma:
        # maybe thisword starts with a verbal prefix ge-
        ge_prefix = re.findall(r'^ge.*', thisword)
        if ge_prefix:
            newpath = path + '/wordlists/{}.txt'.format(thisword[2])  # index starts at 0!
            is_a_lemma = check_wordlists(newpath, thisword)
            if not is_a_lemma:
                print('Not found in file {}.'.format(newpath))
            else:
                # it might be an infinitive or an inflected preterite
                if ge_prefix and re.findall(r'an$', thisword):   # infinitive?
                    pass
                return True

        print('\nManufacturing lemma.')
        thisword_pos, thisword_possibleroot = parse(word)

        print('Checking parser ...')
        parser = control_module.process_items_serially(thisword, thisword_pos)
        print(parser)
        lemma = make_root(thisword, thisword_pos, thisword_possibleroot)
        if lemma == thisword:
            return True

    return is_a_lemma


answer = lemmatize(testword)
if answer:
    print('Yes, that is a lemma')
else:
    print('Not a lemma')

