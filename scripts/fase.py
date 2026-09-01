import pygame, random

class Fase:
    def __init__(self, tela): # será 400x600
        self.imagem = pygame.image.load('assets/cone.png')
        self.imagem = pygame.transform.scale(self.imagem, (40, 40))
        self.tela = tela # tela do jogo
        self.x = random.randint(100, 255) # onde aparecerá os cones no eixo x
        self.y = -self.imagem.get_height() # onde aparecerá os cones no eixo y
        
        self.velocidade = 5

    def atualizar(self):
        self.y += self.velocidade # faz o cone descer
        if self.y > 600: # se a imagem sair da tela:
            self.y = -self.imagem.get_height() 
            self.x = random.randint(100, 255) # onde aparecerá os cones no eixo x
            self.velocidade += 0.1 # aumenta a velocidade aos poucos
            print("Velocidade atual dos cones:",self.velocidade)

    def desenhar(self):
        pygame.draw.rect(self.tela, (80, 80, 80), (100, 0, 200, 600))            
        self.tela.blit(self.imagem,(self.x, self.y))

    def detectarColisao(self, rectJogador):
        rectCone = pygame.Rect((self.x, self.y), self.imagem.get_size())
        
        # Muito legal essas funções de colisão do PyGame!!!
        if rectJogador.colliderect(rectCone):
            return True
        else:
            return False
