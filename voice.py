import sounddevice as sd
import wavio

from pydub import AudioSegment
sound = AudioSegment.from_wav('myfile.wav')

sound.export('myfile.mp3', format='mp3')

folder = "Data/Smile"
counter = 0


duration = 15
samplerate = 44100
channels = 1

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

print("Recording audio...")
with sd.Stream(callback=audio_callback, channels=channels, samplerate=samplerate):
    sd.sleep(duration * 1000)

print("Audio recording finished.")

