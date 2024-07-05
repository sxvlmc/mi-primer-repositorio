
import pygame
import random
import os

#directorio principal
carpeta_juego = os.path.dirname(__file__)
#directorio de imagenes principal
carpeta_imagenes = os.path.join(carpeta_juego, 'imagenes')
#sub directorio de imagenes
carpeta_imagenes_enemigos = os.path.join(carpeta_imagenes, 'enemigos')
carpeta_imagenes_jugador = os.path.join(carpeta_imagenes, 'jugador')
carpeta_imagenes_explosiones = os.path.join(carpeta_imagenes, 'explosiones')

#tamaño de pantalla
ANCHO = 800
ALTO = 600

#FPS
FPS = 30

#Paleta de colores
BLANCO = (255, 255, 255,)
NEGRO = (0, 0, 0)
ROJO = (255,0 , 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
H_FA2F2F = (250, 47, 47)
H_50D2FE =(94, 210, 254)
AZUL2 = (64, 64, 255)


#Fuentes
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

#sonido
pygame.mixer.init()

class Jugador(pygame.sprite.Sprite):
    #sprite del jugador
    def __init__(self):
        #heredamos el init de la clase sprite pygame
        super().__init__()
        #rectangulo (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'nave.png')).convert()

        self.image.set_colorkey(AZUL2)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 27
        
        #centra el rectangulo (sprite)
        self.rect.center = (400, 600)
        
        #velocidad del personaje (inicial)
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Disparos
        self.cadencia = 750
        self.ultimo_disparo = pygame.time.get_ticks()
        self.hp = 100
        self.vidas = 3


    def update(self):
            #velocidad predeterminada cada vuelta del bucle si no pulsas nada 
            self.velocidad_x = 0
            self.velocidad_y = 0

            # mantiene las teclas pulsadas
            teclas = pygame.key.get_pressed()

            #mueve el personaje a la izquierda
            if teclas[pygame.K_a]:
                self.velocidad_x = -10

            #mueve el personaje a la derecha
            if teclas[pygame.K_d]:
                self.velocidad_x = 10

            #mueve el personaje arriba
            if teclas[pygame.K_w]:
                self.velocidad_y = -10

            #mueve el personaje abajo
            if teclas[pygame.K_s]:
                self.velocidad_y = 10
            #disparos
            if teclas[pygame.K_SPACE]:
                ahora = pygame.time.get_ticks()
                if ahora - self.ultimo_disparo > self.cadencia:
                    self.disparo()
                    self.disparo2()
                    self.disparo3()  
                    self.ultimo_disparo = ahora
                


            # actualiza la posicion del personaje
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            #limita margen a la izquierda
            if self.rect.left < 0:
                self.rect.left = 0
                 
            # limita margen a la derecha
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO

            # limita margen inferior
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO

            # limita margen superior
            if self.rect.top < 0:
                self.rect.top = 0

    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top + 20)
        balas.add(bala)
    
    def disparo2(self):
        bala = Disparos(self.rect.centerx + 23, self.rect.top + 30)
        balas.add(bala)

    def disparo3(self):
        bala = Disparos(self.rect.centerx - 23, self.rect.top + 30)
        balas.add(bala)
        




class EnemigosAmarillos(pygame.sprite.Sprite):
    def __init__(self):
        #heredamos el init de la clase sprite pygame
        super().__init__()
        #rectangulo (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo1.png')).convert()

        self.image.set_colorkey(AZUL2)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)
        self.radius = 48
        
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.velocidad_x = random.randrange(1, 3)
        self.velocidad_y = random.randrange(1, 3)
        self.hp = 15

    def update(self):
        #actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #limita margen a la izquierda
        if self.rect.left < 0:
                self.velocidad_x += 1
        
                 
         # limita margen a la derecha
        if self.rect.right > ANCHO:
                self.velocidad_x -= 1

         # limita margen inferior
        if self.rect.bottom > ALTO:
                self.velocidad_y -= 1

        # limita margen superior
        if self.rect.top < 0:
                self.velocidad_y += 1

