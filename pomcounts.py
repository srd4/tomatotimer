import objectcreation as ob

t = ob.OBJECTS

def countPom(string):
    """counts number of pomodoros with code (string)
takes: string
returns: int"""
    count = 0
    for i in ob.OBJECTS:
        if i.code == string:
            count += 1

    return count

def timeFormat(seconds):
    hours = int((seconds/60/60))
    minutes = (seconds/60) % 60
    secs = (seconds) % 60
    this = "%02d:%02d:%02d" % (hours, minutes,secs)

    return this
    

def pomTime(string):
    """Counts duration of all code (string) pomodoros. Returns seconds.
takes : count
returns : int"""
    count = 0
    for i in ob.OBJECTS:
        if i.code == string:
            count += int(i.duration)*60

    return count
      
    
    
        
