# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

# pylint: disable=unused-import
import time
import board
# import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C


reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
# i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
# pm25 = PM25_I2C(i2c, reset_pin)
import csv

pm_data = open("pm25_data.csv",'w', newline = None)
csvwriter = csv.writer(pm_data,delimiter = ',')
csvwriter.writerow(["Time","PM 1.0 Standard Conc.","PM 2.5 Standard Conc.","PM 10 Standard Conc.", 
                    "Particles > 0.3um / 0.1L air:", "Particles > 0.5um / 0.1L air:", 
                    "Particles > 1.0um / 0.1L air:","Particles > 2.5um / 0.1L air:",
                    "Particles > 5.0um / 0.1L air:","Particles > 10 um / 0.1L air:"])
aqdata=pm25.read()
for i in range(60):

    timestamp = time.time()

    PM1stan = aqdata["pm10 standard"]
    PM2_5stan = aqdata["pm25 standard"]
    PM10stan = aqdata["pm100 standard"]

    PM1envr = aqdata["pm10 env"]
    PM2_5envr = aqdata["pm25 env"]
    PM10envr = aqdata["pm100 env"]

    um03 = aqdata["particles 03um"]
    um05 = aqdata["particles 05um"]
    um10 = aqdata["particles 10um"]
    um25 = aqdata["particles 25um"]
    um50 = aqdata["particles 50um"]
    um100 = aqdata["particles 100um"]
    csvwriter.writerow([timestamp,PM1stan,PM2_5stan,PM10stan,PM1envr,PM2_5envr,PM10envr,um03,um05,um10,um25,um50,um100])
    time.sleep(1)
pm_data.close()