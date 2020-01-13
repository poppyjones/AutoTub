from w1thermsensor import W1ThermSensor
sensor = sensor = W1ThermSensor()

def current_temperature():
    t = sensor.get_temperature()
     #if the sensor is unplugged the output is -242.020, but if it is -50 theres probable something wrong anyway..
    if(t < -50):
        raise Exception(str(t)+"C: Sensor input error! Check wiring and reboot")
    return t