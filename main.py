import pygame
from constants import *
from player import *

py_clock = pygame.time.Clock()
dt = 0
player_pos_x = SCREEN_WIDTH/2
player_pos_y = SCREEN_HEIGHT/2

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_player = Player(player_pos_x,player_pos_y)
    
    while True:
        screen.fill(color=(0,0,0))
        py_player.draw(screen)
        pygame.display.flip()
        
        # Close function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = py_clock.tick(60) / 1000



if __name__ == "__main__":
    main()
