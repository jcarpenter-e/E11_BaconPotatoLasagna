import time
import board
import busio
import csv
import sys
from digitalio import DigitalInOut, Direction, Pull

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

import adafruit_bme680

##### Code

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25
if len(sys.argv) < 2:
    print("This script requires an input argument specifying the run time in seconds")
    exit()
else:
    timelimit = int(sys.argv[1])
ctime = 0

mobiledata = open("BME680_PM25.csv",'w', newline = None)
csvwriter = csv.writer(mobiledata,delimiter = ',')
csvwriter.writerow(["Time","PM 1.0 Standard Conc.","PM 2.5 Standard Conc.","PM 10 Standard Conc.",
                    "Particles > 0.3um / 0.1L air:", "Particles > 0.5um / 0.1L air:",
                    "Particles > 1.0um / 0.1L air:", "Particles > 2.5um / 0.1L air:",
                    "Particles > 5.0um / 0.1L air:", "Particles > 10 um / 0.1L air:",
                    "Temperature","Gas","Humidity","Pressure","Altitude"])

while ctime < timelimit:
    ctime +=1
    aqdata = pm25.read()

    timestamp = time.time()

    PM1stan = aqdata["pm10 standard"]
    PM2_5stan = aqdata["pm25 standard"]
    PM10stan = aqdata["pm100 standard"]

    um03 = aqdata["particles 03um"]
    um05 = aqdata["particles 05um"]
    um10 = aqdata["particles 10um"]
    um25 = aqdata["particles 25um"]
    um50 = aqdata["particles 50um"]
    um100 = aqdata["particles 100um"]

    temp = round(bme680.temperature,2)
    gas = round(bme680.gas,2)
    humid = round(bme680.humidity,2)
    pressure = round(bme680.pressure,2)
    altitude = round(bme680.altitude,2)

    csvwriter.writerow([timestamp,PM1stan, PM2_5stan, PM10stan,um03,um05,um10,um25,um50,um100,temp,gas,humid,pressure,altitude])
    time.sleep(1)
mobiledata.close()