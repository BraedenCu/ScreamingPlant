import bluetooth
from subprocess import call
from sh import bluetoothctl
import time
import board
from adafruit_seesaw.seesaw import Seesaw


def connectTarget():
    target_name = "Bose QC35 II"
    target_addr = None
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
        name = bluetooth.lookup_name( bdaddr )
        print(bdaddr)
        print(name)
        if(name == target_name):
            target_addr = bdaddr
            break

    if target_addr is not None:
        #target found
        print("Target Found: " + target_addr)
        return target_addr
    else:
        #target not found
        return None

#home/dev/music/output.avi
def playSound(files):
    fileAddress = files[0]
    basecmd = ["mplayer", "-ao", "alsa:device=bluetooth"]
    call(basecmd + [fileAddress])

def readPlantData():
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    return touch

def main(audio, moistureThreshhold):
    addr = connectTarget()
    audioFiles = audio

    if addr != None:
        bluetoothctl("connect", addr)
    else:
        print("unable to connect too a bluetooth device")

    while(True):
        moistureLevel = readPlantData()
        if (moistureLevel < moistureThreshhold):
            playSound(audioFiles[0])


if __name__ == "__main__":
    i2c_bus = board.I2C()
    ss = Seesaw(i2c_bus, addr=0x36)
    moistureThreshhold = 0.5
    fileAddressArr = ["home/dev/music/output.avi"]
    main(fileAddressArr, moistureThreshhold)
