from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import * #pip install pillow
from actions import luces as lc
from actions import objetos2 as obj
from actions import texto as txt

cuerpo = [[(5,10,0),(0.2,50,50),(5,16,0),(0.8,-2,100,90,0,0),(5,16,0),(0.8,2,100,90,0,0),(5,14,0),(2,4,100,90,0,0),
                (5,8,0),(2,-4,100,90,0,0),(8.5,11.5,0),(0.8,-2,100,90,45,0),(8.7,10.8,0),(0.8,2,100,90,0,0),
                (1.5,11.5,0),(0.8,-2,100,90,-45,0),(1.3,10.8,0),(0.8,2,100,90,0,0),(7,6.8,0),(0.8,2,100,90,0,0),
                (7,2.5,0),(0.8,-2,100,90,0,0),(3,6.8,0),(0.8,2,100,90,0,0),(3,2.5,0),(0.8,-2,100,90,0,0)],
          [(5,8,0),(0.2,50,50),(5,14,0),(0.8,-2,100,90,0,0),(5,14,0),(0.8,2,100,90,0,0),(5,12,0),(2,4,100,90,0,0),
                (5,6,0),(2,-4,100,90,0,0),(8.5,9.5,0),(0.8,-2,100,90,45,0),(8.7,8.8,0),(0.8,2,100,90,0,0),
                (1.5,9.5,0),(0.8,-2,100,90,-45,0),(1.3,8.8,0),(0.8,2,100,90,0,0),(7,5.5,-0.6),(0.8,2,100,180,0,0),
                (7,3,-3),(0.8,-2,100,90,0,0),(3,4.8,0),(0.8,2,100,90,0,0),(3,2.5,0.5),(0.8,-2,100,-180,0,0)],
          [(5,10,0),(0.2,50,50),(5,12,-3),(0.8,-2,100,45,0,0),(5,12,-3),(0.8,2,100,45,0,0),(5,11,-2),(2,4,100,45,0,0),
                (5,7,2),(2,-4,100,45,0,0),(8.5,8.5,-2),(0.8,-2,100,90,45,0),(8.7,7.8,-2),(0.8,2,100,90,0,0),
                (1.5,8.5,-2),(0.8,-2,100,90,-45,0),(1.3,7.8,-2),(0.8,2,100,90,0,0),(7,6.8,2),(0.8,2,100,90,0,0),
                (7,2.5,2),(0.8,-2,100,90,0,0),(3,6.8,2),(0.8,2,100,90,0,0),(3,2.5,2),(0.8,-2,100,90,0,0)],
          [(5,2,0),(0.2,50,50),(5,2,5),(0.8,-2,100,180,0,0),(5,2,5),(0.8,2,100,180,0,0),(5,2,3),(2,4,100,180,0,0),
                (5,2,-3),(2,-4,100,180,0,0),(8.5,2,1.2),(0.8,-2,100,180,45,0),(8.7,2,0.5),(0.8,2,100,180,0,0),
                (1.5,2,1.2),(0.8,-2,100,180,-45,0),(1.3,2,0.5),(0.8,2,100,180,0,0),(7,2,-4.3),(0.8,2,100,180,0,0),
                (7,2,-8.3),(0.8,-2,100,180,0,0),(3,2,-4.3),(0.8,2,100,180,0,0),(3,2,-8.3),(0.8,-2,100,180,0,0)],
          [(5,10,0),(0.2,50,50),(5,16,0),(0.8,-2,100,90,0,0),(5,16,0),(0.8,2,100,90,0,0),(5,14,0),(2,4,100,90,0,0),
                (5,8,0),(2,-4,100,90,0,0),(8.5,14.5,0),(0.8,-2,100,270,45,0),(8.7,15.2,0),(0.8,2,100,270,0,0),
                (1.5,14.5,0),(0.8,-2,100,270,-45,0),(1.3,15.2,0),(0.8,2,100,270,0,0),(7,6.8,0),(0.8,2,100,90,0,0),
                (7,2.5,0),(0.8,-2,100,90,0,0),(3,6.8,0),(0.8,2,100,90,0,0),(3,2.5,0),(0.8,-2,100,90,0,0)],
          [(5,10,0),(0.2,50,50),(5,16,0),(0.8,-2,100,90,0,0),(5,16,0),(0.8,2,100,90,0,0),(5,14,0),(2,4,100,90,0,0),
                (5,8,0),(2,-4,100,90,0,0),(8.5,14.5,0),(0.8,-2,100,90,135,0),(9,15,0),(0.8,2,100,90,135,0),
                (1.5,14.5,0),(0.8,-2,100,90,-135,0),(1,15,0),(0.8,2,100,90,-135,0),(7.5,7.1,0),(0.8,2,100,90,45,0),
                (10.4,3.8,0),(0.8,-2,100,90,45,0),(2.5,7.1,0),(0.8,2,100,90,-45,0),(-0.6,3.8,0),(0.8,-2,100,90,-45,0)],
          [(5,3.5,0),(0.2,50,50),(5,9.5,0),(0.8,-2,100,90,0,0),(5,9.5,0),(0.8,2,100,90,0,0),(5,7.5,0),(2,4,100,90,0,0),
                (5,1.5,0),(2,-4,100,90,0,0),(8.5,5,0),(0.8,-2,100,90,45,0),(8.7,4.3,0),(0.8,2,100,90,0,0),
                (1.5,5,0),(0.8,-2,100,90,-45,0),(1.3,4.3,0),(0.8,2,100,90,0,0),(7,1,-0.5),(0.8,2,100,180,0,0),
                (7,1,-5),(0.8,-2,100,180,0,0),(3,1,-0.5),(0.8,2,100,180,0,0),(3,1,-5),(0.8,-2,100,180,0,0)]]
