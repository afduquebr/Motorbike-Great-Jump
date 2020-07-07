# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite crear la ventana donde se muestran los créditos de la creación del juego.

import sys
import pygame

from Classes import Pointer
from Classes import Button
from Speedometer import Speedometer
from Teaching import Teaching


def Credits():
    # Inicio de la ventana
    pygame.init()
    Screen_4 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 4")
    Clock_4 = pygame.time.Clock()

    # Llamado a imágenes necesarias
    Background = pygame.image.load("Pictures/Shadow_Background.png")
    Return_1 = pygame.image.load("Pictures/Return_1.png")
    Return_2 = pygame.image.load("Pictures/Return_2.png")
    Font = pygame.font.Font("BADABB__.TTF", 35)

    # Creación de Botones
    Button_1 = Button(Return_1, Return_2, 50, 377)

    #Creacion del puntero
    Pointer_4 = Pointer()

    #Definicion de funcion que crea el texto de la ventana
    def Text():
        line_1 = Font.render("Proyecto Final", True, (13, 71, 114))
        line_2 = Font.render("Introduccion a las Ciencias de la Computacion y la Programacion", True, (13, 71, 114))
        line_3 = Font.render("Profesor: Humberto  Sarria Zapata", True, (13, 71, 114))
        line_4 = Font.render("Integrantes: Daniel Barrios Calderon", True, (13, 71, 114))
        line_5 = Font.render("Andres Felipe Duque Bran", True, (13, 71, 114))
        line_6 = Font.render("Agradecimiento Especial: Laura Daniel Pinheros Roa", True, (13, 71, 114))
        Screen_4.blit(line_1, (580, 50))
        Screen_4.blit(line_2, (250, 100))
        Screen_4.blit(line_3, (250, 150))
        Screen_4.blit(line_4, (250, 200))
        Screen_4.blit(line_5, (407, 250))
        Screen_4.blit(line_6, (250, 300))

    #Recorrido de eventos
    play = True
    while play:

        for event in pygame.event.get():
            #Salida segura
            if event.type == pygame.QUIT:
                sys.exit()
            #Seleccion de return
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_4.colliderect(Button_1.rect):
                    Main()
                    quit()

        #Actualizacion de objetos
        Clock_4.tick(100)
        Screen_4.blit(Background, (0, 0))
        Text()
        Pointer_4.update()
        Button_1.update(Screen_4, Pointer_4, 0, 0)
        pygame.display.update()

#__________________________________________________ Definicion de la funcion Main para poder usar return

def Main():
    pygame.init()
    Screen_1 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 1")
    Clock_1 = pygame.time.Clock()

    Wallpaper = pygame.image.load("Pictures/Wallpaper.png")
    Play_1 = pygame.image.load("Pictures/Play_1a.png")
    Play_2 = pygame.image.load("Pictures/Play_2a.png")
    Credits_1 = pygame.image.load("Pictures/Credits_1.png")
    Credits_2 = pygame.image.load("Pictures/Credits_2.png")
    Teaching_1 = pygame.image.load("Pictures/Teaching_1.png")
    Teaching_2 = pygame.image.load("Pictures/Teaching_2.png")

    Button_1 = Button(Play_1, Play_2, 650, 300)
    Button_2 = Button(Credits_1, Credits_2, 1328, 35)
    Button_3 = Button(Teaching_1, Teaching_2, 1315, 105)

    Pointer_1 = Pointer()

    out = False
    while not out:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_1.colliderect(Button_1.rect):
                    Speedometer()
                    quit()
                if Pointer_1.colliderect(Button_2.rect):
                    Credits()
                    quit()
                if Pointer_1.colliderect(Button_3.rect):
                    Teaching()
                    quit()
            if event.type == pygame.QUIT:
                out = True
                sys.exit()

        Clock_1.tick(100)
        Screen_1.blit(Wallpaper, (0, 0))
        Pointer_1.update()
        Button_1.update(Screen_1, Pointer_1, 0, 0)
        Button_2.update(Screen_1, Pointer_1, -118, 0)
        Button_3.update(Screen_1, Pointer_1, -137, 0)
        pygame.display.update()

    pygame.quit()
