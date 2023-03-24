import pygame
import random

# inicialização do Pygame
pygame.init()

# configurar tela
tela_largura = 500
tela_altura = 500

tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Simples Jogo de caça quadrado")

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# variaveis do jogo
bloco_largura = 20
bloco_altura = 20
bloco_pos_x = random.randint(0, tela_largura - bloco_largura)
bloco_pos_y = random.randint(0, tela_altura - bloco_altura)

pontuacao = 0

# função para desenhar bloco
def desenha_bloco(pos_x, pos_y):
    pygame.draw.rect(tela, vermelho, [pos_x, pos_y, bloco_largura, bloco_altura])

# loop principal do jogo
rodando = True 

while rodando:
    # eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:

            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:

                rodando = False 

    # lógica do jogo
    pos_mouse = pygame.mouse.get_pos()
    pos_x = pos_mouse[0]
    pos_y = pos_mouse[1]

    colisao = (pos_x > bloco_pos_x and pos_x < bloco_pos_x + bloco_largura) and (pos_y > bloco_pos_y and pos_y < bloco_pos_y + bloco_altura)

    if colisao:
        bloco_pos_x = random.randint(0, tela_largura - bloco_largura)
        bloco_pos_y = random.randint(0, tela_altura - bloco_altura)

        pontuacao += 1

    # desenha na tela
    tela.fill(branco)

    desenha_bloco(bloco_pos_x, bloco_pos_y)
    pygame.display.set_caption(f"Jogo Simples - Pontuação: {pontuacao}")
    pygame.display.update()

# encerra o Pygame
pygame.quit()