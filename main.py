import objectcreation as ob
import dateparsing as dp
import threading
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
    return True

def record(s,code):
    """Appends pom in file"""
    t = [time.strftime("%H:%M:%S"),time.strftime("%d/%m/%Y"),s,code,"20"]
    
    f = open(currentPath+"tomato_history.csv","a")
    text = "\n"
    
    for i in t:
        if i != t[-1]:
            text += i+";"
        else:
            text += i
            
    f.write(text)
    f.close
    

def to_do():

    dbase = ob.dataBase()
    OBJECTS = dbase.obs

	
    """User interface and main inputs"""
    average = round((getData.totalTime()/60)/getData.sinceFirst(),3)

    print("\nYou have made",len(OBJECTS),"pomodoros, that is",int(getData.totalTime()/60),"hours or",getData.timeFormat(getData.totalTime()*60),"hours of productive, focused work. Your average this week is",getData.weekAverage(),"hours a day. And started",getData.sinceFirst(),"days ago.\n")

    done = getData.pomsToday()
    print("\nToday you have done:",done,"\n")

    
    
    print("So, what the hell you want to do now, buddy?")
    #Response.
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
                sheetThread = threading.Thread(target=gsheet.updatePoms, args=(ob.OBJECTS,))
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
    elif res == "plotWeek":
        dp.plotIt(getData.getWeekPoms())
    elif res == "plotToday":
        dp.plotIt(getData.pomsToday())

if __name__=="__main__":
    while True:
        os.system("cls")
        to_do()
