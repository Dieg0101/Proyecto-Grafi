import pygame as py
import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from robotec import robot
import escenario as es
from Instrucciones import Instrucciones  # Asegúrate de que esta clase esté correctamente definida e importada
import random
import sonidos as so

# Inicializar Pygame y OpenGL
py.init()
display = (1000, 600)
py.display.set_mode(display, DOUBLEBUF | OPENGL)
py.display.set_caption("Robot y Juego de Ahorcado")
gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
glTranslatef(0, -2, -15)

# Crear instancia de Instrucciones
instruction = Instrucciones()

# Cargar texturas de fondo
fondos_variantes = [es.load_texture(f"fondos/r{i}.jpg") for i in range(8)]
robot_variants = [
    robot.draw_robot,           # Variante normal
    robot.draw_angry_robot,     # Variante enojada
    robot.draw_surprised_robot,
    robot.draw_flirtatious_robot,
    robot.draw_sad_robot,       # Variante triste
    robot.draw_dead_robot,      
    robot.draw_malfunctioning_robot,
    robot.draw_hit_robot
]

instrucciones_win = [
        "Felicidades, ganaste !!"
    ]
instrucciones_lost = [
        "Has perdido !!"
    ]
# Variables de control para mostrar mensajes de victoria o derrota
mostrar_win = False
mostrar_lost = False

def reset_game():
    global palabra, letras_adivinadas, intentos_restantes, palabra_adivinada, current_variant_index, instrucciones_ahorcado, mostrar_win, mostrar_lost
    palabra = random.choice(palabras).lower()
    letras_adivinadas = set()
    intentos_restantes = 3
    palabra_adivinada = False
    current_variant_index = 0
    mostrar_win = False
    mostrar_lost = False
    instrucciones_ahorcado = [
        "Adivina la palabra:",
        f"Intentos restantes: {intentos_restantes}",
        "Usa el teclado para ingresar letras.",
        "ESC: Salir del juego",
        "Q: Reiniciar juego"
    ]

# Lista de palabras y lógica del juego
palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]
reset_game()  # Inicializar el primer juego

# Función para mostrar la palabra en progreso con formato de "_ _ _ _"
def mostrar_palabra_formateada():
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Lógica de entrada de teclado y actualización del estado del juego
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False

            # Reiniciar el juego al presionar 'Q'
            if event.key == py.K_q:
                reset_game()
                continue  

            # Captura de letras para el juego de ahorcado si la palabra aún no ha sido adivinada
            if not palabra_adivinada and intentos_restantes > 0 and event.unicode.isalpha() and len(event.unicode) == 1:
                letra = event.unicode.lower()
                if letra not in letras_adivinadas:
                    letras_adivinadas.add(letra)
                    if letra not in palabra:
                        intentos_restantes -= 1
                        instrucciones_ahorcado[1] = f"Intentos restantes: {intentos_restantes}"
                    # Verificar si se han quedado sin intentos
                    if intentos_restantes == 0:
                        mostrar_lost = True
                        instrucciones_ahorcado.append(f"La palabra correcta era: {palabra}")
                        current_variant_index = 5  # Variante de robot muerto

                # Verificar si se adivinó la palabra
                if all(letra in letras_adivinadas for letra in palabra):
                    palabra_adivinada = True
                    mostrar_win = True
                    current_variant_index = 3  # Variante de robot coqueto

    # Limpiar la pantalla y configurar el fondo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    es.draw_escenario(fondos_variantes[current_variant_index])
    glDisable(GL_TEXTURE_2D)

    # Dibujar el robot con la variante actual
    glPushMatrix()
    glTranslatef(-2, 4, 0)
    glScalef(1, 1, 1)
    robot_variants[current_variant_index]()
    glPopMatrix()

    # Actualizar y dibujar la palabra con formato
    palabra_formateada = f"Palabra: {mostrar_palabra_formateada()}"
    instruction.draw_instructions([palabra_formateada] + instrucciones_ahorcado[1:], 500, 300)  # Ajustar posición según sea necesario

    # Mostrar mensajes de victoria o derrota si corresponde
    if mostrar_win:
        instruction.draw_instructions(instrucciones_win, 100, 10)
        so.sonido_efecto("Sounds/win.mp3")               
    elif mostrar_lost:
        instruction.draw_instructions(instrucciones_lost, 100, 10)
        so.sonido_efecto("Sounds/lost.mp3")               

    py.display.flip()
    py.time.wait(10)

py.quit()