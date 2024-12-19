import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_file = 'over-radio-countdown_108bpm_A_minor.wav'
FILE_FROM_USER = 'RECORDING.wav'
VOICE_FILE = 'VOICE.txt'

r = sr.Recognizer()

def recognize_speech_from_file(filename):
    # open file
    with sr.AudioFile(filename) as source:
        # listen for audio and load to memory
        audio = r.record(source)
        text = r.recognize_google(audio)
        return text

def record_audio(filename):
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    myrecording = sd.rec(seconds * fs, samplerate=fs, channels=1, dtype='int32')
    sd.wait()  # Wait until recording is finished
    print("Recording saved")
    sd.play(myrecording, fs)
    sd.wait()
    print("Recording played", end="")
    wav.write(filename, fs, myrecording)

def save_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


def main():
    # print(recognize_speech_from_file(test_file))
    print("Please record your voice for 5 seconds")
    record_audio(FILE_FROM_USER)
    voice_to_text = recognize_speech_from_file(FILE_FROM_USER)
    save_to_file(voice_to_text, VOICE_FILE)

if __name__ == "__main__":
    main()