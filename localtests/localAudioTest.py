import pygame
from subprocess import call

def setup(audio_file_address):
    # Initialize Pygame
    pygame.init()

    # Set the window title
    pygame.display.set_caption("Play Sound from File")

    # Set the window size
    pygame.display.set_mode((400, 300))

    # Load the audio file
    audio_file_object = pygame.mixer.Sound(audio_file_address)
    
    return audio_file_object

def playSound(audio_file_object):
    # Play the audio file
    audio_file_object.play()

    # Wait for the sound to finish playing
    while pygame.mixer.get_busy():
        pygame.time.delay(100)

def main(): 
    audio_file_address = "../audio/dogbark.mp3"
    audio_file_object = setup(audio_file_address)
    playSound(audio_file_object)

if __name__=="__main__":
    main()