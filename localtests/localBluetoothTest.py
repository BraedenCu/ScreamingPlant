import bluetooth
from subprocess import call

def connectTarget():
    target_name = "Bose QC35 II"
    target_addr = None
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break
    if target_addr is not None:
        #target found
        return True
    else:
        #target not found
        return False

#home/dev/music/output.avi
def playSound(fileAddress):
    fileAddress = "home/dev/music/output.avi"
    basecmd = ["mplayer", "-ao", "alsa:device=bluetooth"]
    call(basecmd + [fileAddress])


if __name__ == "__main__":
    if connectTarget():
        playSound()
    else:
        print("unable to connect too a blue tooth device")
