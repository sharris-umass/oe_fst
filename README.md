# **Old English Parser**
___

**AIM**: NLP parser of Old English. Attempts a best guess, rather than certainty.

**TAKES**: a sentence in Old English \
**RETURNS**: list of words with grammatical tags


Description of Files
---

**Glossaries**.
<ul>The files beginning with `data_` are compiled from the main dictionaries of Old English. <br>
Each entry in the JSON array comprises the OE lexeme (that is, the dictionary entry) and its most likely part of speech (POS).

For example, the entry `"witscipe" : "NOUN m"`

The OE word *witscipe* 'knowledge, evidence' is the KEY. The part of speech is the VALUE&mdash;here a noun of the masculine gender.
</ul>

**Word Lists**.
<ul>
The following files were culled from the glossaries, and all nouns put into one files, all adjectives into another, and so on:
  <li>1. lemmas.txt (all words in dictionary form)</li>
<li>2. nouns.txt</li>
<li>3. prefixes.txt</li>
<li>4. suffixes.txt</li>
<li>5. verbs.txt</li>
</ul>

Design
---

First, I check to see if an OE word is a value on a list.

Second, I check to see if it is also on another list. 
<ul>Some words can be both nouns and adjectives. OE *god* can mean either 'good' or 'God'. 
Other words can be nouns or conjunctions! OE *ac* means both 'oak' and 'but'. OE *þa* can be a pronoun,
an adverb, or a conjunction.</ul>

Third, I check the OE word for tell-tale signs of its POS (prefixes, suffixes, etc.). Prefixes are listed
in a file called **prefixes.txt**. Suffixes are listed in **suffixes.txt**.

Fourth, I check the environment of the OE word. Does the word follow a preposition (PRP), for example?
