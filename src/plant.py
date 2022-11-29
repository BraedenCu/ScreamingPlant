import bluetooth
from subprocess import call

def connectTarget():
    target_name = "BluetoothSpeaker"
    target_addr = None
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break
    if target_addr is not None:
        #target found
        return true
    else:
        #target not found
        return false

def playSound(fileAddress):
    basecmd = ["mplayer", "-ao", "alsa:device=bluetooth"]
    call(basecmd + [fileAddress])


if __name__ == "__main__":
    if connectTarget():
        playSound()
    else:
        print("unable to connect too a blue tooth device")
