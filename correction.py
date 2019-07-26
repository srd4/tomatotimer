def loadAndCorrect():
    """to correct technical debt"""
    with open("tomato_history.csv","r") as file:
        data = file.readlines()
        t = []
        new_t = []

        for i in data:
            t.append(i.replace("\n","").split(";"))

        for i in t[:142]:
            i.append("25")
        for i in t[142:458]:
            i.append("30")
        for i in t[458:]:
            i.append("20")
            
        return t

def write_correction(t):
    """write correction in file"""
    string = ""
    for i in t:
        string += i[0]+";"+i[1]+";"+i[2]+";"+i[3]+";"+i[4]+"\n"
    
    with open("csvdata_corrected.csv","w", encoding="utf-8") as file:
        file.write(string)
        
def fullCorrect():
    """automatic correction of the pom history file. Correction is to put
values of time spent in pomodoro at the end of each line"""
    write_correction(loadAndCorrect())









