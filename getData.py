import objectcreation as ob
import dateparsing as dp
import datetime as dt
import time


def takeSec(x):
    """key function for sort() function"""
    return x[1]

def totalTime():
    """returns total time doing all pomodoros of all kinds
returns int"""
    dbase = ob.dataBase()
    OBJECTS = dbase.obs

    t = []
    for i in OBJECTS:
        t.append(int(i.duration))

    return sum(t)

def sinceFirst():
    """returns days since first pomodoro"""
    dbase = ob.dataBase()
    OBJECTS = dbase.obs
    return int(dp.toSingleDay(time.localtime()))-int(dp.toSingleDay(dp.toStruct(OBJECTS[0].date)))


def inSecs(string):
    """Returns time expressed in string hh:nn:ss as int representing secods"""
    hours = int(string[0:2])
    minutes = int(string[3:5])
    secs = int(string[6:])
    return (hours*60*60)+(minutes*60)+secs


def timeFormat(seconds):
    """Turns secs into nice format.
takes: int
returns: string"""
    days = int(seconds/60/60/24)
    hours = int((seconds/60/60)%24)
    minutes = (seconds/60) % 60
    secs = (seconds) % 60
    formated = "%d days %02d:%02d:%02d" % (days, hours, minutes,secs)

    return formated

def pomsToday(date=time.strftime("%d/%m/%Y")):
    """Dictionary of poms done today."""
    t = ob.dataBase().getBy("date",date)

    d = dict()

    for i in t:
        d[i.code] = d.get(i.code,0)+int(i.duration)
        
    return d

def getWeekPoms(start=time.strftime("%d/%m/%Y")):
    """Returns histogram of everything done in last seven days
(including today)."""
    dates = []
    d = dict()
    for i in range(0,7):
        change = dt.datetime.strptime(start, "%d/%m/%Y") + dt.timedelta(days=-i)
        dates.append(pomsToday(change.strftime("%d/%m/%Y")))

    for i in dates:
        for key in i:
            d[key] = d.get(key,0)+i[key]

    return d

def weekAverage(d=getWeekPoms()):
    """Returns average worked last seven days."""
    return timeFormat(int((sum(d.values())*60)/7))[7:]

def fromCode(code):
    """returns all pomodoros of certain code
takes: string
returns: list"""
    dbase = ob.dataBase()
    OBJECTS = dbase.obs
    t = []
    for i in OBJECTS:
        if i.code == code:
            t.append(i)
            
    return t
    


def getPomTime(code):
    """Counts time spent in a pomodoro of a given code
takes: string
returns: int (minutes)."""

    t = ob.dataBase().getBy("code",code)
    
    count = 0
    for i in t:
        count += int(i.duration)
        
    return count

def longAgo(code):
    """Difference between date and today in days format."""
    date = fromCode(code)[-1].date
    return int(dp.toSingleDay(time.localtime()))-int(dp.toSingleDay(dp.toStruct(date)))


def pomLastTime(code):
    t = fromCode(code)
    return t[-1]

def allCodes():
    """returns list of strings, each one is a code, they're sorted for
appearences"""
    dbase = ob.dataBase()
    OBJECTS = dbase.obs
    
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

