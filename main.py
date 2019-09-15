import objectcreation as ob
import getData
import gsheet
import time
import vlc
import os



global currentPath
currentPath = os.getcwd()+"\\"
ms = vlc.MediaPlayer(currentPath+"song.mp3")


def countDown(secs):
    """Counts from secs to cero one at a time
takes : int"""
    for i in range(secs,0,-1):
        minutes = int(i/60)
        seconds = (i%60)
        print("%02d:%02d"%(minutes,seconds),end="\r")
        time.sleep(1)
    ms.play()
    return 1

def record(s,code):
    """appends pom in file"""
    pomsDuration = 20
    description = s
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%Y")
    separation = ";"

    f = open(currentPath+"tomato_history.csv","a")
    f.write("\n"+hour+separation+date+separation+description+separation+code+separation+str(pomsDuration))
    f.close
    

def to_do():

    OBJECTS = ob.createObjects()
	
    """User interface and main inputs"""
    average = round((getData.totalTime()/60)/getData.sinceFirst(),3)

    print("\nYou have made",len(OBJECTS),"pomodoros, that is",int(getData.totalTime()/60),"hours or",getData.timeFormat(getData.totalTime()*60),"hours of productive, focused work. In average",str(getData.timeFormat(average*60*60))[7:],"hours per day in",getData.sinceFirst(),"days.\n")
    
    print("So, what the hell you want to do now, buddy?")
    #res is short for response.
    res = input("1. Pomodoro. \n2. Short Break. \n3. Long Break.\n4. Quit.\n\n> ")
    if res == "1":
        ms.stop()
        do = input("Describe what you are about to do mate:\n> ")
        code = input("What's the code of this activity?\n> ")
        if getData.getPomTime(code) != 0:
            print("You have worked on",code,"for",getData.timeFormat(getData.getPomTime(code)*60),"hours","("+str(len(getData.fromCode(code)))," pomodoros or",int(getData.getPomTime(code)/60),"total hours). "+"The last time you worked on",code,"was in",getData.pomLastTime(code).date,"or",getData.longAgo(code),"days ago.","\n")
        else:
            print("This is your first time working on",code)
        if countDown(1200):
            try:
                record(do,code)
                sheetThread = threading.Thread(target=gsheet.updatePoms, args=(ob.createObjects(),))
                sheetThread.start()
            except:
                pass
    elif res == "2":
        ms.stop()
        countDown(300)
    elif res == "3":
        ms.stop()
        countDown(600)
    elif res == "4":
        quit()

if __name__=="__main__":
    while True:
        os.system("cls")
        to_do()
