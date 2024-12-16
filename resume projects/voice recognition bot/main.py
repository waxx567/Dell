import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_file = ''

FILE_FROM_USER = 'RECORDING.wav'
VOICE_FILE = 'VOICE.wav'

r = sr.Recognizer()

def recognize_speech_from_file(filename):
    # open file
    with sr.AudioFile(filename) as source:
        # listen for audio
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            