articulaciones = [[(7,13,0),(0.8,50,50),(8.7,11.3,0),(0.6,50,50),(3,13,0),(0.8,50,50),
                   (1.3,11.3,0),(0.6,50,50),(7,7.5,0),(0.8,50,50),(7,4.5,0),(0.8,50,50),
                   (3,7.5,0),(0.8,50,50),(3,4.5,0),(0.8,50,50)],
                  [(7,11,0),(0.8,50,50),(8.7,9.3,0),(0.6,50,50),(3,11,0),(0.8,50,50),
                    (1.3,9.3,0),(0.6,50,50),(7,5.5,0),(0.8,50,50),(7,5.5,-3),(0.8,50,50),
                    (3,5.5,0),(0.8,50,50),(3,2.5,0),(0.8,50,50)],
                  [(7,10,-2),(0.8,50,50),(8.7,8.3,-2),(0.6,50,50),(3,10,-2),(0.8,50,50),
                    (1.3,8.3,-2),(0.6,50,50),(7,7.5,2),(0.8,50,50),(7,4.5,2),(0.8,50,50),
                    (3,7.5,2),(0.8,50,50),(3,4.5,2),(0.8,50,50)],
                  [(7,2,2.8),(0.8,50,50),(8.7,2,1),(0.6,50,50),(3,2,2.8),(0.8,50,50),
                    (1.3,2,1),(0.6,50,50),(7,2,-3.7),(0.8,50,50),(7,2,-6.5),(0.8,50,50),
                    (3,2,-3.7),(0.8,50,50),(3,2,-6.5),(0.8,50,50)],
                  [(7,13,0),(0.8,50,50),(8.7,14.7,0),(0.6,50,50),(3,13,0),(0.8,50,50),
                    (1.3,14.7,0),(0.6,50,50),(7,7.5,0),(0.8,50,50),(7,4.5,0),(0.8,50,50),
                    (3,7.5,0),(0.8,50,50),(3,4.5,0),(0.8,50,50)],
                  [(7,13,0),(0.8,50,50),(8.7,14.7,0),(0.6,50,50),(3,13,0),(0.8,50,50),
                    (1.3,14.7,0),(0.6,50,50),(7,7.5,0),(0.8,50,50),(9,5.5,0),(0.8,50,50),
                    (3,7.5,0),(0.8,50,50),(1,5.5,0),(0.8,50,50)],
                  [(7,6.5,0),(0.8,50,50),(8.7,4.8,0),(0.6,50,50),(3,6.5,0),(0.8,50,50),
                    (1.3,4.8,0),(0.6,50,50),(7,1,0),(0.8,50,50),(7,1,-3),(0.8,50,50),
                    (3,1,0),(0.8,50,50),(3,1,-3),(0.8,50,50)]]

color = [(1, 1, 0), (0.678, 0.847, 0.902), (0, 1, 0), (0.75, 0.75, 0.75), (1, 0.647, 0), (0.6, 0.2, 1.0), (0.3, 0.8, 0.8)]

cara = [[3.5,19,0], [3.5,17,0], [3.5,15,-3], [3.5,4,6], [3.5,19,0], [3.5,19,0], [3.5,12.5,0]]
emocion = [": )", ": (", ":O", "-__-", ".__?", "*.*", ": ]"]

