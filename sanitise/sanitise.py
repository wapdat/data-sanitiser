import re
import nltk

debug = False
list = ''

def tokenise(doc):
    tokenized_doc = nltk.word_tokenize(doc)
    tagged_sentences = nltk.pos_tag(tokenized_doc)
    ne_chunked_sents = nltk.ne_chunk(tagged_sentences)
    named_entities = []
    for tagged_tree in ne_chunked_sents:
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
            entity_type = tagged_tree.label() # get NE category
            named_entities.append((entity_name, entity_type))
            doc = doc.replace(entity_name, entity_type)
    if (debug) : print(named_entities)
    if (debug) : print('%-20s "%s"' % ('NER', doc))
    return doc
    

def regexReplace( str, token, desc, regex):
    global list
    list  = list + ', ' + desc
    r = re.compile(regex)
    cleanStr = re.sub( r, token, str, re.I)
    if (debug) : 
        if (str != cleanStr):
            print('%-20s "%s"' % (desc, cleanStr))
    return cleanStr


def replacePPI(str):
    str = regexReplace(str, 'NAME@EMAIL.COM', 'email address', '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    str = regexReplace(str, 'UKPOSTCODE', 'uk postcode', '(gir ?0aa|GIR ?0AA|[a-pr-uwyzA-PR-UWYZ]([0-9]{1,2}|([a-hk-yA-HK-Y][0-9]([0-9abehmnprv-yABEHMNPRV-Y])?)|[0-9][a-hjkps-uwA-HJKPS-UW]) ?[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2})')
    # Amex numbers look like US phone numbers
    str = regexReplace(str, 'CARDNUM', 'Amex', '3[47][0-9]{13}')
    str = regexReplace(str, 'CARDNUM', 'BCGlobal', '(6541|6556)[0-9]{12}')
    str = regexReplace(str, 'CARDNUM', 'Carte Blanche Card', '389[0-9]{11}')
    str = regexReplace(str, 'CARDNUM', 'Diners Club Card', '3(?:0[0-5]|[68][0-9])[0-9]{11}')
    str = regexReplace(str, 'CARDNUM', 'Discover Card', '65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})')
    str = regexReplace(str, 'CARDNUM', 'Insta Payment Card', '63[7-9][0-9]{13}')
    str = regexReplace(str, 'CARDNUM', 'JCB Card', '(?:2131|1800|35\d{3})\d{11}$')
    str = regexReplace(str, 'CARDNUM', 'KoreanLocalCard', '9[0-9]{15}')
    str = regexReplace(str, 'CARDNUM', 'Laser Card', '(6304|6706|6709|6771)[0-9]{12,15}')
    str = regexReplace(str, 'CARDNUM', 'Maestro Card', '(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}')
    str = regexReplace(str, 'CARDNUM', 'Mastercard', '5[1-5][0-9]{14}')
    str = regexReplace(str, 'CARDNUM', 'Solo Card', '(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}')
    str = regexReplace(str, 'CARDNUM', 'Switch Card', '(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}')
    str = regexReplace(str, 'CARDNUM', 'Union Pay Card', '(62[0-9]{14,17})')
    str = regexReplace(str, 'CARDNUM', 'Visa Card', '4[0-9]{12}(?:[0-9]{3})?')
    str = regexReplace(str, 'CARDNUM', 'Visa Master Card', '(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})')
    str = regexReplace(str, 'ZIPCODEUS' , 'zip code', '[0-9]{5}(-[0-9]{4})?')
    str = regexReplace(str, 'POSTCODECA', 'Canada postcode', '[abceghj-nprstvxyABCEGHJ-NPRSTVXY]{1}[0-9]{1}[abceghj-nprstv-zABCEGHJ-NPRSTV-Z]{1}[ ]?[0-9]{1}[abceghj-nprstv-zABCEGHJ-NPRSTV-Z]{1}[0-9]{1}')
    ### after all the more specific matches
    
    # Problem with chomping leading and training space
    str = regexReplace(str, ' USPHONE ', 'US phone', '(1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?)')
    str = regexReplace(str, 'USPHONE', 'US phone', '(\s|^)(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?(\s|$)')
    str = regexReplace(str, 'SSN', 'ssn', '(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}')
    str = regexReplace(str, 'UKPHONE', 'uk phone', '(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?')
    
    str = regexReplace(str, 'ACCOUNTNO', 'account number', '\d{5-12')
    return str
    
def getSubstituteText(key, type):
    return ""