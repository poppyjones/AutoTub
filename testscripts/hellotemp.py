from datetime import datetime
import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)

#f = open("tempLog.txt", "a")
#f.write("Hello! This script was called: ")
#f.write(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
#f.write("   The temperature was: {0:0.3f}C\n".format(sensor.temperature))
#f.close()

print("   The temperature is: {0:0.3f}C\n".format(sensor.temperature))


input()