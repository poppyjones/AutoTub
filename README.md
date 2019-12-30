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

    alias python='/usr/bin/python3.7'

### Test scripts

To test the different hardware components ~~and to figure out how different python libraries work~~ I wrote a few simple test scripts that can be found in the testscripts directory. At the time of writing most of these still leave messy log files all over the place.

### Temperature

To set up the temperature sensor and whatnot follow [these](<https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier>) instructions, skipping the section "Wiring and testing". Remember to enable **SPI** on the Pi, skip the example code and use hellotemp.py to check that is is working. We followed their example and used **GPIO 5**, so do remember to modify code if this changes.

### Relay board

The installation guide for the relay board an by found in [this](<https://github.com/modmypi/PiOT-Relay-Board/wiki>) wiki. The example code is a bit much tbh, although i guess it may be useful if you are using more than one relay. Currently the code assumes that the relay is connected to **GPIO 17** (pin 11).

Note: it seems like different relays have different defaults. When connected to **GPIO 6** the the relay stayed on even after the Pi powered down, when connected to 17 this is not an issue.

### CRONTAB scheduling

So ensure the hottub.py script runs even if there is a short power cut I used the crontab to run the script on reboot.

Enter the crontab by typing:

    crontab -e

Add the line

    @reboot /usr/bin/python3.7 home/pi/Autotub/hottub.py

### Desktop icons

Desktop icons can be added to the Raspberry Pi to make AutoTub a bit more user friendly for normal people.
The icons are [Material Design Icons](https://material.io/resources/icons/?style=baseline).

#### How to  add desktop icons

- Open the desktopicons folder in AutoTub  
- Move all .desktop files to the desktop.
- Press `ctr+alt+t` and copy-paste the text from setup.txt into the terminal window
- To remove pop up when clicking icon
  - File manager
  - Edit
  - Preferences
  - General
  - Tick *Do not ask option on executable launch*
- Click the icon marked test. An window should open with a success message
  - if this does not happen, call me
- Finally you can delete the test icon

## Notes & WIP

- It seems to take roughly 30 mins to raise the temperature of the tub by a degree
- The temperatures vary by roughly a degree minute to minute
  - this may be due to the current placement of the censor and my be improved once it is placed in the heating element
- Consider remote interface.
