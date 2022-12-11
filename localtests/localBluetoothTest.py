import bluetooth
from subprocess import call
from sh import bluetoothctl
import pygame
from subprocess import call

def connectTarget():
    target_name = "Family Room speaker"
    target_addr = None
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
        name = bluetooth.lookup_name( bdaddr )
        print(bdaddr)
        print(name)
        if(name != None):
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
def playSound(audioFiles):
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()  
    cmd = ["mplayer", "-ao", "alsa:device=bluetooth", audioFiles[0]]
    call(cmd)
    #mixer.music.pause()	
    #mixer.music.unpause()
    #mixer.music.stop()

def setup(fileAddr):
    pygame.mixer.init()
    pygame.mixer.music.load(fileAddr[0])


def main(audio):
    addr = connectTarget()
    audioFiles = audio

    if addr != None:
        bluetoothctl("connect", addr)
    else:
        print("unable to connect too a bluetooth device")

    playSound(audioFiles)


if __name__ == "__main__":
    fileAddressArr = ["../audio/dogbark.mp3"]
    setup(fileAddressArr)
    main(fileAddressArr)
