#! usr/bin/env python3
"""
Used by control.py and control_module.py to access json files
Allows searches of the bt json file, bt_edited, raw data, and Bright's Old English Grammar
"""

import json
import re
import bt_markup


def get_pos(sent_word):     # Searches JSON version of Bosworth-Toller

    with open("data_bosToll.json", 'r') as json_data:
        results = []
        bosworth = json.load(json_data)

        for word, part_of_speech in bosworth.items():

            if word == sent_word:
                results.append(part_of_speech)

        return results


def get_rawentry(incoming):     # searches raw data of Bosworth-Toller

    incoming = incoming.strip()
    all_results = []

    with open("data_bt_edited.txt", 'r') as raw_data:
        data = raw_data.read()
        data_lines = data.split('\n')
        raw_data.close()

        for line in data_lines:
            pieces = line.split(':')
            if re.fullmatch(incoming, pieces[0]):

                result = bt_markup.info(line)
                if result == []:
                    continue
                else:
                    all_results.append(result)

    return all_results


def get_brights(word_incoming):     # Searches JSON version of Brights

    with open("data_brights.json", 'r') as json_d:
        brights_results = []
        brights = json.load(json_d)

        for word, part_of_speech in brights.items():

            if word.lower() == word_incoming.lower():
                brights_results.append(part_of_speech)

        return brights_results


def get_texas(word_in):     # Searches JSON version of Brights

    with open("data_tx_glossary.json", 'r') as json_d:
        tx_results = []
        tx = json.load(json_d)

        for word, part_of_speech in tx.items():

            if word.lower() == word_in.lower():
                tx_results.append(part_of_speech)

        return tx_results


def get_clark(wordamungo):     # Searches JSON version of Clark-Hall

    with open("data_clark_new.json", 'r') as json_data:
        ch_results = []
        ch = json.load(json_data)

        for word, part_of_speech in ch.items():

            if word.lower() == wordamungo.lower():
                ch_results.append(part_of_speech)

        return ch_results
