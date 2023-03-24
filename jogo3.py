import pygame
import random

# inicializa o Pygame
pygame.init()

# define as dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# cria a janela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# define o título da janela
pygame.display.set_caption('Jogo de Corrida')

# define as cores que serão utilizadas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# define a fonte utilizada
font = pygame.font.SysFont(None, 25)

# define a velocidade dos carros
CAR_SPEED = 5

# carrega a imagem do carro
car_image = pygame.image.load('img/car.png')

# define as coordenadas iniciais do carro
car_x = SCREEN_WIDTH / 2 - car_image.get_width() / 2
car_y = SCREEN_HEIGHT - car_image.get_height() - 10

# define as coordenadas iniciais dos obstáculos
obstacle_x = random.randint(0, SCREEN_WIDTH - 50)
obstacle_y = -50

# define a pontuação inicial
score = 0

# define se o jogo está rodando ou não
running = True

# loop principal do jogo
while running:

    # verifica se o jogador quer sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move o carro de acordo com as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= CAR_SPEED
    elif keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_image.get_width():
        car_x += CAR_SPEED

    # move o obstáculo
    obstacle_y += CAR_SPEED / 2

    # verifica se o carro colidiu com o obstáculo
    if car_x < obstacle_x + 50 and car_x + car_image.get_width() > obstacle_x and car_y < obstacle_y + 50 and car_y + car_image.get_height() > obstacle_y:
        running = False

    # verifica se o obstáculo chegou ao fim da tela
    if obstacle_y > SCREEN_HEIGHT:
        score += 1
        obstacle_x = random.randint(0, SCREEN_WIDTH - 50)
        obstacle_y = -50

    # limpa a tela
    screen.fill(WHITE)

    # desenha o carro e o obstáculo
    screen.blit(car_image, (car_x, car_y))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, 50, 50))

    # desenha a pontuação
    score_text = font.render(f'Pontuação: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # atualiza a tela
    pygame.display.update()

# encerra o Pygame
pygame.quit()
