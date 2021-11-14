#Import necessary modules
import os 
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

  #Initialize dataEntry list for csv entry
  dataEntry = [currentTime, currentTopic, "CountDown", Tm, Ts]

  #Convert time in seconds 
  Tm *= 60
  Time = Tm + Ts 

  #Countdown loop
  while  Time > 0:
    print(Time)
    Time-= 1
    time.sleep(1)

  #notification for the time up    
  toaster.show_toast("Alarm", "Time's up", icon_path ="Timer.ico")

  #write the data in csv
  writer.writerow(dataEntry)


def Timer():
  Time = 0
  currentTime = str(datetime.datetime.now().time())
  print("Timer has started! Press Esc to stop.")

  #Timer loop
  while True:
    Time += 1
    time.sleep(1)

    #End timer when pressed escape
    if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
      #Calculate Minutes and Seconds
      if Time > 60:
        #Convert seconds into minutes and seconds
        Tm = str(Time // 60)
        Ts = str(Time % 60)

        print("Stopped after " +Tm+ " minutes and " +Ts+ " seconds.")

        #Initialize dataEntry list for csv entry
        dataEntry = [currentTime, currentTopic, "Timer", Tm, Ts]
        #write the data in csv and break the loop
        writer.writerow(dataEntry)
        break

      else:
        print("Stopped after " + str(Time) + " seconds.")

        #Initialize dataEntry list for csv entry
        dataEntry = [currentTime, currentTopic, "Timer", "0", Time]
        #write the data in csv and break the loop
        writer.writerow(dataEntry)
        break

def Stats():
  f = open("Study Report.csv", 'r')
  reader = csv.DictReader(f)
  totalTime = 0
  for row in reader:
    Time = int(row["Duration (sec)"])
    totalTime += Time
  print(totalTime)
    

#Initialize Toaster for notifications
toaster = ToastNotifier()

#Create the csv and add the header if the csv doesn't exists
if not os.path.isfile('Study Report.csv'):
  f = open('Study Report.csv', 'w')
  writer = csv.writer(f)
  header = ["Time", "Assignment", "Mode", "Duration (min)", "Duration (sec)"]
  writer.writerow(header)

#else open in append mode
else:
  f = open('Study Report.csv', 'a')
  writer = csv.writer(f)

mode = int(input("mode:"))
currentTopic = str(input("Enter task:"))

if mode == 0:
  Stats()
elif mode == 1:
  Countdown()
else:
  Timer()