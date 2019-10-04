import auxFunctions as af

def getFile():
    """Returns list of all lines of poms in history file."""
    with open("tomato_history.csv","r", encoding="utf-8") as file:
        data = file.readlines()
        t = []

        for i in data:
            t.append(i.replace("\n","").split(";"))

        return t

class pom:
    """Pomodoro objects, initiates with its data."""
    def __init__(self,t):
        self.time = af.cleanString(t[0])
        self.date = af.cleanString(t[1])
        self.description = af.cleanString(t[2])
        self.code = af.cleanString(t[3])
        self.duration = af.cleanString(t[4])

class dataBase:
    """Created once. Used to apply methods to all poms."""
    def __init__(self):
        self.obs = self.create()

    def getBy(self, attribute, required):
        """Returns all objects that match atribute and requirement.
takes: string, string
returns: list."""
        t = []
        for i in self.obs:
            if getattr(i,attribute) == required:
                t.append(i)
        return t
            
    def create(self):
        """Crates pom objects."""
        t = getFile()
        obs = []

        for i in t:
            obs.append(pom(i))

        return obs

dbase = dataBase()
OBJECTS = dbase.obs