class EnemigosVerdes(pygame.sprite.Sprite):
    def __init__(self):
        #heredamos el init de la clase sprite pygame
        super().__init__()
        #rectangulo (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo2.png')).convert()

        self.image.set_colorkey(AZUL2)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)
        self.radius = 48
        
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.velocidad_x = random.randrange(3, 5)
        self.velocidad_y = random.randrange(3, 5)
        self.hp = 30

    def update(self):
        #actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #limita margen a la izquierda
        if self.rect.left < 0:
                self.velocidad_x += 1
        
                 
         # limita margen a la derecha
        if self.rect.right > ANCHO:
                self.velocidad_x -= 1

         # limita margen inferior
        if self.rect.bottom > ALTO:
                self.velocidad_y -= 1

        # limita margen superior
        if self.rect.top < 0:
                self.velocidad_y += 1


class EnemigosAzules(pygame.sprite.Sprite):
    def __init__(self):
        #heredamos el init de la clase sprite pygame
        super().__init__()
        #rectangulo (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo3.png')).convert()

        self.image.set_colorkey(AZUL2)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)
        self.radius = 48
        
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.velocidad_x = random.randrange(5, 10)
        self.velocidad_y = random.randrange(5, 10)
        self.hp = 45

    def update(self):
        #actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #limita margen a la izquierda
        if self.rect.left < 0:
                self.velocidad_x += 1
        
                 
         # limita margen a la derecha
        if self.rect.right > ANCHO:
                self.velocidad_x -= 1

         # limita margen inferior
        if self.rect.bottom > ALTO:
                self.velocidad_y -= 1

        # limita margen superior
        if self.rect.top < 0:
                self.velocidad_y += 1


class EnemigosRojos(pygame.sprite.Sprite):
    def __init__(self):
        #heredamos el init de la clase sprite pygame
        super().__init__()
        #rectangulo (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo3.png')).convert()

        self.image.set_colorkey(AZUL2)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)
        self.radius = 48
        
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.velocidad_x = random.randrange(10, 15)
        self.velocidad_y = random.randrange(10, 15)
        self.hp = 75

    def update(self):
        #actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #limita margen a la izquierda
        if self.rect.left < 0:
                self.velocidad_x += 1
        
                 
         # limita margen a la derecha
        if self.rect.right > ANCHO:
                self.velocidad_x -= 1

         # limita margen inferior
        if self.rect.bottom > ALTO:
                self.velocidad_y -= 1

        # limita margen superior
        if self.rect.top < 0:
                self.velocidad_y += 1


