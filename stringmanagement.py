import objectcreation as ob
import string

t=ob.OBJECTS

def pomDescriptions():
    """creates list of descriptions from all poms"""
    t = []

    for i in ob.OBJECTS:
        t.append(str(i.description))
        
    return t


def itemFreq():
    """counts frequencies of words.
takes :list
returns :dict"""
    

def punc_off(s):
    """take punctuation chars out of a string
takes : string
returns : sting"""
    for i in string.punctuation:
        s = s.replace(i,"")
    return s
        
def white_off(s):
    """takes whitespace out
takes: string
returns: string"""
    white = ["\t","\n","\r","\x0b","\x0c","\ufeff"]
    for i in white:
        s = s.replace(i,"")
    return s

def toWords(linelist):
    """transforms list of lines in lower-whitespace and punctuation free words
list -> list"""
    t = []

    for i in linelist:
        wordlist = i.split(" ")
        for word in wordlist:
            word = punc_off(white_off(word.lower()))
            if len(word) > 0:
                t.append(word)
    return t
