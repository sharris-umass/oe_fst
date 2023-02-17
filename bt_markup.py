#! usr/bin/env python3

"""
Takes a word from control.py, searches a LINE from data_bt_edited.txt
marks up a word with grammatical information from Bosworth Toller (data_bt_edited.txt)
"""

def info(line):

    markup = []
    entry = line.split(':')

    if len(entry) < 4:
        return None
    if entry[2] == '1':
        markup.append('NOUN')
    elif entry[7] == '1':
        markup.append('PRN')
    elif entry[8] == '1':
        markup.append('ADJ')
    elif entry[9] == '1':
        markup.append('VERB')
    elif entry[17] == '1':
        markup.append('ADV')                          
    elif entry[18] == '1':
        markup.append('PRP')
    elif entry[19] == '1':
        markup.append('CNJ')
    if entry[20] == '1':
        markup.append('INT')
    if entry[21] == '1':
        markup.append('NUM')
    if entry[22] == '1':
        markup.append('PREF')
    elif entry[23] == '1':
        markup.append('SUFF')

    if entry[2] == '1':
        if entry[3] == '1':
            markup.append('m')
        elif entry[4] == '1':
            markup.append('f')
        elif entry[5] == '1':
            markup.append('n')
        elif entry[6] == '1':
            markup.append('u')
        else:
            markup.append('?')

    if entry[9] == '1':
        if entry[10] == '1':
            markup.append('wk')
        if entry[11] == '1':
            markup.append('str')
        if entry[12] == '1':
            markup.append('pretpres')
        if entry[13] == '1':
            markup.append('anom')
        if entry[14] == '1':
            markup.append('?')
        if entry[15] == '1':
            markup.append('contracted')
        if entry[16] == '1':
            markup.append('ppl')


    return(markup)

