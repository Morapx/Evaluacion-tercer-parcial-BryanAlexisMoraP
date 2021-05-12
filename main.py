import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source: 
        if ask: 
            alexa_speak(ask)         
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        
        except sr.UnknownValueError:
            alexa_speak('que?')
        except sr.UnknownValueError:
            alexa_speak('auxilio, no me funciona')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('Mi nombre es Matrix')
    if 'que hora es' in voice_data:
        alexa_speak(ctime())
    if 'buscar' in voice_data:
        buscar = record_audio('¿Que artista, genero o podcast te gustaria buscar te interesa escuchar?')
        url = 'https://open.spotify.com/search/' + buscar
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para: ' + buscar)
    if 'canciones' in voice_data:
        canciones = record_audio("¿Habro tu biblioteca?")
        url = 'https://open.spotify.com/collection/playlists' 
        webbrowser.get().open(url)
        alexa_speak('Abriendo biblioteca' + canciones)
    if 'termina' in voice_data:
        exit()
    
time.sleep(1)
alexa_speak('¿Que te apetece escuchar hoy?')
while 1:
    voice_data = record_audio()
    respond(voice_data)