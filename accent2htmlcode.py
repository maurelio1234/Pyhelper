# -*- coding: utf-8 -*-
# based on http://code.activestate.com/recipes/546517-accent2htmlcodepy-convert-accents-and-special-char/download/1/ 
# adapted to be used as a module

# accent2htmlcode.py might be useful to someone out there
# on the other hand, if it causes extensive damage 
# to your computer, home and property I am not responsible in 
# any way
htmlcodes = ['&Aacute;', '&aacute;', '&Agrave;', '&Acirc;', '&agrave;', '&Acirc;', '&acirc;', '&Auml;', '&auml;', '&Atilde;', '&atilde;', '&Aring;', '&aring;', '&Aelig;', '&aelig;', '&Ccedil;', '&ccedil;', '&Eth;', '&eth;', '&Eacute;', '&eacute;', '&Egrave;', '&egrave;', '&Ecirc;', '&ecirc;', '&Euml;', '&euml;', '&Iacute;', '&iacute;', '&Igrave;', '&igrave;', '&Icirc;', '&icirc;', '&Iuml;', '&iuml;', '&Ntilde;', '&ntilde;', '&Oacute;', '&oacute;', '&Ograve;', '&ograve;', '&Ocirc;', '&ocirc;', '&Ouml;', '&ouml;', '&Otilde;', '&otilde;', '&Oslash;', '&oslash;', '&szlig;', '&Thorn;', '&thorn;', '&Uacute;', '&uacute;', '&Ugrave;', '&ugrave;', '&Ucirc;', '&ucirc;', '&Uuml;', '&uuml;', '&Yacute;', '&yacute;', '&yuml;', '&copy;', '&reg;', '&trade;', '&euro;', '&cent;', '&pound;', '&lsquo;', '&rsquo;', '&ldquo;', '&rdquo;', '&laquo;', '&raquo;', '&mdash;', '&ndash;', '&deg;', '&plusmn;', '&frac14;', '&frac12;', '&frac34;', '&times;', '&divide;', '&alpha;', '&beta;', '&infin', '&eacute;']
funnychars = [u'\xc1',u'\xe1',u'\xc0',u'\xc2',u'\xe0',u'\xc2',u'\xe2',u'\xc4',u'\xe4',u'\xc3',u'\xe3',u'\xc5',u'\xe5',u'\xc6',u'\xe6',u'\xc7',u'\xe7',u'\xd0',u'\xf0',u'\xc9',u'\xe9',u'\xc8',u'\xe8',u'\xca',u'\xea',u'\xcb',u'\xeb',u'\xcd',u'\xed',u'\xcc',u'\xec',u'\xce',u'\xee',u'\xcf',u'\xef',u'\xd1',u'\xf1',u'\xd3',u'\xf3',u'\xd2',u'\xf2',u'\xd4',u'\xf4',u'\xd6',u'\xf6',u'\xd5',u'\xf5',u'\xd8',u'\xf8',u'\xdf',u'\xde',u'\xfe',u'\xda',u'\xfa',u'\xd9',u'\xf9',u'\xdb',u'\xfb',u'\xdc',u'\xfc',u'\xdd',u'\xfd',u'\xff',u'\xa9',u'\xae',u'\u2122',u'\u20ac',u'\xa2',u'\xa3',u'\u2018',u'\u2019',u'\u201c',u'\u201d',u'\xab',u'\xbb',u'\u2014',u'\u2013',u'\xb0',u'\xb1',u'\xbc',u'\xbd',u'\xbe',u'\xd7',u'\xf7',u'\u03b1',u'\u03b2',u'\u221e', u'è']

def replace_accents(textcontent):
    newtext = u''
    for char in textcontent:
        uchar = unicode(char)
        if uchar not in funnychars:
            newtext = newtext + uchar
        else:
            newtext  = newtext + htmlcodes[funnychars.index(uchar)]
    return newtext
