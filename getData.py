import objectcreation as ob
import dateparsing as dp
import time


def takeSec(x):
    """key function for sort() function"""
    return x[1]

def totalTime():
    """returns total time doing all pomodoros of all kinds
returns int"""
    OBJECTS = ob.createObjects()
    t = []
    for i in OBJECTS:
        t.append(int(i.duration))

    return sum(t)


def sinceFirst():
    """returns days since first pomodoro"""
    OBJECTS = ob.createObjects()
    return int(dp.toSingleDay(time.localtime()))-int(dp.toSingleDay(dp.toStruct(OBJECTS[0].date)))


def inSecs(string):
    """turns time expressed in string as hh:nn:ss on int representing secods"""
    hours = int(string[0:2])
    minutes = int(string[3:5])
    secs = int(string[6:])
    return (hours*60*60)+(minutes*60)+secs


def timeFormat(seconds):
    """turns secs in nice format
takes: int
returns: string"""
    days = int(seconds/60/60/24)
    hours = int((seconds/60/60)%24)
    minutes = (seconds/60) % 60
    secs = (seconds) % 60
    formated = "%d days %02d:%02d:%02d" % (days, hours, minutes,secs)

    return formated


def fromCode(code):
    """returns all pomodoros of certain code
takes: string
returns: list"""
    OBJECTS = ob.createObjects()
    t = []
    for i in OBJECTS:
        if i.code == code:
            t.append(i)
            
    return t

def getPomTime(code):
    """counts time spent in a pomodoro of a given code
takes: string
returns: int (minutes)"""
    poms = fromCode(code)
    t = 0
    for i in poms:
        t += int(i.duration)
        
    return t

def longAgo(code):
    """difference between date and today in days format"""
    date = fromCode(code)[-1].date
    return int(dp.toSingleDay(time.localtime()))-int(dp.toSingleDay(dp.toStruct(date)))


def pomLastTime(code):
    t = fromCode(code)
    return t[-1]

def allCodes():
    """returns list of strings, each one is a code, they're sorted for
appearences"""
    OBJECTS = ob.createObjects()
    d = dict()
    tuplesList = []
    sortedCodes = []
    
    
    for i in OBJECTS:
        d[i.code] = d.get(i.code,0)+1

    for i in d:
        tuplesList.append((i,d[i]))

    tuplesList.sort(key=takeSec,reverse=True)

    for i in tuplesList:
        sortedCodes.append(str(i[0]))

    return sortedCodes
        

def inSecs(string):
    """turns time expressed in string as hh:nn:ss on int representing secods"""
    hours = int(string[0:2])
    minutes = int(string[3:5])
    secs = int(string[6:])
    return (hours*60*60)+(minutes*60)+secs









