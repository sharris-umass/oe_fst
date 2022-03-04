# **Old English Nouns**
___

AIM: Improved parsing of Old English nouns and noun phrases.

TAKES: a sentence in Old English \
RETURNS: all nouns


Description of Files
---

**Glossaries**.
<ul>The files beginning with `data_` are taken from the main dictionaries of Old English. \
Each entry in the JSON array comprises the OE lexeme (that is, the dictionary entry) and its most likely part of speech (POS).

For example, the entry `"witscipe" : "NOUN m"`

The OE word *witscipe* 'knowledge, evidence' is the KEY. The part of speech is the VALUE&mdash;here a noun of the masculine gender.
</ul>

**Word Lists**.
<ul>
The following files were culled from the glossaries, and all nouns put into one files, all adjectives into another, and so on:
1. lemmas.txt (all words in dictionary form)
2. nouns.txt
3. prefixes.txt
4. suffixes.txt
5. verbs.txt
</ul>

Design
---

First, I check to see if an OE word is on a list of nouns.

Second, I check to see if it is also on another list. 
<ul>Some words can be both nouns and adjectives. OE *god* can mean either 'good' or 'God'. 
Other words can be nouns or conjunctions! OE *ac* means both 'oak' and 'but'. OE *þa* can be a pronoun,
an adverb, or a conjunction.</ul>

Third, I check the environment of the OE word for tell-tale signs that it is a noun.
