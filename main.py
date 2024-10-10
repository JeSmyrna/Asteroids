import pygame
from constants import *
from player import *

py_clock = pygame.time.Clock()
dt = 0
player_pos_x = SCREEN_WIDTH/2
player_pos_y = SCREEN_HEIGHT/2

py_player = Player(player_pos_x,player_pos_y)

updatable = pygame.sprite.Group(py_player)
drawable = pygame.sprite.Group(py_player)

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    while True:
        screen.fill(color=(0,0,0))
        dt = py_clock.tick(60) / 1000
        for draw in drawable:
            draw.draw(screen)
        for object in updatable:
            object.update(dt)
        #updatable.update()
        #drawable.draw()
        
        
        # Close function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()
