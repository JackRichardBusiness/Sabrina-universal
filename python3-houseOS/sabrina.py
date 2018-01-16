try:
    from firebase import firebase
    import speech_recognition as sr
    import time
    import pygame
    from time import sleep
    print("LOG: Imports successful")
except:
    print("LOG: Imports installing")
    os.system('pip3 install pygame')
    pygame.mixer.music.load("houseOS-preset1c")
    pygame.mixer.music.play()
    import os
    os.system('pip3 install SpeechRecognition')
    os.system('sudo apt-get install -y python3-pyaudio')
    print("LOG: Running again...")
    os.system('python3 sabrina.py')
def callback(recognizer, audio):
    try:
        output = recognizer.recognize_google(audio)
        if output == "hey Sabrina":
            pygame.mixer.music.load("houseOS-preset1a.mp3")
            pygame.mixer.music.play()
            sleep(1)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
            print("ERROR: "+str(e))
            pygame.init()
            pygame.mixer.music.load("houseOS-preset1c.mp3")
            pygame.mixer.music.play()
            sleep(1)
pygame.mixer.init()
pygame.mixer.music.load("houseOS-preset1a.mp3")
pygame.mixer.music.play()
##r = sr.Recognizer()
##m = sr.Microphone()

##while True:
##	database = firebase.FirebaseApplication('https://sabrina-415a1.firebaseio.com/')
##	inputstr = input('>>> ')
##	output = database.get('conversation/', inputstr)
##	if output == None:
##		print("Sorry, I didn't get that.")
##		database.put('unknown/', inputstr, '?')
##	else:
##		print(output)
