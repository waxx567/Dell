import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_file = 'over-radio-countdown_108bpm_A_minor.wav'

# FILE_FROM_USER = 'RECORDING.wav'
# VOICE_FILE = 'VOICE.wav'

r = sr.Recognizer()

def recognize_speech_from_file(filename):
    # open file
    with sr.AudioFile(filename) as source:
        # listen for audio and load to memory
        audio = r.record(source)
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        return text

# def record_audio():
#     fs = 44100  # Sample rate
#     seconds = 5  # Duration of recording
#     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
#     sd.wait()  # Wait until recording is finished
#     wav.write(VOICE_FILE, fs, myrecording)
#     return myrecording

def main():
    # record_audio()
    result = recognize_speech_from_file(test_file)
    print(result)
    # return result

if __name__ == "__main__":
    main()