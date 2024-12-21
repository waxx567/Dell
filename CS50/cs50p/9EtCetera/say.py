import cowsay
import pyttsx3

"""Initialize library for text to speech"""
engine = pyttsx3.init()
# prompt user and store in variable
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()