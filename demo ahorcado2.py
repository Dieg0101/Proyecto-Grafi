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
letra = ""

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
            if event.key == pygame.K_a:
                letra = "a"
            if event.key == pygame.K_b:
                letra = "b"
            if event.key == pygame.K_c:
                letra = "c"
            if event.key == pygame.K_d:
                letra = "d"
            if event.key == pygame.K_e:
                letra = "e"
            if event.key == pygame.K_f:
                letra = "f"
            if event.key == pygame.K_g:
                letra = "g"
            if event.key == pygame.K_h:
                letra = "h"
            if event.key == pygame.K_i:
                letra = "i"
            if event.key == pygame.K_j:
                letra = "j"
            if event.key == pygame.K_k:
                letra = "k"
            if event.key == pygame.K_l:
                letra = "l"
            if event.key == pygame.K_m:
                letra = "m"
            if event.key == pygame.K_n:
                letra = "n"
            if event.key == pygame.K_o:
                letra = "o"
            if event.key == pygame.K_p:
                letra = "p"
            if event.key == pygame.K_q:
                letra = "q"
            if event.key == pygame.K_r:
                letra = "r"
            if event.key == pygame.K_s:
                letra = "s"
            if event.key == pygame.K_t:
                letra = "t"
            if event.key == pygame.K_u:
                letra = "u"
            if event.key == pygame.K_v:
                letra = "v"
            if event.key == pygame.K_w:
                letra = "w"
            if event.key == pygame.K_x:
                letra = "x"
            if event.key == pygame.K_y:
                letra = "y"
            if event.key == pygame.K_z:
                letra = "z"
            if event.key == pygame.K_0:
                pygame.quit()
                quit()
    ## Verifica si el jugador ingresó una letra válida
    #if not letra.isalpha():
    #    glPushMatrix()
    #    txt.draw_text("Por favor, presiona una letra.",-20,-5,30,25,255,255,255,0,0,0)
    #    glPopMatrix()
    #    continue
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