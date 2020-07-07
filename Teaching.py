# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite crear la ventana donde se muestran las instrucciones del juego.

import sys
import pygame

from Classes import Pointer
from Classes import Button
from Speedometer import Speedometer

def Teaching():
    # Inicio de la ventana
    pygame.init()
    Screen_5 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 5")
    Clock_5 = pygame.time.Clock()

    # Llamado a imágenes necesarias
    Background = pygame.image.load("Pictures/Shadow_Background.png")
    Return_1 = pygame.image.load("Pictures/Return_1.png")
    Return_2 = pygame.image.load("Pictures/Return_2.png")

    #Definicion de fuente
    Font = pygame.font.Font("BADABB__.TTF", 20)

    # Creación de Botones
    Button_1 = Button(Return_1, Return_2, 50, 377)

    #Creacion de puntero
    Pointer_5 = Pointer()

    #Funcion que crea el texto de la ventana
    def Text():
        line_1 = Font.render("Guia para maestros", True, (13, 71, 114))
        line_2 = Font.render("Esta aplicacion esta disenhada para acompanhar el proceso de aprendizaje de ninhos entre los 13 y 15 anhos que quieran aprender los conceptos basicos del  MOVIMIENTO PARABOLICO ", True, (13, 71, 114))
        line_3 = Font.render("AMORTIGUADO. Para el uso adecuado de la herramienta, se sugiere seguir las siguientes instrucciones:", True, (13, 71, 114))
        line_4 = Font.render("1. Cree un entorno en el que se fomente la curiosidad de los alumnos, en el que describa los terminos de velocidad, masa de un objeto y gravedad.", True, (13, 71, 114))
        line_5 = Font.render("2. Explique como funcionan los controles del juego, como se indica en el apartado CONTROLES.", True, (13, 71, 114))
        line_6 = Font.render("3. Deje al alumno explorar libremente, para posteriormente explicar el objetivo del juego.", True, (13, 71, 114))
        line_7 = Font.render("4. Finalmente, proponga preguntas sobre lo obervado en la simulacion.", True,(13, 71, 114))
        line_8 = Font.render("5. Si desea realizar una explicacion mas avanzada, solicite a los creadores un version en codigo abierto e ingrese al apartado \'Modelo.py\' en el cual podra modificar mas", True,(13, 71, 114))
        line_8 = Font.render("parametros del simulador.", True, (13, 71, 114))
        line_9 = Font.render("Controles", True,(13, 71, 114))
        line_10 = Font.render("La aplicacion cuenta con controles muy intuitivos que permiten aumentar y disminuir la velocidad, asi como iniciar la simulacion o regresar a la ventana anterior.", True, (13, 71, 114))
        Screen_5.blit(line_1, (630, 50))
        Screen_5.blit(line_2, (60, 80))
        Screen_5.blit(line_3, (60, 110))
        Screen_5.blit(line_4, (100, 140))
        Screen_5.blit(line_5, (100, 170))
        Screen_5.blit(line_6, (100, 200))
        Screen_5.blit(line_7, (100, 230))
        Screen_5.blit(line_8, (100, 260))
        Screen_5.blit(line_9, (670, 290))
        Screen_5.blit(line_10, (60, 320))

    #Recorrido de eventos
    play = True
    while play:

        for event in pygame.event.get():
            #Salida segura
            if event.type == pygame.QUIT:
                sys.exit()
            #Seleccion de boton return
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_5.colliderect(Button_1.rect):
                    Main()
                    quit()

        #Actualizacion de objetos
        Clock_5.tick(100)
        Screen_5.blit(Background, (0, 0))
        Text()
        Pointer_5.update()
        Button_1.update(Screen_5, Pointer_5, 0, 0)
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
                    # Teaching()
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