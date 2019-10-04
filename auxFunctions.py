import string
import os

def cleanString(aString):
    """Returns same string without garbage characters."""
    garbage = ["\t","\n","\r","\x0b","\x0c", "\ufeff"]
    newString = aString
    for i in garbage:
        if i in aString:
            newString = newString.replace(i,"")
            
    return newString


def hasLetters(aString):
    """Checks if a string has letters."""
    for i in string.ascii_lowercase:
        if(i in aString.lower()):
            return True
    return False


def isDate(line):
    """Recognizes if a line is a date."""
    if(8 <= len(line) <= 10) and ("/" in line or "-" in line) and hasLetters(line) == False:
        return True
    return False



def isTime(line):
    """Checks if line is a time in HH:MM XM format"""
    chars = ":m"
    charCount = 0
    numCount = 0
    
    for i in chars:
        if i in line:
            charCount += 1

    for i in line:
        if i in string.digits:
            numCount += 1

    if 5 < len(line) < 9 and charCount == 2 and 3 <= numCount <= 4 and ("a" in line or "p" in line):
        return True
    return False

def dateFormat(date):
    """Changes date in dd-mm-aaa format to dd/mm/aaa.
takes/returns: string"""
    digits = date.split("-")
    newDate = ""

    for i in digits:
        newDate += "/"+i

    return newDate[1:]


def hist(aString):
    d = dict()
    forbidden = "1234567890/()?!#$%&\,.;- "
    
    for i in aString.lower():
        if i not in forbidden:
            d[i] = d.get(i,0)+1
    return d
    

def dicToTuple(d):
    a,b,c,d,e = d.values()

    return (a,b,c,d,e)






    

