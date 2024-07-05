import pygame, sys
from pygame.locals import*
pygame.init()

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('primer juego')

BLANCO = (255, 255, 255,)
NEGRO = (0, 0, 0)
ROJO = (255,0 , 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

PANTALLA.fill(VERDE)

RECTANGULO1 = pygame.draw.rect(PANTALLA, ROJO, (100, 50, 100, 50))
print(RECTANGULO1)
pygame.draw.line(PANTALLA, AZUL, (100, 104), (199, 104),10)
pygame.draw.circle(PANTALLA, NEGRO, (122, 250), 20, 0)
pygame.draw.ellipse(PANTALLA, H61CD35, (275, 200, 40, 80),10)

PUNTOS = [(100,300), (100,100), (150, 100)]
pygame.draw.polygon(PANTALLA, (0, 150, 255), PUNTOS, 8)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()