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
    with