import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # Mostra a largura da tela
    print(f"Screen height: {SCREEN_HEIGHT}") # Mostra a altura da tela
    pygame.init() # Inicia o módulo pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # cria uma tela com o tamanho definido
    while True: # loop infinito (Todo jogo se baseia em um loop infinito)
        for event in pygame.event.get(): # Pega todos os eventos que aconteceram
            if event.type == pygame.QUIT: # Se o evento for fechar a janela
                return # Fecha o jogo
        screen.fill((0,0,0)) # Preenche a tela com a cor preta
        pygame.display.flip() # Atualiza a tela

if __name__ == "__main__":
    main()
    