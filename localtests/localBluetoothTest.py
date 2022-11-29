import bluetooth
from subprocess import call
from sh import bluetoothctl

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
        return target_addr
    else:
        #target not found
        return None

#home/dev/music/output.avi
def playSound(fileAddress):
    fileAddress = "home/dev/music/output.avi"
    basecmd = ["mplayer", "-ao", "alsa:device=bluetooth"]
    call(basecmd + [fileAddress])

if __name__ == "__main__":
    addr = connectTarget()
    if addr != None:
        print(addr)
        bluetoothctl("connect", addr)
    else:
        print("unable to connect too a bluetooth device")
