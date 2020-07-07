# Introducción a las Ciencias de la Computación y la Programación
# Proyecto Final 2020-1
# Integrantes:
# Daniel Barrios Calderón, Andrés Felipe Duque Bran
# En este código se definen las clases para la interacción de los objetos en la ventana.

import pygame

# Esta clase permite definir la interacción del puntero con los objetos en la ventana.
class Pointer(pygame.Rect):
     def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
     def update(self):
        self.left, self.top = pygame.mouse.get_pos()

# Esta clase permite definir la interacción de los botones con el puntero.
class Button(pygame.sprite.Sprite):
     def __init__(self, picture_1, picture_2, x, y):
        self.standard_picture = picture_1
        self.selected_picture = picture_2
        self.current_picture = self.standard_picture
        self.rect = self.current_picture.get_rect()
        self.rect.left, self.rect.top = (x, y)
     
     def update(self, Screen, Pointer, dx, dy):
        if Pointer.colliderect(self.rect):
            self.current_picture = self.selected_picture
            Screen.blit(self.current_picture, (self.rect.left + dx, self.rect.top + dy))
        else:
            self.current_picture = self.standard_picture
            Screen.blit(self.current_picture, self.rect)