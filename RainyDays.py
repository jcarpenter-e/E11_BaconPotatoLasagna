import adafruit_bme680

print("Starting Measurements!")

import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25
timelimit = 0

while timelimit != 20:
	print("\nTemperature: %0.1f C" % bme680.temperature)
	print("Gas: %d ohm" % bme680.gas)
	print("Humidity: %0.1f" % bme680.relative_humidity)
	print("Pressure: %0.3f hPa" % bme680.pressure)
	print("Altitude = %0.2f meters" % bme680.altitude)
	countdown = 20-timelimit
	print("Time limit is",countdown)
	timelimit = timelimit+1
	time.sleep(2)
print("Done!!")
