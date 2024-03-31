import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
sound = AudioSegment.from_wav('output1.wav')

sound.export('myfile.mp3', format='mp3')

fs = 44100
seconds = 5
channels = 1

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

print("Recording audio...")
with sd.Stream(callback=audio_callback, channels=channels, samplerate=fs):
    sd.sleep(seconds * 1000)

print("Audio recording finished.")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output1.wav', fs, myrecording)  # Save as WAV file