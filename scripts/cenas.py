import pygame, random
from scripts.fase import Fase
from scripts.jogador import Jogador
from scripts.interfaces import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 550)
        self.fase = Fase(tela)
        self.estado = "partida" #indica o estado atual do jogo, se perdemos ou não

        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela, str(self.pontosValor),10,10,(0,0,0),30)

    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()
        self.fase.atualizar()

        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
        # aqui, desenhamos os pontos
        self.pontosTexto.desenhar()

        if self.fase.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            self.jogador.posicao = [176, 550]
            # zerando os pontos
            self.pontosValor = 0
            self.fase.y = -self.fase.imagem.get_height() 
            self.fase.x = random.randint(100, 255) # onde aparecerá os cones no eixo x
            self.fase.velocidade = 5

        self.fase.desenhar()
        self.jogador.desenhar()
        self.pontosTexto.desenhar()

        return self.estado
    
class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, 'Dirigindo BiBiBi!', 50, 20, (0,0,0), 50)
        self.estado = "menu"
        self.botao_jogar = Botao(tela, "JOGAR!", 115, 100, 50, (189, 134, 252), (177, 13, 222))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            self.estado = "partida"

        return self.estado

