import bluetooth
from subprocess import call
from sh import bluetoothctl
import pygame


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
def playSound(files):
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()  
    #mixer.music.pause()	
    #mixer.music.unpause()
    #mixer.music.stop()

def setup():
    pygame.mixer.init()
    pygame.mixer.music.load('../audio/audio.mp3')


def main(audio):
    addr = connectTarget()
    audioFiles = audio

    if addr != None:
        bluetoothctl("connect", addr)
        playSound(audioFiles)
    else:
        print("unable to connect too a bluetooth device")


if __name__ == "__main__":
    setup()
    fileAddressArr = ["./audio/audio.mp3"]
    main(fileAddressArr)
