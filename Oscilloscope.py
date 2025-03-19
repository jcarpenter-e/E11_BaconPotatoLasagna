import RPi.GPIO as GPIO
import datetime
import time
import sys
import csv

channel = 11 
def my_callback(channeln):
    if GPIO.input(channeln) == GPIO.LOW:
        print('Event Detected at ' + str(datetime.datetime.now()))
        return True
    else:
        return False

GPIO.add_event_detect(channel, GPIO.FALLING)  # add rising edge detection on a channel

if len(sys.argv) < 2:
    print("This script requires an input argument specifying the run time in seconds")
    exit()
else:
    timelimit = int(sys.argv[1])
counttime = 0

filename = str(sys.argv[2]) + ".csv"
mobiledata = open(filename,'w', newline = None)
csvwriter = csv.writer(mobiledata,delimiter = ',')
csvwriter.writerow()


count = 0
while counttime < timelimit:
    counttime += 1
    if my_callback(channel) == True:
        count += 1

    