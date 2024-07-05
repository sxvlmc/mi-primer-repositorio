import pygame
import sys

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Exterminator')
icono=pygame.image.load('imagenes/icono informatica.jpg')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('imagenes/ciudad.png')

# Música de fondo
pygame.mixer.music.load('sonido/Intergalactic Odyssey.ogg')
pygame.mixer.music.play(-1)


# Personaje
quieto = pygame.image.load('imagenes/idle1.png')

camina_derecha = [pygame.image.load('imagenes/run1.png'),
				pygame.image.load('imagenes/run2.png'),
				pygame.image.load('imagenes/run3.png'),
				pygame.image.load('imagenes/run4.png'),
				pygame.image.load('imagenes/run5.png'),
				pygame.image.load('imagenes/run6.png')]



salta = [pygame.image.load('imagenes/jump1.png'),
		pygame.image.load('imagenes/jump2.png')]

# Sonido
sonido_arriba = pygame.image.load('sonido/volume_up.png')
sonido_abajo = pygame.image.load('sonido/volume_down.png')
sonido_mute = pygame.image.load('sonido/volume_muted.png')
sonido_max = pygame.image.load('sonido/volume_max.png')

x=0
px = 50
py = 200
ancho = 40
velocidad = 10
#control de fps
RELOJ = pygame.time.Clock()
#variable de salto
salto = False
#altura del salto
cuanto_salta = 10
#variables direccion
derecha = False
#pasos
cuenta_pasos = 0
#movimiento
def recargar_pantalla():
    #variables globales
    global cuenta_pasos
    global x

#fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width , 0))
    if x_relativa < W:
        PANTALLA.blit(fondo,(x_relativa, 0))
    x -= 5
#contador de pasos
    if cuenta_pasos + 1 >= 6:
        cuenta_pasos = 0
    #movimiento a la derecha
    elif derecha:
        PANTALLA.blit(camina_derecha[cuenta_pasos // 1], (int(px), int(py)))
    
    elif salto + 1 >= 2:
        cuenta_pasos = 0
        PANTALLA.blit(salta[cuenta_pasos // 1], (int(px), int(py)))

    else:
        PANTALLA.blit(quieto,(int(px), int(py)))
    
    #actualizacion de la pantalla
    pygame.display.update()



ejecuta = True

#bucle de acciones y controles
while ejecuta:
    #FPS
    RELOJ.tick(18)

    #bucle del juego 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    #Opcion tecla pulsada
    keys = pygame.key.get_pressed()

    #Tecla A - Movimiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = False
        derecha = True
     
    #Tecla D - Movimiento a la derecha
    if keys[pygame.K_d] and px < 900 - velocidad - ancho:
        px += velocidad
        izquierda = True
    #personaje quieto
    else:
        izquierda = False
        derecha = False
        cuenta_pasos = 0
    #tecla W - Movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad
    #tecla S - Movimiento hacia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
    #tecla SPACE -Salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuenta_pasos = 0
    else:
        if cuenta_pasos >= 10:
            py -= (cuanto_salta * abs(cuanto_salta)) * 0.5
            cuanto_salta -= 1
        else:
            cuanto_salta = 10
            salto = False
    #control del audios
    #sube volumen
    if keys[pygame.K_0]:
        if pygame.mixer.music.get_volume() < 1.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        if pygame.mixer.music.get_volume() == 1.0:
            PANTALLA.blit(sonido_max, (850, 25))
        else:
            PANTALLA.blit(sonido_max, (850, 25))
 
        #baja volumen 
    elif keys[pygame.K_9]:
        if pygame.mixer.music.get_volume() > 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        if pygame.mixer.music.get_volume() == 0.0:
            PANTALLA.blit(sonido_mute, (850, 25))
        else:
            PANTALLA.blit(sonido_mute, (850, 25))

        PANTALLA.blit(sonido_mute, (850, 25))

    #desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25 ))

    #reactivar sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (850, 25))



    
    #Llamada a la funcion de actualizacion de la ventana
    recargar_pantalla()


#salida del juego 
pygame.quit()

