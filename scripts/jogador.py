import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.posicao = [x, y] 
        self.tamanho = [48, 48] # tamanho do player
        self.rect = pygame.Rect(self.posicao, self.tamanho) # usaremos para detectar a colisão do player

        self.tela = tela # tela do jogo do main.py

        self.imagem = pygame.image.load(f'assets/carro.png') # jeito chique de alterar as imagens, amei!
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho) # escala a imagem para as proporções corretas

        self.velocidade = 3

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao) # desenha, por fim, a imagem

    def atualizar(self):
        self.teclas = pygame.key.get_pressed()

        # Movimento em X com trava nos limites da pista (100 até 300)
        if self.teclas[pygame.K_LEFT]:
            self.posicao[0] -= self.velocidade
            # 1. Trava na borda esquerda da pista
            if self.posicao[0] < 100:
                self.posicao[0] = 100

        if self.teclas[pygame.K_RIGHT]:
            self.posicao[0] += self.velocidade
            # 1. Trava na borda direita da pista
            if self.posicao[0] > 300 - self.tamanho[0]:
                self.posicao[0] = 300 - self.tamanho[0]

        # Movimento em Y com trava no topo e na base da tela
        if self.teclas[pygame.K_UP]:
            self.posicao[1] -= self.velocidade
            if self.posicao[1] < 0:
                self.posicao[1] = 0

        if self.teclas[pygame.K_DOWN]:
            self.posicao[1] += self.velocidade
            if self.posicao[1] > 600 - self.tamanho[1]:
                self.posicao[1] = 600 - self.tamanho[1]

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)

