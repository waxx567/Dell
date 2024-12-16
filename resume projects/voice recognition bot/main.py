import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_file = 'over-radio-countdown_108bpm_A_minor.wav'

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

def record_audio():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wav.write(VOICE_FILE, fs, myrecording)
    return myrecording

def main():
    record_audio()
    result = recognize_speech_from_file(VOICE_FILE)
    print(result)
    return result

if __name__ == "__main__":
    main()