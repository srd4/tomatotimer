class pom:
    def __init__(self,t):
        self.time = t[0]
        self.date = t[1]
        self.description = t[2]
        self.code = t[3]
        self.duration = t[4]



def getFile():
    """returns list of all lines of poms in history file"""
    with open("tomato_history.csv","r") as file:
        data = file.readlines()
        t = []

        for i in data:
            t.append(i.replace("\n","").split(";"))

        return t

def createObjects():
    """makes pom objects"""
    t = getFile()
    obs = []

    for i in t:
        obs.append(pom(i))

    return obs

global OBJECTS
OBJECTS = createObjects()
