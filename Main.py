# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite desplegar la interfaz gráfica de la ventana principal. Además, se conecta con los
# demás eventos del juego.

import sys
import pygame

from Classes import Pointer
from Classes import Button
from Speedometer import Speedometer
from Credits import Credits
from Teaching import Teaching

def Main():
    #Inicio de la ventana
    pygame.init()
    Screen_1 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 1")
    Clock_1 = pygame.time.Clock()

    #Llamado a imágenes necesarias
    Wallpaper = pygame.image.load("Pictures/Wallpaper.png")
    Play_1 = pygame.image.load("Pictures/Play_1a.png")
    Play_2 = pygame.image.load("Pictures/Play_2a.png")
    Credits_1 = pygame.image.load("Pictures/Credits_1.png")
    Credits_2 = pygame.image.load("Pictures/Credits_2.png")
    Teaching_1 = pygame.image.load("Pictures/Teaching_1.png")
    Teaching_2 = pygame.image.load("Pictures/Teaching_2.png")

    #Creación de Botones
    Button_1 = Button(Play_1, Play_2, 650, 300)
    Button_2 = Button(Credits_1, Credits_2, 1328, 35)
    Button_3 = Button(Teaching_1, Teaching_2, 1315, 105)

    #Creación de Puntero
    Pointer_1 = Pointer()

    #Recorrido de eventos
    out = False
    while not out:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                #Selección de botón Play
                if Pointer_1.colliderect(Button_1.rect):
                    Speedometer()
                    quit()
                #Seleccion de botón Credits
                if Pointer_1.colliderect(Button_2.rect):
                    Credits()
                    quit()
                #Selección de botón Teaching
                if Pointer_1.colliderect(Button_3.rect):
                    Teaching()
                    quit()
             #Salida segura
            if event.type == pygame.QUIT:
                out = True
                sys.exit()

        #Actualización de los objetos
        Clock_1.tick(100)
        Screen_1.blit(Wallpaper, (0, 0))
        Pointer_1.update()
        Button_1.update(Screen_1, Pointer_1, 0, 0)
        Button_2.update(Screen_1, Pointer_1, -118, 0)
        Button_3.update(Screen_1, Pointer_1, -137, 0)
        pygame.display.update()

    pygame.quit()

Main()
