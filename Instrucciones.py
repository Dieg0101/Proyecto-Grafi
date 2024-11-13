import pygame
from OpenGL.raw.GLU import gluOrtho2D
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *


class Instrucciones():

    def draw_instructions(self, instructions, x, y):
        glColor(1, 1, 1)  # Establece el color del texto a blanco
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 800, 0, 600)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Posición de las instrucciones en la esquina inferior izquierda
        x_pos = x
        y_pos = y

        # Dibuja cada línea de instrucción
        for text in instructions:
            self.render_text(x_pos, y_pos, text)
            y_pos += 20  # Ajusta la posición vertical para la siguiente línea

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def render_text(self, x, y, text):
        font = pygame.font.Font(None, 25)  # Define el tamaño de la fuente
        text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))  # Renderiza el texto
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glRasterPos2f(x, y)  # Establece la posición del texto
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)