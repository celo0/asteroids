import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init() # Inicia o módulo pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # cria uma tela com o tamanho definido
    clock = pygame.time.Clock() # Cria um objeto de clock para controlar o tempo
    dt = 0 # Delta time, tempo que passou desde o último frame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True: # loop infinito (Todo jogo se baseia em um loop infinito)
        for event in pygame.event.get(): # Pega todos os eventos que aconteceram
            if event.type == pygame.QUIT: # Se o evento for fechar a janela
                return # Fecha o jogo
        screen.fill((0,0,0)) # Preenche a tela com a cor preta
        updatable.update(dt)
        for jogador in drawable:
            jogador.draw(screen)
        pygame.display.flip() # Atualiza a tela
        clock.tick(60) # Limita o jogo a 60 frames por segundo
        dt = clock.tick(60) / 1000 # Atualiza o delta time

if __name__ == "__main__":
    main()
    