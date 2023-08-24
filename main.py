# Importando librería de Pygame.
import pygame
import random
import math
from pygame import mixer

pygame.init()

# Resolución de la ventana del videojuego.
screen_width = 800
screen_height = 600

size = (screen_width, screen_height)

# Definir el tamaño de la ventana con Pygame.
screen = pygame.display.set_mode(size)

# Agregando el fondo de pantalla.
background = pygame.image.load("assets\FondoEspacio.png")

# Música de fondo.
mixer.music.load("Bonetrousle Undertale.wav")
mixer.music.play(-1)

bullet_sound = mixer.Sound("shoot-ship.wav")
bullet_sound.set_volume(0.5)

explosion_sound = mixer.Sound("hit-enemy.wav")
explosion_sound.set_volume(0.2)

# Definir el título de la ventana.
pygame.display.set_caption("Kyle neko under the space")

# Ícono de la ventana.
icon = pygame.image.load("assets\wool64x64.png")

pygame.display.set_icon(icon)

# Balas.
bullet_img = pygame.image.load("assets\wool64x64.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

score = 0
score_text = pygame.font.Font("score_text.ttf", 32)
score_x = 10
score_y = 10

# Función del puntaje.
def show_score(x, y):
    text_score = score_text.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text_score, (x, y))

# Coordenadas del jugador.
player_x = 365
player_y = 480
player_img = pygame.image.load("assets\kyle64x64.png")
player_x_change = 0

# Coordenadas del Boss.
boss_x = 0
boss_y = 0
boss_img = pygame.image.load("assets\Kyra47.png")
boss_x_change = 0.1
boss_y_change = 0.1
boss_life = 3

# Balas del jefe
bullet_boss_img = pygame.image.load("boots64x64.png")
bullet_boss_x = 50
bullet_boss_y = 0
bullet_boss_x_change = 0
bullet_boss_y_change = 10
bullet_boss_state = "ready"


# Patrones de movimiento del jefe
movimiento = ['basico','arriba y abajo','basico'] 

# Variable para decidir el patrón del enemigo
boss_num_random = 0
boss_random_move = 0
patron = 'Cambio'

# Fuente para la pantalla de Game Over.
go_font = pygame.font.Font("score_text.ttf", 64)
go_x = 250
go_y = 250

# Lista de parámetros para múltiples enemigos.
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

number_enemies = 2  

# Agregando al enemigo.
for item in range(number_enemies):
    enemy_img.append(pygame.image.load("assets\mutant64x64.png"))
    enemy_x.append(random.randint(0, 730))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(30)

# Función para llamar al personaje en el Game Loop.
def player(x, y):
    screen.blit(player_img, (x, y))

# Función del enemigo.
def enemy(x, y):
    screen.blit(enemy_img[item], (x, y))

# Función del jefe KYRA
def boss(x, y):
    screen.blit(boss_img, (x, y))

# Función de disparo de la nave.
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Función de disparo de la nave.
def fireBoss(x, y):
    global bullet_boss_state
    bullet_boss_state = "fire"
    screen.blit(bullet_boss_img, (x + 16, y + 10))

# patron del jefe Boss

def patron_boss (num_random):
    global patron, boss_x, boss_y, boss_x_change, boss_y_change
    if patron == "Cambio":
        for i in range(len(movimiento)):
            if i == num_random:
                patron = movimiento[i]
                # print(patron)
                # patron = 'arriba y abajo'
    elif patron == 'basico':  
        if boss_y >= 70:
            boss_y = random.randint(50,100)
            boss_x = random.randint(50,100)
            patron = "Cambio"
                        
        if boss_x <= 0:
                    boss_x_change = 0.5
                    boss_y_change = 40
                    boss_y += boss_y_change
                        
        elif boss_x >= 736:
            boss_x_change = -0.5
            boss_y_change = 40
            boss_y += boss_y_change

        boss_x += boss_x_change
    elif patron == 'arriba y abajo':
                
        if boss_x >= 726:
                    boss_x = 0
                    boss_y = 0
                    patron = "Cambio"
                
        if boss_x >= 125 :
                    boss_y -=  math.acos(boss_x_change)
                    boss_x +=  math.cos(boss_x_change)

        if boss_x >= 200 :
                    boss_y +=  math.cos(boss_x_change)
                    boss_x +=  math.cos(boss_x_change)

        if boss_x >= 400 :
                    boss_y -=  math.acos(boss_x_change)
                    boss_x +=  math.cos(boss_x_change)

        if boss_x >= 600 :
                    boss_y +=  math.cos(boss_x_change)
                    boss_x +=  math.cos(boss_x_change)

        if boss_y >= 200:
                     boss_y -=  math.acos(boss_x_change)
                     boss_x +=  math.cos(boss_x_change)

        if boss_y <= 10 :
                    boss_y += math.cos(boss_x_change)
                    boss_x += math.acos(boss_x_change)

        if boss_y <= 0 :
                    boss_y += math.cos(boss_x_change)
                    boss_x += math.acos(boss_x_change)
                        
        if boss_y >= 100 :
                    boss_y += math.cos(boss_x_change)
                    boss_x += math.acos(boss_x_change)
                    

                # boss_y += boss_y_change
        boss_y += math.cos(boss_x_change)
        boss_x += math.acos(boss_x_change)

