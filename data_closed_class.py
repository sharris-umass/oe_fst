#! usr/bin/env python3
"""
Takes a term and determines if it is a closed-class word or if its
inflections indicate that it is very likely a noun, adjective, adverb, or verb

Copyright Steve Harris, UMass Amherst 2022
"""

def get_pos(term):
    import re
    morphology =[]

    term = term.lower()

# ___________________________________________________________ ADVERBS

    if re.findall(r'^nu$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5') 
    if re.findall(r'^eft$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5') 
    if re.findall(r'^eac$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 2') 
    if re.findall(r'^ær$', term, re.IGNORECASE):
        morphology.append('ADV 3') 
    if re.findall(r'^oft$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5') 
    if re.findall(r'^(ð|þ)eah$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 2') 
    if re.findall(r'^(ð|þ)eah$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 2') 
    if re.findall(r'^sum$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 1') 
    if re.findall(r'^sume$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 2')
    if re.findall(r'^(a|æ)$', term, re.IGNORECASE):
        morphology.append('ADV 5')
    if re.findall(r'^(a|æ)fter$', term, re.IGNORECASE):
        morphology.append('ADV 2') 
    if re.findall(r'^(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('ADV 3') 
    if re.findall(r'^(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('ADV 3')
    if re.findall(r'^(ð|þ)(a|æ)r$', term, re.IGNORECASE):
        morphology.append('ADV 5')
    if re.findall(r'^(ð|þ)(a|æ)re$', term, re.IGNORECASE):
        morphology.append('ADV 5')
    if re.findall(r'^(ð|þ)enden$', term, re.IGNORECASE):
        morphology.append('ADV 3') 
    if re.findall(r'^(ð|þ)ider$', term, re.IGNORECASE):
        morphology.append('ADV 3') 
    if re.findall(r'lice$', term, re.IGNORECASE):
        morphology.append('ADV UNDECL 5') 
    if re.findall(r'unga$', term, re.IGNORECASE):
        morphology.append('ADV UNDECL 5')
    if re.findall(r'^for(þ|ð)on$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5')
    if re.findall(r'^iu$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5')
    if re.findall(r'^geo$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5')
    if re.findall(r'^hwile$', term, re.IGNORECASE):
        morphology.append('ADV UNDCL 5')

    # ___________________________________________________________ PREPOSITIONS
    if re.findall(r'^o(ð|þ)$', term, re.IGNORECASE):
        morphology.append('PRP ACC 4') 
    if re.findall(r'(ð|þ)urh$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^ymbe$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^æfter$', term, re.IGNORECASE):
        morphology.append('PRP ACC 3') 
    if re.findall(r'^after$', term, re.IGNORECASE):
        morphology.append('PRP ACC 3') 
    if re.findall(r'^ær$', term, re.IGNORECASE):
        morphology.append('PRP ACC 3') 
    if re.findall(r'^be$', term, re.IGNORECASE):
        morphology.append('PRP ACC 4') 
    if re.findall(r'^bi$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^binnan$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^butan$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^fram$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^from$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^mid$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5')
    if re.findall(r'^midd$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5')
    if re.findall(r'^of$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5') 
    if re.findall(r'^to$', term, re.IGNORECASE):
        morphology.append('PRP ACC 5')

    if re.findall(r'^ofer$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^on$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^under$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^wi(ð|þ)$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^æt$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^for$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5') 
    if re.findall(r'^in$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5')
    if re.findall(r'^inne$', term, re.IGNORECASE):
        morphology.append('PRP ACCDAT 5')

    # ___________________________________________________________ PRONOUNS
    if re.findall(r'^se$', term, re.IGNORECASE):
        morphology.append('PRN DET M NOM S 5') 
    if re.findall(r'(ð|þ)æs$', term, re.IGNORECASE):
        morphology.append('PRN DET M GEN S 5') 
    if re.findall(r'(ð|þ)æm$', term, re.IGNORECASE):
        morphology.append('PRN DET M DAT S 5') 
    if re.findall(r'(ð|þ)y$', term, re.IGNORECASE):
        morphology.append('PRN DET M INS S 5') 
    if re.findall(r'(ð|þ)æt$', term, re.IGNORECASE):
        morphology.append('PRN DET N NOM S 5') 
    if re.findall(r'(ð|þ)æs$', term, re.IGNORECASE):
        morphology.append('PRN DET N GEN S 5') 
    if re.findall(r'(ð|þ)æm$', term, re.IGNORECASE):
        morphology.append('PRN DET N DAT S 5') 
    if re.findall(r'(ð|þ)y$', term, re.IGNORECASE):
        morphology.append('PRN DET N INS S 5') 
    if re.findall(r'(ð|þ)on$', term, re.IGNORECASE):
        morphology.append('PRN DET N INS S 5') 
    if re.findall(r'^seo$', term, re.IGNORECASE):
        morphology.append('PRN DET F NOM S 5') 
    if re.findall(r'(ð|þ)ære$', term, re.IGNORECASE):
        morphology.append('PRN DET F GEN S 5') 
    if re.findall(r'(ð|þ)ære$', term, re.IGNORECASE):
        morphology.append('PRN DET F DAT S 5') 
    if re.findall(r'(ð|þ)ære$', term, re.IGNORECASE):
        morphology.append('PRN DET F INS S 5') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET M NOM PL 3') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET N NOM PL 3') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET F NOM PL 3') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET M ACC PL 3') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET N ACC PL 3') 
    if re.findall(r'(ð|þ)a$', term, re.IGNORECASE):
        morphology.append('PRN DET F ACC PL 3') 
    if re.findall(r'(ð|þ)ara$', term, re.IGNORECASE):
        morphology.append('PRN DET M GEN PL 5') 
    if re.findall(r'(ð|þ)ara$', term, re.IGNORECASE):
        morphology.append('PRN DET N GEN PL 5') 
    if re.findall(r'(ð|þ)ara$', term, re.IGNORECASE):
        morphology.append('PRN DET F GEN PL 5') 
    if re.findall(r'(ð|þ)(æ|a)m$', term, re.IGNORECASE):
        morphology.append('PRN DET M DAT PL 5') 
    if re.findall(r'(ð|þ)(æ|a)m$', term, re.IGNORECASE):
        morphology.append('PRN DET N DAT PL 5') 
    if re.findall(r'(ð|þ)(æ|a)m$', term, re.IGNORECASE):
        morphology.append('PRN DET F DAT PL 5') 
    if re.findall(r'^ic$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 NOM S 5') 
    if re.findall(r'^min$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 GEN S 5') 
    if re.findall(r'^minne$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 GEN S 5') 
    if re.findall(r'^me$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 DAT S 5') 
    if re.findall(r'^mec$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 ACC S 5') 
    if re.findall(r'^wit$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 NOM D 5') 
    if re.findall(r'^uncer$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 GEN D 5') 
    if re.findall(r'^unc$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 DAT D 5') 
    if re.findall(r'^we$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 NOM PL 5') 
    if re.findall(r'^ure$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 GEN PL 5') 
    if re.findall(r'^us$', term, re.IGNORECASE):
        morphology.append('PRN PERS 1 DAT PL 5') 
    if re.findall(r'^(ð|þ)u$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 NOM S 5') 
    if re.findall(r'^(ð|þ)in$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 GEN S 5')
    if re.findall(r'^(ð|þ)inre$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 GEN S 5')
    if re.findall(r'^(ð|þ)e$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 DAT S 3') 
    if re.findall(r'^git$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 NOM D 5') 
    if re.findall(r'^incer$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 GEN D 5') 
    if re.findall(r'^inc$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 DAT D 5') 
    if re.findall(r'^ge$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 NOM PL 5') 
    if re.findall(r'^eower$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 GEN PL 5') 
    if re.findall(r'^eow$', term, re.IGNORECASE):
        morphology.append('PRN PERS 2 DAT PL 5') 
    if re.findall(r'^he$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M NOM S 5') 
    if re.findall(r'^his$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M GEN S 5') 
    if re.findall(r'^him$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M DAT S 5') 
    if re.findall(r'^hit$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N NOM S 5') 
    if re.findall(r'^his$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N GEN S 5') 
    if re.findall(r'^him$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N DAT S 5') 
    if re.findall(r'^heo$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F NOM S 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F ACC S 5') 
    if re.findall(r'^hie$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F ACC S 5') 
    if re.findall(r'^hire$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F GEN S 5') 
    if re.findall(r'^hire$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F DAT S 5') 
    if re.findall(r'^hie$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M NOM PL 5') 
    if re.findall(r'^hie$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F NOM PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M NOM PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N NOM PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F NOM PL 5') 
    if re.findall(r'^hie$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M ACC PL 5') 
    if re.findall(r'^hie$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F ACC PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M ACC PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N ACC PL 5') 
    if re.findall(r'^hi$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F ACC PL 5') 
    if re.findall(r'^hi(e?)ra$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M GEN PL 5') 
    if re.findall(r'^hi(e?)ra$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F GEN PL 5') 
    if re.findall(r'^h(e|i)ora$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M GEN PL 5') 
    if re.findall(r'^h(e|i)ora$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N GEN PL 5') 
    if re.findall(r'^h(e|i)ora$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F GEN PL 5') 
    if re.findall(r'^h(i|eo)m$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 M GEN PL 5') 
    if re.findall(r'^h(i|eo)m$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 N GEN PL 5') 
    if re.findall(r'^h(i|eo)m$', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F GEN PL 5') 
    if re.findall(r'^sw(e|i|y)lc', term, re.IGNORECASE):
        morphology.append('PRN PERS 3 F NOM S 3') 
    if re.findall(r'(ð|þ)es$', term, re.IGNORECASE):
        morphology.append('PRN DEM M NOM S 5') 
    if re.findall(r'(ð|þ)isses$', term, re.IGNORECASE):
        morphology.append('PRN DEM M GEN S 5') 
    if re.findall(r'(ð|þ)issum$', term, re.IGNORECASE):
        morphology.append('PRN DEM M DAT S 5') 
    if re.findall(r'(ð|þ)ys\b$', term, re.IGNORECASE):
        morphology.append('PRN DEM M INS S 5') 
    if re.findall(r'(ð|þ)is$', term, re.IGNORECASE):
        morphology.append('PRN DEM N NOM S 5') 
    if re.findall(r'(ð|þ)isses$', term, re.IGNORECASE):
        morphology.append('PRN DEM N GEN S 5') 
    if re.findall(r'(ð|þ)issum$', term, re.IGNORECASE):
        morphology.append('PRN DEM N DAT S 5') 
    if re.findall(r'(ð|þ)ys$', term, re.IGNORECASE):
        morphology.append('PRN DEM N INS S 5') 
    if re.findall(r'(ð|þ)eos$', term, re.IGNORECASE):
        morphology.append('PRN DEM F NOM S 5') 
    if re.findall(r'(ð|þ)isse$', term, re.IGNORECASE):
        morphology.append('PRN DEM F GEN S 5') 
    if re.findall(r'(ð|þ)isre$', term, re.IGNORECASE):
        morphology.append('PRN DEM F GEN S 5') 
    if re.findall(r'(ð|þ)isse$', term, re.IGNORECASE):
        morphology.append('PRN DEM F DAT S 5') 
    if re.findall(r'(ð|þ)as$', term, re.IGNORECASE):
        morphology.append('PRN DEM M NOM PL 5') 
    if re.findall(r'(ð|þ)as$', term, re.IGNORECASE):
        morphology.append('PRN DEM N NOM PL 5') 
    if re.findall(r'(ð|þ)as$', term, re.IGNORECASE):
        morphology.append('PRN DEM N ACC PL 5') 
    if re.findall(r'(ð|þ)as$', term, re.IGNORECASE):
        morphology.append('PRN DEM F NOM PL 5') 
    if re.findall(r'(ð|þ)as$', term, re.IGNORECASE):
        morphology.append('PRN DEM F ACC PL 5') 
    if re.findall(r'(ð|þ)is(s|r)a$', term, re.IGNORECASE):
        morphology.append('PRN DEM M GEN PL 5') 
    if re.findall(r'(ð|þ)is(s|r)a$', term, re.IGNORECASE):
        morphology.append('PRN DEM N GEN PL 5') 
    if re.findall(r'(ð|þ)is(s|r)a$', term, re.IGNORECASE):
        morphology.append('PRN DEM F GEN PL 5') 
    if re.findall(r'^(ð|þ)issum$', term, re.IGNORECASE):
        morphology.append('PRN DEM M DAT PL 5') 
    if re.findall(r'^(ð|þ)issum$', term, re.IGNORECASE):
        morphology.append('PRN DEM N DAT PL 5') 
    if re.findall(r'^(ð|þ)issum$', term, re.IGNORECASE):
        morphology.append('PRN DEM F DAT PL 5') 
    if re.findall(r'^hwa$', term, re.IGNORECASE):
        morphology.append('PRN INT M NOM S 5') 
    if re.findall(r'^hwonne$', term, re.IGNORECASE):
        morphology.append('PRN INT M ACC S 5') 
    if re.findall(r'^hwæs$', term, re.IGNORECASE):
        morphology.append('PRN INT M GEN S 5') 
    if re.findall(r'^hw(æ|a)m$', term, re.IGNORECASE):
        morphology.append('PRN INT M DAT S 5') 
    if re.findall(r'^hwy$', term, re.IGNORECASE):
        morphology.append('PRN INT M INS S 5') 
    if re.findall(r'^hwæt$', term, re.IGNORECASE):
        morphology.append('PRN INT N NOM S 3') 
    if re.findall(r'^hwæt$', term, re.IGNORECASE):
        morphology.append('PRN INT N ACC S 3') 
    if re.findall(r'^hwæs$', term, re.IGNORECASE):
        morphology.append('PRN INT N GEN S 5') 
    if re.findall(r'^hwæm$', term, re.IGNORECASE):
        morphology.append('PRN INT N DAT S 5') 
    if re.findall(r'^hwy$', term, re.IGNORECASE):
        morphology.append('PRN INT N INS S 5') 
    if re.findall(r'^hwon$', term, re.IGNORECASE):
        morphology.append('PRN INT N INS S 5') 
    if re.findall(r'^hwa$', term, re.IGNORECASE):
        morphology.append('PRN INT F NOM S 5') 
    if re.findall(r'^hwæs$', term, re.IGNORECASE):
        morphology.append('PRN INT F GEN S 5') 
    if re.findall(r'^hw(æ|a)m$', term, re.IGNORECASE):
        morphology.append('PRN INT F DAT S 5')
    if re.findall(r'^sylfa$', term, re.IGNORECASE):
        morphology.append('PRN REFLX')
    if re.findall(r'^sylfe$', term, re.IGNORECASE):
        morphology.append('PRN REFLX')
    if re.findall(r'^sylfes$', term, re.IGNORECASE):
        morphology.append('PRN REFLX')
    if re.findall(r'^sylfum$', term, re.IGNORECASE):
        morphology.append('PRN REFLX')

    # ___________________________________________________________ NUMERALS
    if re.findall(r'^an$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twegen$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^(ð|þ)rie$', term, re.IGNORECASE):
        morphology.append('NUM 5')
    if re.findall(r'^feower$', term, re.IGNORECASE):
        morphology.append('NUM 5')
    if re.findall(r'^fif$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^siex$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^seofon$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^eahta$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^nigon$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^tien$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^begen$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^ba$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^bu$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twa$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twu$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^twegra$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twega$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twæm$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^begra$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^bega$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^bæm$', term, re.IGNORECASE):
        morphology.append('NUM 3') 
    if re.findall(r'^twentig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^(ð|þ)ritig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^feowrtig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^fiftig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^siextig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^seofontig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^eahtig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^nigontig$', term, re.IGNORECASE):
        morphology.append('NUM 5') 
    if re.findall(r'^hundert$', term, re.IGNORECASE):
        morphology.append('NUM 5')

    # ___________________________________________________________ CONJUNCTIONS
    if re.findall(r'^ond$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^and$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^ac$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^ær$', term, re.IGNORECASE):
        morphology.append('CNJ 3') 
    if re.findall(r'^\&$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^for(ð|þ)am$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^gif$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^nu$', term, re.IGNORECASE):
        morphology.append('CNJ 3') 
    if re.findall(r'^o(ð|þ)$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^o(ð|þ)at$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^o(ð|þ)æt$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^swa$', term, re.IGNORECASE):
        morphology.append('CNJ 4') 
    if re.findall(r'^(ð|þ)e$', term, re.IGNORECASE):
        morphology.append('CNJ 3') 
    if re.findall(r'^but(a|o)n$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^sam$', term, re.IGNORECASE):
        morphology.append('CNJ 5') 
    if re.findall(r'^si(ð|þ)(ð|þ)an$', term, re.IGNORECASE):
        morphology.append('CNJ 3') 
    if re.findall(r'^sw(e|i|y)lce$', term, re.IGNORECASE):
        morphology.append('CNJ 3') 
    if re.findall(r'^hwonne$', term, re.IGNORECASE):
        morphology.append('CNJ 3')

    # ___________________________________________________________ NEGATIVE
    if re.findall(r'^ne$', term, re.IGNORECASE):
        morphology.append('NEG 5')

    # ___________________________________________________________ INTERJECTIONS
    if re.findall(r'^gea$', term, re.IGNORECASE):
        morphology.append('INTJ 5') 
    if re.findall(r'^eala$', term, re.IGNORECASE):
        morphology.append('INTJ 5') 
    if re.findall(r'^hwæt$', term, re.IGNORECASE):
        morphology.append('INTJ 3')

    # ___________________________________________________________ ADJECTIVES
    if re.findall(r'.+ig$', term, re.IGNORECASE):
        morphology.append('ADJ S M NOM S 5') 
    if re.findall(r'.+ig$', term, re.IGNORECASE):
        morphology.append('ADJ S N NOM S 5') 
    if re.findall(r'.+ig$', term, re.IGNORECASE):
        morphology.append('ADJ S N ACC S 5') 
    if re.findall(r'.+(e|o)st$', term, re.IGNORECASE):
        morphology.append('ADJ SUPL 3')
    if re.findall(r'.+or$', term, re.IGNORECASE):
        morphology.append('ADJ CMP 3')
    if re.findall(r'.{1,15}ne$', term, re.IGNORECASE):
        morphology.append('ADJ S M ACC S 3')
    if re.findall(r'.{1,15}lic$', term, re.IGNORECASE):
        morphology.append('ADJ 5')
    if re.findall(r'.{1,15}licost$', term, re.IGNORECASE):
        morphology.append('ADJ 5')
        if re.findall(r'.{1,15}licor$', term, re.IGNORECASE):
            morphology.append('ADJ 5')

    # ___________________________________________________________ CONTRACTIONS
    if re.findall(r'^nyl?e$', term, re.IGNORECASE):
        morphology.append('NEG VERB')
    if re.findall(r'^nolde$', term, re.IGNORECASE):
        morphology.append('NEG VERB')

    # ___________________________________________________________ VERBS
#    if re.findall(r'.+an$', term, re.IGNORECASE):
#        morphology.append('VERB INF 2')
    if re.findall(r'^eom$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRES IND 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRES IND 5') 
    if re.findall(r'^eart$', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRES IND 5') 
    if re.findall(r'^bist$', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRES IND 5') 
    if re.findall(r'^is$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRES IND 5')
    if re.findall(r'^ys$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRES IND 5')
    if re.findall(r'^bi(þ|ð)$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRES IND 5') 
    if re.findall(r'^sin(d|don)$', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRES IND 5') 
    if re.findall(r'^sin(d|don)$', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRES IND 5') 
    if re.findall(r'^sin(d|don)$', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRES IND 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRES IND 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRES IND 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRES IND 5')
    if re.findall(r'^sy$', term, re.IGNORECASE):
        morphology.append('VERB SBJ 5')
    if re.findall(r'^sie$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRES SBJ 5') 
    if re.findall(r'^sie$', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRES SBJ 5') 
    if re.findall(r'^sie$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRES SBJ 5') 
    if re.findall(r'^sien$', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRES SBJ 5') 
    if re.findall(r'^sien$', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRES SBJ 5') 
    if re.findall(r'^sien$', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRES SBJ 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRES SBJ 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRES SBJ 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRES SBJ 5') 
    if re.findall(r'^beon$', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRES SBJ 5') 
    if re.findall(r'^beon$', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRES SBJ 5') 
    if re.findall(r'^beon$', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRES SBJ 5') 
    if re.findall(r'^was$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRT IND 5') 
    if re.findall(r'^wære', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRT IND 5')
    if re.findall(r'^wear(þ|ð)$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRT IND 5')
    if re.findall(r'^weor(þ|ð)$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRT IND 5')
    if re.findall(r'^weor(þ|ð)en$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRT SUBJ 5')
    if re.findall(r'^wæs', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRT IND 5') 
    if re.findall(r'^wæron', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRT IND 5') 
    if re.findall(r'^wæron', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRT IND 5') 
    if re.findall(r'^wæron', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRT IND 5')
    if re.findall(r'^næron', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRT IND 5')
    if re.findall(r'^were$', term, re.IGNORECASE):
        morphology.append('VERB 1 S PRT SBJ 4') 
    if re.findall(r'^were$', term, re.IGNORECASE):
        morphology.append('VERB 2 S PRT SBJ 4') 
    if re.findall(r'^were$', term, re.IGNORECASE):
        morphology.append('VERB 3 S PRT SBJ 4') 
    if re.findall(r'^weren$', term, re.IGNORECASE):
        morphology.append('VERB 1 P PRT SBJ 5') 
    if re.findall(r'^weren$', term, re.IGNORECASE):
        morphology.append('VERB 2 P PRT SBJ 5') 
    if re.findall(r'^weren$', term, re.IGNORECASE):
        morphology.append('VERB 3 P PRT SBJ 5') 
    if re.findall(r'^wesan$', term, re.IGNORECASE):
        morphology.append('VERB INF 5') 
    if re.findall(r'^beon$', term, re.IGNORECASE):
        morphology.append('VERB INF 5') 
    if re.findall(r'^wes$', term, re.IGNORECASE):
        morphology.append('VERB 1 S IMP 5') 
    if re.findall(r'^wes$', term, re.IGNORECASE):
        morphology.append('VERB 2 S IMP 5') 
    if re.findall(r'^wes$', term, re.IGNORECASE):
        morphology.append('VERB 3 S IMP 5') 
    if re.findall(r'^wesa(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 1 P IMP 5') 
    if re.findall(r'^wesa(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 2 P IMP 5') 
    if re.findall(r'^wesa(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 3 P IMP 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 1 S IMP 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 2 S IMP 5') 
    if re.findall(r'^beo$', term, re.IGNORECASE):
        morphology.append('VERB 3 S IMP 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 1 P IMP 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 2 P IMP 5') 
    if re.findall(r'^beo(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB 3 P IMP 5') 
    if re.findall(r'^beonne$', term, re.IGNORECASE):
        morphology.append('VERB GER 5') 
    if re.findall(r'^wesende$', term, re.IGNORECASE):
        morphology.append('VERB PPL 5') 
    if re.findall(r'^sceal$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 1S 5') 
    if re.findall(r'^sculon$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 1P 5') 
    if re.findall(r'^wille$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 1S 3') 
    if re.findall(r'^wille$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 123S SUBJ 3') 
    if re.findall(r'^wile$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 3S 3') 
    if re.findall(r'^willa(ð|þ)$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 123P 5') 
    if re.findall(r'^willen$', term, re.IGNORECASE):
        morphology.append('VERB MODAL 123P SUBJ 5') 
    if re.findall(r'^wolde$', term, re.IGNORECASE):
        morphology.append('VERB MODAL PT 5') 
    if re.findall(r'^woldon$', term, re.IGNORECASE):
        morphology.append('VERB MODAL PT 5') 
    if re.findall(r'^wolden$', term, re.IGNORECASE):
        morphology.append('VERB MODAL PT SUBJ 5') 
    return morphology
