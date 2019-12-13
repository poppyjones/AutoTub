import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)

def current_temperature():
    t = sensor.temperature
     #if the sensor is unplugged the output is -242.020, but if it is -50 theres probable something wrong anyway..
    if(t < -50):
        raise Exception("Sensor input error! Check wiring and reboot")
    return t