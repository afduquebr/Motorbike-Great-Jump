# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite seleccionar la velocidad del movimiento.

import sys
import pygame

from Classes import Pointer
from Classes import Button
from Game import Game_loop


def Speedometer():
    # Inicio de la ventana
    pygame.init()
    Screen_3 = pygame.display.set_mode((1400, 467))
    pygame.display.set_caption("Screen 3")
    Clock_3 = pygame.time.Clock()

    #Inicio de la velocidad
    V0 = 75

    # Llamado a imágenes necesarias
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

    #Definicion de la fuente
    Font = pygame.font.Font("BADABB__.TTF", 55)

    # Creación de Botones
    Button_1 = Button(Play_1, Play_2, 1300, 377)
    Button_2 = Button(Return_1, Return_2, 50, 377)
    Button_3 = Button(Decrease_1, Decrease_2, 290, 140)
    Button_4 = Button(Increase_1, Increase_2, 1030, 140)

    #Creacion del puntero
    Pointer_3 = Pointer()

    #Funcion que imprime el valor de la velocidad
    def Speed(V0):
        text = Font.render(str(V0), True, (13, 71, 114))
        Screen_3.blit(text, (625, 350))

    #Recorrido de los eventos
    play = True
    while play:
        for event in pygame.event.get():
            #Salida segura
            if event.type == pygame.QUIT:
                sys.exit()
            #Seleccion de play
            if event.type == pygame.MOUSEBUTTONUP:
                if Pointer_3.colliderect(Button_1.rect):
                    Game_loop(V0*2)
                    quit()
                #Seleccion de return
                if Pointer_3.colliderect(Button_2.rect):
                    Main()
                    quit()
                #Disminucion de velocidad
                if Pointer_3.colliderect(Button_3.rect):
                    if(30 < V0):
                        V0 -= 5
                #Aumento de velocidad
                if Pointer_3.colliderect(Button_4.rect):
                    if(V0 < 180):
                        V0 += 5

        #Actualizacion de objetos
        Clock_3.tick(100)
        Screen_3.blit(Background, (0, 0))
        #Rotacion de puntero de velocidad
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

#__________________________________________________ Definicion de Main para poder usar return

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
