import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import textos as txt
import random

# Inicialización de Pygame y OpenGL
pygame.init()
pygame.mixer.init()
display = (1000,600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Configuración inicial de la cámara
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
initial_camera_position = [0, 0, 0]
glTranslatef(*initial_camera_position)
glOrtho(0, 15, 0, 15, 0, 6)

# Lista de palabras posibles para el juego
palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]

# Selecciona una palabra al azar de la lista
palabra = random.choice(palabras).lower()
letras_adivinadas = set()  # Letras que el jugador ha adivinado
intentos_restantes = 6  # Intentos permitidos


# Función para mostrar el progreso actual de la palabra
def mostrar_palabra():
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Bucle principal del juego
while intentos_restantes > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            # Convertir el código de la tecla en carácter
            letra = chr(event.key)
            # Verifica si el jugador ingresó una letra válida
            if not letra.isalpha():
                glPushMatrix()
                txt.draw_text("Por favor, presiona una letra.",-20,-5,30,25,255,255,255,0,0,0)
                glPopMatrix()
                continue
            # Verifica si la letra ya fue adivinada
            if letra in letras_adivinadas:
                glPushMatrix()
                txt.draw_text("Ya has adivinado esa letra. Intenta con otra.",-20,-5,30,25,255,255,255,0,0,0)
                glPopMatrix()
                continue
            
            # Agrega la letra a las letras adivinadas
            letras_adivinadas.add(letra)

            # Verifica si la letra está en la palabra
            if letra in palabra:
                glPushMatrix()
                txt.draw_text(f"¡Bien hecho! La letra '{letra}' está en la palabra.",-20,-5,30,25,255,255,255,0,0,0)
                glPopMatrix()
            else:
                glPushMatrix()
                txt.draw_text(f"La letra '{letra}' no está en la palabra.",-20,-5,30,25,255,255,255,0,0,0)
                glPopMatrix()
                intentos_restantes -= 1

            # Verifica si el jugador ha ganado
            if all(letra in letras_adivinadas for letra in palabra):
                glPushMatrix()
                txt.draw_text(("¡Felicidades! Has adivinado la palabra:" + palabra),-20,-5,30,25,255,255,255,0,0,0)
                glPopMatrix()
                #pygame.quit()
                #quit()
                #break
    glPushMatrix()
    txt.draw_text("¡Bienvenido al juego de ahorcado!",-20,20,30,25,255,255,255,0,0,0)
    #txt.draw_text("_ " * len(palabra),-20,15,30,25,255,255,255,0,0,0)
    txt.draw_text(("Palabra: " + mostrar_palabra()),-20,10,30,25,255,255,255,0,0,0)
    txt.draw_text(f"Intentos restantes: {intentos_restantes}",-20,5,30,25,255,255,255,0,0,0)
    txt.draw_text("Adivina una letra: ",-20,0,30,25,255,255,255,0,0,0)
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(100)
else:
    txt.draw_text(("Lo siento, te has quedado sin intentos. La palabra era:" + palabra),-20,10,30,25,255,255,255,0,0,0)
    #pygame.quit()
    #quit()