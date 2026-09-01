import pygame
from scripts.cenas import Partida, Menu

pygame.init() # inicia o pygame

tamanhoTela = [400, 600]
tela = pygame.display.set_mode(tamanhoTela) # variável da tela com o pygame
pygame.display.set_caption("BiBiBi!")
relogio = pygame.time.Clock() # Usado para o FPS e controle da velocidade do jogo
corFundo = (110, 112, 111) # RGB
# jog = Jogador(tela, 100, 100)
# cano = Cano(tela)

listaCenas = {
    'partida': Partida(tela),
    'menu': Menu(tela),
}

cenaAtual = 'menu'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: # se o evento obtido for sair:
            pygame.quit()

    tela.fill(corFundo) # minha tela roxa amooo!


    cenaAtual = listaCenas[cenaAtual].atualizar() # uma forma bem legal de trocar as cenas!

    relogio.tick(60) # 60 FPS
    pygame.display.flip() # atualiza a tela