# Función de la colisión al disparar. 
def is_collision (enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)

    if distance < 27:
        return True
    else:
        return False

# Función de Game Over.
def game_over(x, y):
    go_text = go_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(go_text, (x, y))

def you_win (x, y) :
    go_text = go_font.render(f"YOU WIN! SCORE {score}", True, (255, 255, 255))
    screen.blit(go_text, (x, y))

# Game loop: para correr y retener el videojuego.
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Movimiento al presionar la tecla izquierda.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -10
            if event.key == pygame.K_RIGHT:
                player_x_change = 10
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_x = player_x
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("shoot-ship.wav")
                    bullet_sound.set_volume(0.15)
                    bullet_sound.play()
                    bullet_x = player_x
                fire (bullet_x, bullet_y)

# Movimiento al dejar de presionar la tecla izquierda.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

# Color del fondo de pantalla.
    rgb = (41, 60, 94)
    screen.fill(rgb)
    screen.blit(background, (0, 0))
    player_x += player_x_change

# Límites de la nave en pantalla.
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Comprobar si se llegó al score para que se genere el boss
    if score == 10:
        for life in range(boss_life):  
            boss_random_move = random.randint(0,2)
            
            patron_boss(boss_random_move)
            
            collision = is_collision(boss_x, boss_y, bullet_x, bullet_y)

            if collision:
                bullet_y = 480
                bullet_state = "ready"
                boss_life -= 1
                explosion_sound.play()
                explosion_sound.set_volume(0.2)
                if boss_life <= 0 :
                    break
            
            boss_num_random = random.randint(0,100)
            if boss_num_random == 1 and bullet_boss_state == 'ready':
                bullet_boss_x = boss_x
                if bullet_boss_state == "ready":
                    bullet_sound = mixer.Sound("shoot-ship.wav")
                    bullet_sound.set_volume(0.15)
                    bullet_sound.play()
                    bullet_boss_x = boss_x
                fireBoss (bullet_boss_x, bullet_boss_y)

             # Carga de la bala del jefe
            if bullet_boss_state == "fire":
                fireBoss(bullet_boss_x, bullet_boss_y)
                bullet_boss_y += bullet_boss_y_change
            
            if bullet_boss_y >= 536:
                bullet_boss_y = 20
                bullet_boss_state = "ready"
            
            collision_player = is_collision(player_x, player_y, bullet_boss_x, bullet_boss_y)

            if collision_player:
                bullet_boss_y = 30
                bullet_boss_state = "ready"
                explosion_sound.play()
                explosion_sound.set_volume(0.2)
                
                game_over(go_x, go_y)
                break
                

            boss(boss_x, boss_y)
    else:
    # límites/generación del enemigo.
        for item in range(number_enemies):
            if enemy_y[item] > 440:
                for j in range(number_enemies):
                    enemy_y[j] = 2000
                game_over(go_x, go_y)
                    
                break

            enemy_x[item] += enemy_x_change[item]

            if enemy_x[item] <= 0:
                enemy_x_change[item] = 4
                enemy_y[item] += enemy_y_change[item]
            
            elif enemy_x[item] >= 736:
                enemy_x_change[item] = -4
                enemy_y[item] += enemy_y_change[item]

    # Colisiones de disparo hacia el enemigo.
            collision = is_collision(enemy_x[item], enemy_y[item], bullet_x, bullet_y)

            if collision:
                bullet_y = 480
                bullet_state = "ready"
                score += 5
                enemy_x[item] = random.randint(0, 735)
                enemy_y[item] = random.randint(50, 150)
                explosion_sound.play()
                explosion_sound.set_volume(0.2)
            
            enemy(enemy_x[item], enemy_y[item])


# Balas/disparo posicionamiento y llamado al Game Loop.
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

   

    show_score(score_x, score_y)

    if boss_life == 0 :
        you_win(go_x, go_y)
    

    player(player_x, player_y)
    clock.tick(60)
    pygame.display.update()
pygame.quit()