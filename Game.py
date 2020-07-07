# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite llevar a cabo el desarrollo del evento donde tiene lugar el movimiento parabólico.

import sys
import pygame

from Classes import Pointer
from Classes import Button
from Plot import Plot

def Game_loop(V0):
    # Inicio de la ventana
    pygame.init()
    Screen_2 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 2")
    Clock_2 = pygame.time.Clock()

    # Creación variables necesarias
    j = 0
    P = [ 0, 0]

    # Llamado a imágenes necesarias
    Background = pygame.image.load("Pictures/Background.png")
    Slope_1 = pygame.image.load("Pictures/Slope_1.png")
    Slope_2 = pygame.image.load("Pictures/Slope_2.png")
    Play_1 = pygame.image.load("Pictures/Play_1b.png")
    Play_2 = pygame.image.load("Pictures/Play_2b.png")
    Return_1 = pygame.image.load("Pictures/Return_1.png")
    Return_2 = pygame.image.load("Pictures/Return_2.png")

    # Creación de Botones
    Button_1 = Button(Play_1, Play_2, 50, 40)
    Button_2 = Button(Return_1, Return_2, 150, 40)

    #Creacion de puntero
    Pointer_2 = Pointer()

    #Recorrido de eventos
    graphic = False; play = True
    while play:

        for event in pygame.event.get():
            #Salida segura
            if event.type == pygame.QUIT:
                sys.exit()
            #Seleccion de play
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_2.colliderect(Button_1.rect):
                    graphic = True
                #Seleccion de return
                if Pointer_2.colliderect(Button_2.rect):
                    Speedometer()
                    quit()

        #Actualizacion de objetos y creación de la trayectoria
        Clock_2.tick(V0)
        Screen_2.blit(Background, (0, 0))
        Screen_2.blit(Slope_1, (143, 370))
        Screen_2.blit(Slope_2, (1115, 370))
        if graphic is True:
            if j < 200:
                Plot(j, V0, P, Screen_2)
                j += 1
        Pointer_2.update()
        Button_1.update(Screen_2, Pointer_2, 0, 0)
        Button_2.update(Screen_2, Pointer_2, 0, 0)
        pygame.display.update()

#_____________________________________________ Definicion de Main y Speedometer para poder usar el boton return

def Speedometer():
    pygame.init()
    Screen_3 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 3")
    Clock_3 = pygame.time.Clock()

    V0 = 75

    Background = pygame.image.load("Pictures/Shadow_Speedometer.png")
    Play_1 = pygame.image.load("Pictures/Play_1b.png")
    Play_2 = pygame.image.load("Pictures/Play_2b.png")
    Return_1 = pygame.image.load("Pictures/Return_1.png")
    Return_2 = pygame.image.load("Pictures/Return_2.png")
    Decrease_1 = pygame.image.load("Pictures/Down_1.png")
    Decrease_2 = pygame.image.load("Pictures/Down_2.png")
    Increase_1 = pygame.image.load("Pictures/Up_1.png")
    Increase_2 = pygame.image.load("Pictures/Up_2.png")
    Arrow = pygame.image.load("Pictures/Pointer.png")
    Font = pygame.font.Font("BADABB__.TTF", 55)

    Button_1 = Button(Play_1, Play_2, 1300, 377)
    Button_2 = Button(Return_1, Return_2, 50, 377)
    Button_3 = Button(Decrease_1, Decrease_2, 290, 140)
    Button_4 = Button(Increase_1, Increase_2, 1030, 140)

    Pointer_3 = Pointer()

    def Speed(V0):
        text = Font.render(str(V0), True, (13, 71, 114))
        Screen_3.blit(text, (625, 350))

    play = True
    while play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_3.colliderect(Button_1.rect):
                    Game_loop(V0*2)
                    quit()
                if Pointer_3.colliderect(Button_2.rect):
                    Main()
                    quit()
                if Pointer_3.colliderect(Button_3.rect):
                    if(30 < V0):
                        V0 -= 5
                if Pointer_3.colliderect(Button_4.rect):
                    if(V0 < 180):
                        V0 += 5


        Clock_3.tick(100)
        Screen_3.blit(Background, (0, 0))
        if(30 <= V0 and V0 < 50):
            Screen_3.blit(pygame.transform.rotate(Arrow, 93), (617, 153))
        elif(50 <= V0 and V0 < 70):
            Screen_3.blit(pygame.transform.rotate(Arrow, 70), (617, 133))
        elif(70 <= V0 and V0 < 90):
            Screen_3.blit(pygame.transform.rotate(Arrow, 45), (637, 100))
        elif(90 <= V0 and V0 < 110):
            Screen_3.blit(pygame.transform.rotate(Arrow, 0), (687, 85))
        elif(110 <= V0 and V0 < 130):
            Screen_3.blit(pygame.transform.rotate(Arrow, -28), (687, 88))
        elif(130 <= V0 and V0 < 150):
            Screen_3.blit(pygame.transform.rotate(Arrow, -50), (683, 106))
        elif(150 <= V0 and V0 < 170):
            Screen_3.blit(pygame.transform.rotate(Arrow, -68), (687, 126))
        else:
            Screen_3.blit(pygame.transform.rotate(Arrow, -88), (687, 156))
        Speed(V0)
        Pointer_3.update()
        Button_1.update(Screen_3, Pointer_3, 0, 0)
        Button_2.update(Screen_3, Pointer_3, 0, 0)
        Button_3.update(Screen_3, Pointer_3, 0, 0)
        Button_4.update(Screen_3, Pointer_3, 0, 0)
        pygame.display.update()

#_____________________________________________

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
