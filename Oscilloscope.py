import RPi.GPIO as GPIO
import datetime
import time
import sys
import csv

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
def my_callback(channeln):
    print('Event Detected at ' + str(datetime.datetime.now()))
    global count 
    count += 1

GPIO.add_event_detect(11, GPIO.FALLING, callback= my_callback)  # add rising edge detection on a channel

timelimit = int(sys.argv[1])
counttime = 0

filename = str(sys.argv[2]) + ".csv"
mobiledata = open(filename,'w', newline = None)
csvwriter = csv.writer(mobiledata,delimiter = ',')
csvwriter.writerow("Counts in the Last Minute")

while counttime < timelimit:
    counttime += 1
    csvwriter.writerow([count])
    count = 0
    time.sleep(60)
mobiledata.close()