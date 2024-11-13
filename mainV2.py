import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import escenario as es
import sonidos as so
from actions import luces as lc
import textos as txt
import colisiones as coli
from Bombolin import Bombolin as bombolin
from robotec import robot
from Instrucciones import Instrucciones

import trixor
import random

py.init()
py.mixer.init()

display = (1000,600)
py.display.set_mode(display, DOUBLEBUF | OPENGL)
py.display.set_caption("Compile or die")
gluPerspective(50, (display[0]/display[1]),0.1,150.0)
glTranslatef(0,0,-5)

#Pantalla seleccion de nivel
escenario = "Images/1344089.png"
# Textos del menú
menu_items = ["     1. Fundamentos de Programación", 
              "2. Programación Orientada a Objetos", 
              "              3. Estructura de Datos", 
              "                     Instrucciones"]
selected_item = 0
menu_active = True
show_instructions = False
mouse_active = False

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT = (50, 205, 50)

# Dibujar el menú
def draw_menu():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #set_lighting()
    
    glPushMatrix()
    glRotatef(20, 1, 0, 0)  # Rotar para mejor vista
    glRotatef(20, 0, 1, 0)


    # Título cambia según el estado del menú
    title_text = "Instrucciones" if show_instructions else "Compile or Die"
    txt.draw_text(title_text, -1.2, 1.5, 0, 74, WHITE[0], WHITE[1], WHITE[2], BLACK[0], BLACK[1], BLACK[2])

    if menu_active:
        # Dibujar cada item del menú más a la derecha
        for i, item in enumerate(menu_items):
            color = HIGHLIGHT if i == selected_item else WHITE
            txt.draw_text(item, -2.2, 1 - (i * 0.5), 0, 50, color[0], color[1], color[2], BLACK[0], BLACK[1], BLACK[2])

    if show_instructions:
        # Mostrar instrucciones con mayor separación y más a la izquierda
        instrucciones_items = [
            "En cada nivel se te presentará una pregunta que tendrás que responder" ,            
            "Para responder tendrás que presionar una letra del teclado",            
            "Esc. para volver al menú",
            ""
        ]
        for i, item in enumerate(instrucciones_items):
            txt.draw_text(item, -3, 1 - (i * 0.25), 0, 40, WHITE[0], WHITE[1], WHITE[2], BLACK[0], BLACK[1], BLACK[2])

    glPopMatrix()
    #py.display.flip()

camara_speed = 0.1
rotacion_speed = 0.2
mouse_sensitivity = 0.1
py.event.set_grab(True)
py.mouse.set_visible(False)
directorio_script = os.path.dirname(os.path.abspath(__file__))

escenarios = ["fondos/FondoPrincipal.jpg","fondos/fondoBomb1.jpg", "fondos/fondoBomb2.jpg", "fondos/fondoBomb3.jpg", "fondos/fondoBomb4.png", "fondos/fondoBomb5.png",
              "fondos/fondoBomb6.png","fondos/fondoBomb7.jpg"]
escenarios_cargados = [es.load_texture(escenario) for escenario in escenarios]

instruction = Instrucciones()

creadores_arr = ["ARISTA RODRIGUEZ EMILIANO",
                 "ALCANTARA FERNANDEZ SAMUEL",
                 "SALAZAR REYES DIEGO",
                 "Creadores:"]

instrucciones_Bombolin = ["R = Bombolin Feliz",
                       "T = Bombolin Triste.",
                       "Y = Bombolin Enojado",
                       "U = Bombolin Dudoso",
                       "I = Bombolin Muerto",
                       "K = Bombolin Sonriendo",
                       "L = Bombolin Indiferente",
                       "ESC:  Regresar",
                       "TAB:  Seleccionar", "Bombolin"]

instrucciones_Trixor = ["Click izquierdo = Siguiente estado",
                       "Click derecho = Estado anterior ",
                       "ESC:  Regresar",
                       "TAB:  Seleccionar", "TRIXOR"]

instrucciones_Robot = ["P = Siguiente estado de Robot ",
                       "ESC:  Regresar",
                       "TAB:  Seleccionar", "ROBOTEC"]

