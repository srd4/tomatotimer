from objectcreation import OBJECTS
import matplotlib.pyplot as plt
from getData import *
import numpy as np
import time


#t = OBJECTS

def dates():
    """single list with all dates of poms"""
    dates = []
    for i in OBJECTS:
        dates.append(i.date)

    return dates

def toStruct(string):
    """takes date in format xx/xx/xxxx and turns it into struct format from
time module.
takes : str
returns : struc_time"""
    return time.strptime(string,"%d/%m/%Y")

def toSingleDay(struc):
    return time.strftime("%j",struc)
    

def toStr(struc):
    """struc_time date to string in format xx/xx/xxx"""
    return time.strftime("%d/%m/%Y",struc)

def fromSingleDay(string):
    """turns decimal day of the year and turns it into struct"""
    return time.strptime(string,"%j")
    

def pomDatesInSingleDays():
    """All dates in day of the year (repeated)
returns list"""
    t = []

    for i in OBJECTS:
        t.append(toSingleDay(toStruct(i.date)))

    return t

def datesByCode(code):
    """to get registered dates of a code
takes: string
returns: list"""
    t = []
    
    for i in OBJECTS:
        if i.code == code:
            t.append(toSingleDay(toStruct(i.date)))
    return t


def fillGaps(t):
    """returns dic with x thing made on each day since year started
included days in which did not do anything, datesByCode is helper
takes: list
returns: dict()"""
    registered = t
    d = dict()
    base = list(range(1,int(toSingleDay(time.localtime()))))

    for i in base:
        d[i] = 0

    for i in registered:
        d[int(i)] = d.get(int(i),0)+1
        
    return d

def pomTimeEachDay(code):
    """returns dictionary with time invested in code each day"""
    d = fillGaps([])
    t = []

    for i in OBJECTS:
        if i.code == code:
            t.append(i)
            
    for i in t:
        day = int(toSingleDay(toStruct(i.date)))
        d[day] = d.get(day,0)+int(i.duration)

    return d


            
def plotThem(t,codes):
    """takes a list of dictionaries and plots everything in there in same plot.
takes list"""

    count = 0
    for i in t:
        lists = sorted(i.items())
        x,y = zip(*lists)

        y2 = []#for comultive sum

        cumSum = 0
        for i in y:
            cumSum += i
            y2.append(cumSum/60)

        plt.plot(x[30:],y2[30:],label=codes[count])
        #plt.fill_between(x[30:],y2[30:],label=codes[count])
        count += 1
    plt.grid()
    plt.legend()
    plt.show()
    

def plotIt(d):
    """plots a dict()
takes dict()"""
    
    lists = sorted(d.items())
    x,y = zip(*lists)
    y2 = []#for comultive sum

    cumSum = 0
    for i in y:
        cumSum += i
        y2.append(cumSum)


    plt.grid()
    plt.plot(x,y)
    plt.show()

def plotPoms(codes):
    """to plot several pom codes dictionaries
takes: list (with codes)"""
    ts = []
    
    for i in codes:
        ts.append(fillGaps(datesByCode(i)))

    plotThem(ts,codes)
    

def plotTimes(codes):
    """plot duration vs days of several pom codes dictionaries
takes: list (of codes)"""

    ts = []

    for i in codes:
        ts.append(pomTimeEachDay(i))

    plotThem(ts,codes)

def getPomTimes():
    """Returns list of moments in which poms were registered."""
    t = []
    for i in OBJECTS:
        t.append(i.time)

    return t

def histTimes():
    """Counts how many poms have been done on each hour of the day."""
    d = dict()
    for i in getPomTimes():
        d[i[:2]] = d.get(i[:2],0)+1

    return d
        
        

        





    

    

        
