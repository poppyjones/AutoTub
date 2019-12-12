# AutoTub

Scripts to help an outdoor hot tub survive the vicious winters of Scotland

## What did we do?

Basic step by step so I don't forget how this works..

### Hardware

- Raspberry Pi 4 Model B
- Temperature sensor thingy
  - Three wire temperature sensor? (water proof)
  - Amplifier was [MAX31856](<https://www.adafruit.com/product/3263>)
- Relay
  - [ModMyPi PiOT Relay Board](<https://thepihut.com/products/modmypi-piot-relay-board>)

### Raspberry Pi setup

The Raspberry Pi used for this project is the **Raspberry Pi 4 Model B** running **Raspian** from [here](<https://www.raspberrypi.org/downloads/noobs/>).

The default python version is set to 3.7 with:

    alias python='/usr/bin/python3.4'

### Test scripts

To test the different hardware components ~~ and to figure out how different python libraries work ~~ I wrote a few simple test scripts that can be found in the testscripts directory. At the time of writing most of these still leave messy log files all over the place.

### Temperature

To set up the temperature sensor and whatnot follow [these](<https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier>) instructions, skipping the section "Wiring and testing". Remember to enable **SPI** on the Pi, skip the example code and use hellotemp.py to check that is is working. We followed their example and used **GPIO 5**, so do remember to modify code if this changes.

### Relay board

The installation guide for the relay board an by found in [this](<https://github.com/modmypi/PiOT-Relay-Board/wiki>) wiki. The example code is a bit much tbh, although i guess it may be useful if you are using more than one relay. Currently the code assumes that the relay is connected to **GPIO 17** (pin 11). 
Note: it seems like different relays have different defaults. When connected to **GPIO 6** the the relay stayed on even after the Pi powered down, when connected to 17 this is not an issue.

### CRONTAB scheduling

So ensure the hottub.py script runs even if there is a short power cut I used the crontab to run the script on reboot.

Enter the crontab with:

    crontab -e

Add the line

    @reboot /usr/lib/python3.7 /Autotub/hottub.py