class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'disparo.png')).convert(), (10, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
    def update(self):
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()
'''
class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load('imagenes/meteorito.png').convert(), (100, 100))
            self.radius = 50
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load('imagenes/meteorito.png').convert(), (50, 50))
            self.radius = 25
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load('imagenes/meteorito.png').convert(), (25, 25))
            self.radius = 12
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()     
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocidad_y = random.randrange(1, 10)   

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = -self.rect.width
            # ANCHO
            self.velocidad_y = random.randrange(1, 10)
'''
class Explosiones(pygame.sprite.Sprite):
    def __init__(self, centro, dimensiones):
        pygame.sprite.Sprite.__init__(self)
        self.dimensiones = dimensiones
        self.image = animacion_explosion1[self.dimensiones][0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.fotograma = 0
        self.frecuencia_fotograma = 35
        self.actualizacion = pygame.time.get_ticks()

    def update(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.actualizacion > self.frecuencia_fotograma:
            self.actualizacion = ahora
            self.fotograma +=1
            if self.fotograma == len(animacion_explosion1[self.dimensiones]):
                self.kill()
            else:
                centro = self.rect.center
                self.image = animacion_explosion1[self.dimensiones][self.fotograma]
                self.rect = self.image.get_rect()
                self.rect.center = centro



#inicializacion  de pygame, creacion de la ventana, titulo y control del juego
pygame.init()
Pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('trabajando con sprites')
clock = pygame.time.Clock()

#sistema de puntuaciones
puntuacion = 0


#explosiones
animacion_explosion1 = {'t1': [], 't2': [], 't3': [], 't4': []}

for x in range(24):
    archivo_explosiones = f'expl_01_00{x:02d}.png'
    imagenes = pygame.image.load(os.path.join(carpeta_imagenes_explosiones, archivo_explosiones))
    imagenes.set_colorkey(NEGRO)
    imagenes_t1 = pygame.transform.scale(imagenes, (32, 32))
    animacion_explosion1['t1'].append(imagenes_t1)
    imagenes_t2 = pygame.transform.scale(imagenes, (64, 64))
    animacion_explosion1['t2'].append(imagenes_t2)
    imagenes_t3 = pygame.transform.scale(imagenes, (128, 128))
    animacion_explosion1['t3'].append(imagenes_t3)
    imagenes_t4 = pygame.transform.scale(imagenes, (256, 256))
    animacion_explosion1['t4'].append(imagenes_t4)
    
def barra_hp(Pantalla, x, y, hp):
    largo = 200
    ancho = 25
    calculo_barra = int((jugador.hp / 100) * largo)
    borde = pygame.Rect(x, y, largo, ancho)
    rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
    pygame.draw.rect(Pantalla, AZUL2, borde, 3)
    pygame.draw.rect(Pantalla, H_50D2FE, rectangulo)
    




def muestra_texto(Pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    Pantalla.blit(superficie, rectangulo)

#grupo de sprites, instanciando del otro jugador 
sprites = pygame.sprite.Group()
enemigos_amarillos = pygame.sprite.Group()
enemigos_verdes = pygame.sprite.Group()
enemigos_azules = pygame.sprite.Group()
enemigos_rojos = pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()
explosiones = pygame.sprite.Group()


jugador = Jugador()
sprites.add(jugador)

enemigo1 = EnemigosAmarillos()
enemigos_amarillos.add(enemigo1)

enemigo2 = EnemigosVerdes()
enemigos_verdes.add(enemigo2)

enemigo3 = EnemigosAzules()
enemigos_azules.add(enemigo3)

enemigo4 = EnemigosRojos()
enemigos_rojos.add(enemigo4)
'''
for x in range(10):
    meteorito = Meteoritos()
    meteoritos.add(meteorito)
    '''




#bucle del juego
ejecutando = True
while ejecutando:
    #es lo que especifica la velocidad del bucle del juego
    clock.tick(FPS)
    #EVENTOS
    for event in pygame.event.get():
        #se cierra  y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    #Actualizacion de sprites
    sprites.update()
    enemigos_amarillos.update()
    enemigos_verdes.update()
    enemigos_azules.update()
    enemigos_rojos.update()
    balas.update()
    meteoritos.update()
    explosiones.update()



    

    r = random.randrange(1, 4)
    
    colision_nave1 = pygame.sprite.spritecollide(jugador, enemigos_amarillos, True, pygame.sprite.collide_circle)
    if colision_nave1:
        explosion = Explosiones(enemigo1.rect.center, f't{r}')
        explosiones.add(explosion)
        jugador.hp -= 15
        if puntuacion >= 0:
            puntuacion -= 100
            if puntuacion < 0:
                puntuacion = 0
        else:
            puntuacion = puntuacion
        

    colision_nave2 = pygame.sprite.spritecollide(jugador, enemigos_verdes, True, pygame.sprite.collide_circle)
    if colision_nave2:
        explosion = Explosiones(enemigo2.rect.center, f't{r}')
        explosiones.add(explosion)
        jugador.hp -= 25
        if puntuacion >= 0:
            puntuacion -= 75
            if puntuacion < 0:
                puntuacion = 0
        else:
            puntuacion = puntuacion

    colision_nave3 = pygame.sprite.spritecollide(jugador, enemigos_azules, True, pygame.sprite.collide_circle)
    if colision_nave3:
        explosion = Explosiones(enemigo3.rect.center, f't{r}')
        explosiones.add(explosion)
        jugador.hp -= 35
        if puntuacion >= 0:
            puntuacion -= 50
            if puntuacion < 0:
                puntuacion = 0
        else:
            puntuacion = puntuacion

    colision_nave4 = pygame.sprite.spritecollide(jugador, enemigos_rojos, True, pygame.sprite.collide_circle)
    if colision_nave4:
        explosion = Explosiones(enemigo4.rect.center, f't{r}')
        explosiones.add(explosion)
        jugador.hp -= 50
        if puntuacion >= 0:
            puntuacion -= 25
            if puntuacion < 0:
                puntuacion = 0
        else:
            puntuacion = puntuacion

    colision_disparo_amarillos = pygame.sprite.groupcollide(enemigos_amarillos, balas, False, True, pygame.sprite.collide_circle)

    if colision_disparo_amarillos:
        puntuacion +=10
        explosion = Explosiones(enemigo1.rect.center, f't{r}')
        explosiones.add(explosion)
        enemigo1.hp -= 5
    if enemigo1.hp <= 0:
        enemigo1.kill()

    colision_disparo_verdes = pygame.sprite.groupcollide(enemigos_verdes, balas, False, True, pygame.sprite.collide_circle) 

    if colision_disparo_verdes:
        puntuacion +=25
        explosion = Explosiones(enemigo2.rect.center, f't{r}')
        explosiones.add(explosion)
        enemigo2.hp -= 5
    if enemigo2.hp <= 0:
        enemigo2.kill()


    colision_disparo_azules = pygame.sprite.groupcollide(enemigos_azules, balas, False, True, pygame.sprite.collide_circle)

    if colision_disparo_azules:
        puntuacion +=50
        explosion = Explosiones(enemigo3.rect.center, f't{r}')
        explosiones.add(explosion)
        enemigo3.hp -= 5
    if enemigo3.hp <= 0:
        enemigo3.kill()


    colision_disparo_rojos = pygame.sprite.groupcollide(enemigos_rojos, balas, False, True, pygame.sprite.collide_circle)

    if colision_disparo_rojos:
        puntuacion +=75
        explosion = Explosiones(enemigo4.rect.center, f't{r}')
        explosiones.add(explosion)
        enemigo4.hp -= 5
    if enemigo4.hp <= 0:
        enemigo4.kill()
    

    warning = pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'warning.png')).convert()
    muerte_3 = Pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (510, 15))
    muerte_2 = Pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (475, 15))
    muerte_1 = Pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (440, 15))
    cruz = pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'cruz.png')).convert()
    


    if jugador.hp < 30:
        Pantalla.blit(pygame.transform.scale(warning, (25, 25)), (545, 15))

    
    if jugador.hp < 0 and jugador.vidas == 3:
        jugador.kill()
        jugador = Jugador()
        sprites.add(jugador)
        jugador.vidas = 2

    if jugador.vidas == 2:
        if jugador.hp <= 0:
            jugador.kil()  
            jugador = Jugador()
            sprites.add(jugador)
            jugador.vidas = 1
        muerte_1 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (510, 15))

    if jugador.vidas == 1:
        if jugador.hp <= 0:
            jugador.kill()
            jugador = Jugador()
            sprites.add(jugador)
            jugador.vidas = 0
        muerte_1 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (510, 15))
        muerte_2 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (475, 15))
    
    if jugador.vidas == 0:
        if jugador.hp <= 0:
            jugador.kill()
            jugador.hp = 0
        muerte_1 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (510, 15))
        muerte_2 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (475, 15))
        muerte_3 = Pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (440, 15))
        break
    

        



    if not enemigos_amarillos and not enemigos_verdes and not enemigos_azules and not enemigos_rojos:
        enemigo1 = EnemigosAmarillos()
        enemigos_amarillos.add(enemigo1)

        enemigo2 = EnemigosVerdes()
        enemigos_verdes.add(enemigo2)

        enemigo3 = EnemigosAzules()
        enemigos_azules.add(enemigo3)

        enemigo4 = EnemigosRojos()
        enemigos_rojos.add(enemigo4)



    '''
    if colision_nave:
        print('colision de la nave')

    if colision_disparo:
        print('colision por disparo')
        '''

    

    #fondo de pantalla, dibujo de sprites y formas geometricas.
    Pantalla.fill(NEGRO)
    sprites.draw(Pantalla)
    enemigos_amarillos.draw(Pantalla)
    enemigos_verdes.draw(Pantalla)
    enemigos_azules.draw(Pantalla)
    enemigos_rojos.draw(Pantalla)
    balas.draw(Pantalla)
    meteoritos.draw(Pantalla)
    explosiones.draw(Pantalla)
    pygame.draw.line(Pantalla, H_50D2FE, (400, 0 ), (400, 800), 1)
    pygame.draw.line(Pantalla, AZUL, (0, 300), (800, 300), 1)
    #actualiza el contenido de la pantalla
    pygame.display.flip()

    # dibuja los textos en la pantalla
    muestra_texto(Pantalla, consolas, str(puntuacion).zfill(7), ROJO, 40, 700, 50)
    barra_hp(Pantalla, 580, 15, jugador.hp)
    pygame.display.update()

pygame.quit()