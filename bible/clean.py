#! usr/bin/env python3

"""
Cleans DOE corpus of all tags
"""

import re


with open('GLOSSES.txt') as fp:
    text = fp.read()

# clean HTML entities
    text = re.sub(r"\&T\;", "Þ", text)
    text = re.sub(r"\&t\;", "þ", text)
    text = re.sub(r"\&D\;", "Ð", text)
    text = re.sub(r"\&d\;", "ð", text)
    text = re.sub(r"\&AE\;", "Æ", text)
    text = re.sub(r"\&ae\;", "æ", text)
    text = re.sub(r"\&ouml\;", "o", text)
    text = re.sub(r"\&amp\;", r"&", text)
    text = re.sub(r"\&eacute\;", "é", text)
    text = re.sub(r"\&e\;", "e", text)

# clean basic tags
    text = re.sub(r"<body>", "", text)
    text = re.sub(r"<text>", "", text)
    text = re.sub(r"<p>", "", text)
    text = re.sub(r"</body>", "", text)
    text = re.sub(r"</text>", "", text)
    text = re.sub(r"</p>", "", text)
    text = re.sub(r"<corr>", "", text)
    text = re.sub(r"</corr>", "", text)

# modify tags
    text = re.sub(r"(\d)\">", r"\1.", text)
    text = re.sub(r"n=\"", "", text)
    text = re.sub(r"id=\"\w\d{11}\"", "", text)
    text = re.sub(r"<s\s+?", "", text)

# put in newlines and scrub
    text = re.sub(r"</s>", "\n", text)
    text = re.sub(r"\n\n", "\n", text)
    text = re.sub(r"</tei\.2>", "\nEND_TEXT\nSTART_TEXT\n", text)


# reduce headers
    text = re.sub(r"<teiheader>", "", text)
    text = re.sub(r"</teiheader>", "", text)
    text = re.sub(r"<fileDesc>", "", text)
    text = re.sub(r"</filedesc>", "", text)
    text = re.sub(r"<titlestmt>", "", text)
    text = re.sub(r"</titlestmt>", "", text)
    text = re.sub(r"<publicationstmt>", "", text)
    text = re.sub(r"</publicationstmt>", "", text)
    text = re.sub(r"<availability>", "", text)
    text = re.sub(r"</availability>", "", text)
    text = re.sub(r"<address>", "", text)
    text = re.sub(r"</address>", "", text)
    text = re.sub(r"\&doeaddress\;", "", text)
    text = re.sub(r"<publisher>Dictionary of Old English</publisher>", "", text)
    text = re.sub(r"We ask that you .+? of the material", "", text)
    text = re.sub(r"<encodingdesc>", "", text)
    text = re.sub(r"</encodingdesc>", "", text)
    text = re.sub(r"<refsdecl>", "", text)
    text = re.sub(r"</refsdecl>", "", text)
    text = re.sub(r"<profiledesc>", "", text)
    text = re.sub(r"</profiledesc>", "", text)
    text = re.sub(r"<textclass>", "", text)
    text = re.sub(r"</textclass>", "", text)
    text = re.sub(r"<catref target=\"\w\w\w\">", "", text)
    text = re.sub(r"<P>Cited.+?</P>", "", text)
    text = re.sub(r"<tei\.2.+?\d\d\d\d\d\.", "", text)
    text = re.sub(r"<hi rend=\"rune\">.+?</hi>", r"", text)

    text = re.sub(r"<title type=\"st\">(.+?)</title>", r"\1", text)
    text = re.sub(r"<title type=\"ss\">(.+?)</title>", r"", text)
    text = re.sub(r"<extent>(.+?)</extent>", r"", text)
    text = re.sub(r"<idno>(.+?)</idno>", r"\n\1", text)

    text = re.sub(r"<sourcedesc><bibl>(.+?)</bibl></sourcedesc>", r"\n\1", text)


    print(text)
