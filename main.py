from os import write
from win10toast import ToastNotifier
import time
import msvcrt
import csv
import os.path
import datetime

def Countdown():
  currentTime = str(datetime.datetime.now().time())
  #Required inputs
  Tm = int(input("Enter time in Minutes:"))
  Ts = int(input("Enter time in Seconds:"))
  dataEntry = [currentTime, currentTopic, "CountDown", Tm, Ts]
  Tm *= 60
  Time = Tm + Ts 

  #Countdown loop
  while  Time > 0:
    print(Time)
    Time-= 1
    time.sleep(1)

  #notification for the time up    
  toaster.show_toast("Alarm", "Time's up", icon_path ="Timer.ico")
  writer.writerow(dataEntry)

def Timer():
  currentTime = str(datetime.datetime.now().time())
  print("Timer has started! Press Esc to stop.")
  #Initialize time
  Time = 0
  #Timer loop
  while True:
    #End timer when pressed escape
    if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
      #Calculate Hours and Minutes
      if Time > 60:
        Tm = str(Time // 60)
        Ts = str(Time % 60)
        print("Stopped after " +Tm+ " minutes and " +Ts+ " seconds.")
        dataEntry = [currentTime, currentTopic, "Timer", Tm, Ts]
        writer.writerow(dataEntry)
        break
      #else print the Seconds
      else:
        print("Stopped after " + str(Time) + " seconds.")
        dataEntry = [currentTime, currentTopic, "Timer", "0", Time]
        writer.writerow(dataEntry)
        break
    Time += 1
    time.sleep(1)






#Initialize Toaster for notifications
toaster = ToastNotifier()

header = ["Time", "Assignment", "Mode", "Duration (min)", "Duration (sec)"]

if not os.path.isfile('Study Report.csv'):
  f = open('Study Report.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(header)

else:
  f = open('Study Report.csv', 'a')
  writer = csv.writer(f)
  
currentTopic = str(input("Enter task:"))

Countdown() 
