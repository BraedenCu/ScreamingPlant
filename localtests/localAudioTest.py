from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("../audio/dogbark.mp3")
play(song)