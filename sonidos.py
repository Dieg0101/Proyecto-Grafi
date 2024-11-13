import pygame as py

py.init()
py.mixer.init()

def play(filename):
    audio = filename
    py.mixer.music.load(audio)
    py.mixer.music.play()
    
def stop():
    py.mixer.music.stop()

def sonido_musica(FileName):
    py.mixer.music.load(FileName)
    py.mixer.music.play(-1)  # Reproduce en bucle

def sonido_musicaStop():
    print("Detenimion")
    py.mixer.music.stop

def sonido_efecto(FileName):
    efecto = py.mixer.Sound(FileName)
    efecto.play()

def stopsonido():
    py.mixer.music.stop()