instrucciones_seleccionar = ["SELECCIONA TU PERSONAJE "]
instrucciones_seleccionarTrixor = ["1 = TRIXOR "]
instrucciones_seleccionarBombolin = ["2 = BOMBOLIN"]
instrucciones_seleccionarRobot = ["3 = ROBOTEC"]

cuerpo_actual = 0
fondos_trixor = ["fondos/trix1.jpeg","fondos/trix2.jpeg","fondos/trix3.jpeg","fondos/trix4.jpeg","fondos/trix5.jpeg","fondos/trix6.jpeg","fondos/trix7.jpeg"]
fondos_trix_cargados = [es.load_texture(fondo) for fondo in fondos_trixor]
sonidos = [py.mixer.Sound(f"Sounds/sonido{i}.wav") for i in range(1, 8)]
banderas = [True, True, True, True, True, True, True, True, True, True, True]
# Para ir eliminando parte por parte del trixor
bandera_actual = 10

escenarios_bombolin = ["fondos/fondoBomb1.jpg", "fondos/fondoBomb2.jpg", "fondos/fondoBomb3.jpg", "fondos/fondoBomb4.png", "fondos/fondoBomb5.png",
              "fondos/fondoBomb6.png","fondos/fondoBomb7.jpg"]
escenarios_cargadosBombolin = [es.load_texture(escenario) for escenario in escenarios_bombolin]



def drawTrixor_Menu(cuerpo_actual,banderas):
    glTranslatef(-70,-20,20)
    #glRotatef(180, 0, 1, 0)
    glScalef(4, 4, 4)
    trixor.draw(cuerpo_actual,banderas)

global opcionBombolin 
opcionBombolin = 0
def drawBombolin_Menu(opcionBombolin):
    #glScalef(2,2,2)
    glTranslate(5,0,0)
    if opcionBombolin == 0:
        bombolin.drawBombolin(0,0,False)
        
    elif opcionBombolin == 1:
        bombolin.drawBombolinFeliz(0,0,False)
        
    elif opcionBombolin == 2:
        bombolin.drawBombolinTriste(0,0,False)
        
    elif opcionBombolin == 3:
        bombolin.drawBombolinEnojado(0,0,False)
        
    elif opcionBombolin == 4:
        bombolin.drawBombolinDudoso(0,0)
        
    elif opcionBombolin == 5:
        bombolin.drawBombolinMuerto(0,0,False)
        
    elif opcionBombolin == 6:
        bombolin.drawBombolinSonriendo(0,0,False)
    elif opcionBombolin == 7:
        bombolin.drawBombolinIndiferente(0,0,False)
        
def drawRobot_Menu():
    glPushMatrix()
    glTranslatef(28, 10, 10) 
    glScalef(2.5, 2.5, 2.5)  
    glRotatef(200, 0, 1, 0)  
    robot.draw_robot()
    glPopMatrix()

def drawRobot_Menu2():
    glPushMatrix()
    glTranslatef(0, 25, 0)  
    glScalef(5.5, 5.5, 5.5)  
    glRotatef(180, 0, 1, 0)  
    robot.draw_robot()
    glPopMatrix()

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

fondos_variantes = [
    es.load_texture("fondos/r0.jpg"),      # Fondo para la variante normal
    es.load_texture("fondos/r1.jpg"),     # Fondo para la variante enojada
    es.load_texture("fondos/r2.jpg"),    # Fondo para la variante asustada
    es.load_texture("fondos/r3.jpg"),       # Fondo para la variante feliz
    es.load_texture("fondos/r4.jpg"),     # Fondo para la variante que flirtea
    es.load_texture("fondos/r5.jpg"),      # Fondo para la variante muerta
    es.load_texture("fondos/r6.jpg"),     
    es.load_texture("fondos/r7.jpg")     
]
r_sonidos_variantes = [
    os.path.join(directorio_script,"Sounds/r_s0.mp3"),      
    os.path.join(directorio_script,"Sounds/r_s1.mp3"),     
    os.path.join(directorio_script,"Sounds/r_s2.mp3"),    
    os.path.join(directorio_script,"Sounds/r_s3.mp3"),       #  para la variante feliz
    os.path.join(directorio_script,"Sounds/r_s4.mp3"),     # Fondo para la variante que flirtea
    os.path.join(directorio_script,"Sounds/r_s5.mp3"),      # Fondo para la variante muerta
    os.path.join(directorio_script,"Sounds/r_s6.mp3"),     
    os.path.join(directorio_script,"Sounds/r_s7.mp3")     
]


