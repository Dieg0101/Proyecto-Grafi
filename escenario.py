import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image #pip install pillow

pygame.init()
pygame.mixer.init()

def load_texture(filename):
    im = Image.open(filename)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, 
                 GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture_id

def draw_escenario(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,0,50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(50,0,50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(50,100,50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(-50,100,50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(50,0,50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(50,0,-50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(50,100,-50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(50,100,50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(50,0,-50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(-50,0,-50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(-50,100,-50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(50,100,-50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,0,-50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(-50,0,50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(-50,100,50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(-50,100,-50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,100,-50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(50,100,-50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(50,100,50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(-50,100,50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()

    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,0,-50) #ESQUINA INFERIOR IZQUIERDA
    glTexCoord2f(1,0)
    glVertex3f(50,0,-50) #ESQUINA INFERIOR DERECHA
    glTexCoord2f(1,1)
    glVertex3f(50,0,50) #ESQUINA SUPERIOR DERECHA
    glTexCoord2f(0,1)
    glVertex3f(-50,0,50) #ESQUINA SUPERIOR IZQUIERDA
    glEnd()