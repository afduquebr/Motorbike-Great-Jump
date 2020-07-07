# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# Este código permite graficar el movimiento del motociclista.

import pygame
import math

from Model import Motorbike
from Model import Motorbikeb
from Model import Angle
from Model import Rect

#Llamado a imágenes necesarias
Init_Biker = pygame.image.load("Pictures/Init_Biker.png")
Jumping_Biker = pygame.image.load("Pictures/Jumping_Biker.png")
End_Biker = pygame.image.load("Pictures/End_Biker.png")
Fall = pygame.image.load("Pictures/Fall.png")
Gone = pygame.image.load("Pictures/Gone.png")
Celebration = pygame.image.load("Pictures/Celebration.png")

def Plot(j, V0, P, Screen_2):
    u = math.pi / 6
    #Gráfica de la subida de la rampa
    if (j < 10):
        Screen_2.blit(pygame.transform.rotate(Init_Biker, u * 180 / math.pi), Rect([82, 417, 210, 340])[j])
    #Grafica de la trayectoria de la moto en el aire
    elif (10 <= j and j < 60):
        #Trayectoria sin acrobacia
        if (Motorbike(V0)[j - 10][1] <= 320 and Motorbike(V0)[j - 10][1] > 280):
            Screen_2.blit(pygame.transform.rotate(Init_Biker, Angle(Motorbikeb(V0), (u * 180 / math.pi))[j - 10]),
                          Motorbike(V0)[j - 10])
        #Trayectoria con acrobacia
        else:
            Screen_2.blit(pygame.transform.rotate(Jumping_Biker, Angle(Motorbikeb(V0), (u * 180 / math.pi))[j - 10]), Motorbike(V0)[j - 10])
            #Guardado de una posicion para desplegar onomatopeya en ciertos casos de velocidad
                #Si se va por el lado derecho
            if (260 <= V0 and V0 < 290):
                if (1320 <= Motorbike(V0)[j - 10][0] and Motorbike(V0)[j - 10][0] < 1350):
                    P[0] = Motorbike(V0)[j - 10][0] - 70
                    P[1] = Motorbike(V0)[j - 10][1]
                #Si se va por la parte superior
            elif (290 <= V0):
                if (-100 <= Motorbike(V0)[j - 10][1] and Motorbike(V0)[j - 10][1] < 0 and Motorbike(V0)[j - 10][0] < 1270):
                    P[0] = Motorbike(V0)[j - 10][0]
                    P[1] = Motorbike(V0)[j - 10][1] + 110
    #Grafica de la caida de la moto al terminar la trayectoria
    elif (60 <= j):
        #Si cae en los cactus
        if (V0 < 220):
            Screen_2.blit(Fall, (Motorbike(V0)[49][0] + 30, 220))
            Screen_2.blit(pygame.transform.rotate(Init_Biker, Angle(Motorbikeb(V0), (u * 180 / math.pi))[49]), (Motorbike(V0)[49][0] + 5, 335))
        #Si logra llegar
        elif (220 <= V0 and V0 < 230):
            if (j < 70):
                Screen_2.blit(pygame.transform.rotate(Init_Biker, 295), Rect([Motorbike(V0)[49][0], 320, Motorbike(V0)[49][0] + 60, 417])[j - 60])
            else:
                Screen_2.blit(End_Biker, (Motorbike(V0)[49][0] + 73, 400))
                Screen_2.blit(Celebration, (1200, 270))
        #Si cae delante de la rampa
        elif (230 <= V0 and V0 < 260):
            if (j < 70):
                Screen_2.blit(pygame.transform.rotate(Init_Biker, 295), Rect([Motorbike(V0)[49][0], 320, Motorbike(V0)[49][0] + 60, 417])[j - 60])
            else:
                Screen_2.blit(pygame.transform.rotate(Init_Biker, 295), (Motorbike(V0)[49][0] + 63, 413))
                Screen_2.blit(Fall, (Motorbike(V0)[49][0] - 35, 300))
        #Si se va por la lateral
        elif (260 <= V0 and V0 < 290):
            print(P)
            Screen_2.blit(Gone, P)
        #Si se va por la parte superior
        else:
            print(P)
            Screen_2.blit(Gone, P)