current_variant_index = 0  # Índice de la variante actual

menuPersonaje=False
trixor_selected = False
bombolin_selected = False
robot_selected = False
three_selected = True
keyboard_lock = False
nivel_seleccionado, intentos_restantes, intentos = 0, 0, 0
trixor_selected2 = False
bombolin_selected2 = False
robot_selected2 = False
so.sonido_musica("Sounds/Music.wav")

def seleccion():
    glTranslatef(0,-2,-5)
    glOrtho(0,15,0,15,0,6)
    global mouse_active,menu_active, show_instructions
    global three_selected, trixor_selected, bombolin_selected, robot_selected
    mouse_active = True
    menu_active = False #Se desactiva el menu
    show_instructions = False
    so.stop()
    so.sonido_efecto("Sounds/FX2.wav")  # Sonido de selección
    three_selected=True
    trixor_selected=False
    bombolin_selected=False
    robot_selected=False
# Lista de palabras y lógica del juego
palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]
# Función para reiniciar el juego
palabra = random.choice(palabras).lower()
palabra_adivinada = Falsepalabra = random.choice(palabras).lower()
letras_adivinadas = set()
palabra_adivinada = False
current_variant_index = 0
instrucciones_ahorcado = [""]
def reset_game(intentos, nivel_seleccionado):
    global palabra, letras_adivinadas, intentos_restantes, palabra_adivinada, current_variant_index, instrucciones_ahorcado
    if nivel_seleccionado == 1:
        palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]
    elif nivel_seleccionado == 2:
        palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]
    else:
        palabras = ["python", "programacion", "juego", "computadora", "codigo", "desarrollo", "software"]
    palabra = random.choice(palabras).lower()
    letras_adivinadas = set()
    intentos_restantes = intentos
    palabra_adivinada = False
    current_variant_index = 0
    instrucciones_ahorcado = [
        "Adivina la palabra:",
        f"Intentos restantes: {intentos_restantes}",
        "Usa el teclado para ingresar letras.",
        "0: Salir del juego",
        "9: Reiniciar juego"
    ]
# Función para mostrar la palabra en progreso con formato de "_ _ _ _"
def mostrar_palabra_formateada():
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