def draw_body(cuerpo_actual,banderas):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [color[cuerpo_actual][0], color[cuerpo_actual][1], color[cuerpo_actual][2], 1.0])  # Color[cuerpo_actual] ambiental y difuso
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])  # Color especular para reflejos (ajústalo según tu preferencia)
    glMaterialf(GL_FRONT, GL_SHININESS, 30.0)  # Ajusta el brillo (de 0 a 128)

    if banderas[0]:
      #Nucleo xd
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][0])
      obj.draw_sphere(*cuerpo[cuerpo_actual][1])
      glPopMatrix()

    if banderas[1]:
      #Cabeza
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][2])
      obj.draw_cone(*cuerpo[cuerpo_actual][3])
      glPopMatrix()

      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][4])
      obj.draw_cone(*cuerpo[cuerpo_actual][5])
      glPopMatrix()

    if banderas[2]:
      #Cuerpo
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][6])
      obj.draw_cone(*cuerpo[cuerpo_actual][7])
      glPopMatrix()
      
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][8])
      obj.draw_cone(*cuerpo[cuerpo_actual][9])
      glPopMatrix()

    #Brazo derecho
    if banderas[3]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][10])
      obj.draw_cone(*cuerpo[cuerpo_actual][11])
      glPopMatrix()

    if banderas[4]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][12])
      obj.draw_cone(*cuerpo[cuerpo_actual][13])
      glPopMatrix()

    #Brazo izquierdo
    if banderas[5]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][14])
      obj.draw_cone(*cuerpo[cuerpo_actual][15])
      glPopMatrix()

    if banderas[6]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][16])
      obj.draw_cone(*cuerpo[cuerpo_actual][17])
      glPopMatrix()

    #Pierna derecha
    if banderas[7]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][18])
      obj.draw_cone(*cuerpo[cuerpo_actual][19])
      glPopMatrix()

    if banderas[8]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][20])
      obj.draw_cone(*cuerpo[cuerpo_actual][21])
      glPopMatrix()

    #Pierna izquierda
    if banderas[9]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][22])
      obj.draw_cone(*cuerpo[cuerpo_actual][23])
      glPopMatrix()

    if banderas[10]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*cuerpo[cuerpo_actual][24])
      obj.draw_cone(*cuerpo[cuerpo_actual][25])
      glPopMatrix()

def draw_art(cuerpo_actual,banderas):
    #Articulaciones en gris oscuro
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0.45, 0.45, 0.45, 1.0])  # Color[cuerpo_actual] ambiental y difuso
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])  # Color[cuerpo_actual] especular para reflejos (ajústalo según tu preferencia)
    glMaterialf(GL_FRONT, GL_SHININESS, 30.0)  # Ajusta el brillo (de 0 a 128)

    #Brazo derecho
    if banderas[3]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][0])
      obj.draw_sphere(*articulaciones[cuerpo_actual][1])
      glPopMatrix()
    
    if banderas[4]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][2])
      obj.draw_sphere(*articulaciones[cuerpo_actual][3])
      glPopMatrix()
    
    #Brazo izquierdo
    if banderas[5]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][4])
      obj.draw_sphere(*articulaciones[cuerpo_actual][5])
      glPopMatrix()
    
    if banderas[6]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][6])
      obj.draw_sphere(*articulaciones[cuerpo_actual][7])
      glPopMatrix()
    
    #Pierna derecha
    if banderas[7]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][8])
      obj.draw_sphere(*articulaciones[cuerpo_actual][9])
      glPopMatrix()
    
    if banderas[8]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][10])
      obj.draw_sphere(*articulaciones[cuerpo_actual][11])
      glPopMatrix()
    
    #Pierna izquierda
    if banderas[9]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][12])
      obj.draw_sphere(*articulaciones[cuerpo_actual][13])
      glPopMatrix()
    
    if banderas[10]:
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glTranslatef(*articulaciones[cuerpo_actual][14])
      obj.draw_sphere(*articulaciones[cuerpo_actual][15])
      glPopMatrix()


def draw(cuerpo_actual,banderas):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #Cabeza,cuerpo,brazos,piernas sin articulaciones[cuerpo_actual]
    draw_body(cuerpo_actual,banderas)
    
    #Articulaciones
    draw_art(cuerpo_actual,banderas)

    #Expresiones
    txt.draw_text(emocion[cuerpo_actual], cara[cuerpo_actual][0], cara[cuerpo_actual][1], cara[cuerpo_actual][2], 50, 255, 255, 255, 0, 0, 0)