while True:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        #Despues de presionar TAB para seleccionar un personaje
        #para no tener que cambiar todas las demas teclas a otros botones
        if event.type == py.KEYDOWN:
            if keyboard_lock:
                if event.key == py.K_a:
                    letra = "a"
                    print("funciono xdddd")
                if event.key == py.K_b:
                    letra = "b"
                if event.key == py.K_c:
                    letra = "c"
                if event.key == py.K_d:
                    letra = "d"
                if event.key == py.K_e:
                    letra = "e"
                if event.key == py.K_f:
                    letra = "f"
                if event.key == py.K_g:
                    letra = "g"
                if event.key == py.K_h:
                    letra = "h"
                if event.key == py.K_i:
                    letra = "i"
                if event.key == py.K_j:
                    letra = "j"
                if event.key == py.K_k:
                    letra = "k"
                if event.key == py.K_l:
                    letra = "l"
                if event.key == py.K_m:
                    letra = "m"
                if event.key == py.K_n:
                    letra = "n"
                if event.key == py.K_o:
                    letra = "o"
                if event.key == py.K_p:
                    letra = "p"
                if event.key == py.K_q:
                    letra = "q"
                if event.key == py.K_r:
                    letra = "r"
                if event.key == py.K_s:
                    letra = "s"
                if event.key == py.K_t:
                    letra = "t"
                if event.key == py.K_u:
                    letra = "u"
                if event.key == py.K_v:
                    letra = "v"
                if event.key == py.K_w:
                    letra = "w"
                if event.key == py.K_x:
                    letra = "x"
                if event.key == py.K_y:
                    letra = "y"
                if event.key == py.K_z:
                    letra = "z"
                if event.key == py.K_0:
                    py.quit()
                    quit()
                # Reiniciar el juego al presionar 'R'
                if event.key == py.K_9:
                    reset_game(intentos,nivel_seleccionado)
    
                # Captura de letras para el juego de ahorcado si la palabra aún no ha sido adivinada
                if not palabra_adivinada and intentos_restantes > 0 and event.unicode.isalpha() and len(event.unicode) == 1:
                    letra = event.unicode.lower()
                    if letra not in letras_adivinadas:
                        letras_adivinadas.add(letra)
                        if letra not in palabra:
                            intentos_restantes -= 1
                            instrucciones_ahorcado[1] = f"Intentos restantes: {intentos_restantes}"
                            instrucciones_ahorcado.append(f"La letra '{letra}' no está en la palabra.")
                        else:
                            instrucciones_ahorcado.append(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
                        # Verificar si se han quedado sin intentos
                        if intentos_restantes == 0:
                            instrucciones_ahorcado.append("Te has quedado sin intentos.")
                            instrucciones_ahorcado.append(f"La palabra correcta era: {palabra}")
                            current_variant_index = 5
    
                    # Verificar si se adivinó la palabra
                    if all(letra in letras_adivinadas for letra in palabra):
                        palabra_adivinada = True
                        instrucciones_ahorcado.append("¡Felicidades! Has adivinado la palabra.")
                        current_variant_index = 3  # Cambiar a la variante 3 del robot
            else:
                if menu_active and event.key == py.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                    so.sonido_efecto("Sounds/FX1.wav")  # Sonido de movimiento
                elif menu_active and event.key == py.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                    so.sonido_efecto("Sounds/FX1.wav")  # Sonido de movimiento
                #Acciones que se tomaran a cabo cuando se seleccione un elemento del menu
                elif menu_active and event.key == py.K_RETURN:
                    if selected_item == 0:  #Si se selecciona la opcion de Fundamentos de Programacion
                        seleccion()
                        nivel_seleccionado = 1
                        
                    elif selected_item == 1:
                        seleccion()
                        nivel_seleccionado = 2
                        
                    elif selected_item == 2:
                        seleccion()
                        nivel_seleccionado = 3
                        
                    elif selected_item == 3:  # Instrucciones
                        show_instructions = True
                        menu_active = False
                        so.sonido_efecto("Sounds/FX2.wav")  # Sonido de selección
                    
                elif show_instructions and event.key == py.K_ESCAPE:
                    show_instructions = False
                    menu_active = True
                    so.sonido_efecto("Sounds/FX3.wav")  # Sonido de salida
                elif event.key == py.K_p:  # Cambiar a la variante de robot
                    current_variant_index = (current_variant_index - 1) % len(robot_variants)
                    so.play(r_sonidos_variantes[current_variant_index])
                elif event.key == py.K_1:
                        three_selected = False
                        trixor_selected = True
                        bombolin_selected = False
                        robot_selected = False
                        so.sonido_efecto("Sounds/FxSelected.wav")
                elif event.key == py.K_2:
                        three_selected = False
                        trixor_selected = False
                        bombolin_selected = True
                        opcionBombolin=0
                        robot_selected = False
                        so.sonido_efecto("Sounds/FxSelected.wav")
                elif event.key == py.K_3:
                        three_selected = False
                        robot_selected = True
                        trixor_selected = False
                        bombolin_selected = False
                        so.play(r_sonidos_variantes[current_variant_index])
                elif event.key == py.K_ESCAPE:
                        three_selected = True
                        trixor_selected = False
                        bombolin_selected = False
                        opcionBombolin =0
                        robot_selected = False
                        so.sonido_efecto("Sounds/FxEsc.wav")
                elif event.key==py.K_r: #-------------------------> Gestion de eventos para los movimientos del Bombolin
                    opcionBombolin = 1
                    so.sonido_efecto("Sounds/BombolinFeliz.wav")
                    
                elif event.key==py.K_t:
                    opcionBombolin = 2
                    so.sonido_efecto("Sounds/BombolinTriste.wav")
                    
                elif event.key==py.K_y:
                    opcionBombolin = 3
                    so.sonido_efecto("Sounds/BombolinEnojado.wav")
                    
                elif event.key==py.K_u:
                    opcionBombolin = 4
                    so.sonido_efecto("Sounds/BombolinSorpresa.wav")
                    
                elif event.key==py.K_i:
                    opcionBombolin = 5
                    so.sonido_efecto("Sounds/BombolinMuerto.wav")
                    
                elif event.key==py.K_k:
                    opcionBombolin = 6
                    so.sonido_efecto("Sounds/BombolinSonriendo.wav")
                    
                elif event.key==py.K_l:
                    opcionBombolin = 7
                    so.sonido_efecto("Sounds/BombolinIndiferente.wav")
                #elif event.key == py.K_9:
                #    banderas[bandera_actual] = False
                #    bandera_actual -= 1
                elif event.key == K_TAB:
                    keyboard_lock = True
                    mouse_active = False
                    if trixor_selected:
                        trixor_selected2 = True
                        intentos = 10
                        reset_game(intentos,nivel_seleccionado)  # Inicializar el primer juego
                    elif bombolin_selected:
                        bombolin_selected2 = True
                        intentos = 5
                        reset_game(intentos,nivel_seleccionado)  # Inicializar el primer juego
                    else:
                        robot_selected2 = True
                        intentos = 3
                        reset_game(intentos,nivel_seleccionado)  # Inicializar el primer juego
    
                # Controles de la cámara
                keys = py.key.get_pressed()
                if keys[py.K_e]:
                    glTranslate(0, 0, 10)
                if keys[py.K_q]:
                    glTranslate(0, 0, -10)
                if keys[py.K_d]:
                    glTranslate(-10, 0, 0)
                if keys[py.K_a]:
                    glTranslate(10, 0, 0)
                if keys[py.K_w]:
                    glTranslate(0, -10, 0)
                if keys[py.K_s]:
                    glTranslate(0, 10, 0)
                if keys[py.K_0]:
                     py.quit()
                     quit()
    if not keyboard_lock:
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo
                sonidos[cuerpo_actual].stop()
                cuerpo_actual = (cuerpo_actual + 1) % 7
                sonidos[cuerpo_actual].play()
            elif event.button == 3:  # Botón derecho
                sonidos[cuerpo_actual].stop()
                cuerpo_actual = (cuerpo_actual - 1) % 7
                sonidos[cuerpo_actual].play()
    # Capturar eventos de movimiento del mouse solo si `mouse_active` es True
    if mouse_active and event.type == py.MOUSEMOTION:
        # Rotar cámara con el mouse
        x, y = py.mouse.get_rel()
        glRotatef(x * mouse_sensitivity, 0, 1, 0)
        py.mouse.set_pos(display[0] // 2, display[1] // 2)
    
    
    if menu_active or show_instructions:
        draw_menu()
    else:
        if trixor_selected:
            #glRotatef(180, 0, 1, 0)
            #glScalef(4, 4, 4)
            glPushMatrix()
            glTranslatef(55,-15,0)
            lc.iluminacion("Interpolado")
            drawTrixor_Menu(cuerpo_actual,banderas)
            glDisable(GL_LIGHTING)
            #escenario_actual = "fondos/fondoMenu2.jpg"
            glEnable(GL_TEXTURE_2D)
            es.draw_escenario(fondos_trix_cargados[cuerpo_actual])
            glDisable(GL_TEXTURE_2D)
            instruction.draw_instructions(instrucciones_Trixor, 500, 10)    
            glPopMatrix()
        elif bombolin_selected:
            #drawBombolin_Menu()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glScalef(7,7,7)
            glTranslatef(-10,0,0)
            lc.iluminacion("Interpolado")
            glTranslatef(-7,-4,4)
            drawBombolin_Menu(opcionBombolin)
            glEnable(GL_TEXTURE_2D)     
            es.draw_escenario(escenarios_cargadosBombolin[opcionBombolin-1])     
            glDisable(GL_TEXTURE_2D)   
            instruction.draw_instructions(instrucciones_Bombolin, 500, 10)
            glPopMatrix()

        elif robot_selected:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glDisable(GL_LIGHTING)
            
            glPushMatrix()
            glScalef(5.5, 5.5, 5.5)  
            glRotatef(180, 0, 1, 0)
            glTranslatef(0,5,0)
            robot_variants[current_variant_index]()
            glPopMatrix()

            glEnable(GL_TEXTURE_2D)
            es.draw_escenario(fondos_variantes[current_variant_index])
            glDisable(GL_TEXTURE_2D)
            instruction.draw_instructions(instrucciones_Robot, 500, 10)
            glPopMatrix()

        if three_selected:

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            lc.iluminacion("Interpolado")
            sonidos[cuerpo_actual].stop()
            cuerpo_actual = 0
            drawTrixor_Menu(cuerpo_actual,banderas)
            glDisable(GL_LIGHTING)
            glEnable(GL_TEXTURE_2D)
            es.draw_escenario(escenarios_cargados[0])
            glDisable(GL_TEXTURE_2D)

            drawBombolin_Menu(opcionBombolin)
            drawRobot_Menu() 
            instruction.draw_instructions(creadores_arr, 500, 10)
            instruction.draw_instructions(instrucciones_seleccionar, 250, 520)
            instruction.draw_instructions(instrucciones_seleccionarTrixor, 100, 50)
            instruction.draw_instructions(instrucciones_seleccionarBombolin, 300, 70)
            instruction.draw_instructions(instrucciones_seleccionarRobot, 500, 150)

            glPopMatrix()
        if trixor_selected2:
            #glRotatef(180, 0, 1, 0)
            #glScalef(4, 4, 4)
            glPushMatrix()
            #glTranslatef(-55,15,55)
            lc.iluminacion("Interpolado")
            drawTrixor_Menu(cuerpo_actual,banderas)
            glTranslate(30,-30,-30)
            glDisable(GL_LIGHTING)
            #escenario_actual = "fondos/fondoMenu2.jpg"
            glEnable(GL_TEXTURE_2D)
            es.draw_escenario(fondos_trix_cargados[cuerpo_actual])
            glDisable(GL_TEXTURE_2D)
            instruction.draw_instructions(instrucciones_Trixor, 500, 10)    
            glPopMatrix()
            #ahorcado()
        if bombolin_selected2:
            #TRASLADAR PERSONAJE AL FONDO
            #drawBombolin_Menu()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glScalef(7,7,7)
            glTranslatef(-10,0,0)
            lc.iluminacion("Interpolado")
            glTranslatef(-7,-4,4)
            drawBombolin_Menu(opcionBombolin)
            glEnable(GL_TEXTURE_2D)     
            es.draw_escenario(escenarios_cargadosBombolin[opcionBombolin-1])     
            glDisable(GL_TEXTURE_2D)   
            instruction.draw_instructions(instrucciones_Bombolin, 500, 10)
            glPopMatrix()

        if robot_selected2:
            #TRASLADAR PERSONAJE AL FONDO DEL ESCENARIO
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glDisable(GL_LIGHTING)
            
            glPushMatrix()
            glScalef(5.5, 5.5, 5.5)  
            glRotatef(180, 0, 1, 0)
            glTranslatef(0,5,0)
            robot_variants[current_variant_index]()
            glPopMatrix()

            glEnable(GL_TEXTURE_2D)
            es.draw_escenario(fondos_variantes[current_variant_index])
            glDisable(GL_TEXTURE_2D)
            instruction.draw_instructions(instrucciones_Robot, 500, 10)
            glPopMatrix()
        if trixor_selected2 or bombolin_selected2 or robot_selected2:
            # Actualizar y dibujar la palabra con formato
            palabra_formateada = f"Palabra: {mostrar_palabra_formateada()}"
            instruction.draw_instructions([palabra_formateada] + instrucciones_ahorcado[1:], 500, 300)  # Ajustar posición según sea necesario
    py.display.flip()
    py.time.wait(10)
