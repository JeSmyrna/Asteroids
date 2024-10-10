import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroids import Asteroid
from shot import Shot

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

    asteroids_group = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    updatable = pygame.sprite.Group(py_player)
    drawable = pygame.sprite.Group(py_player)
    
    Shot.containers = (player_shots, updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    
    while True:
        screen.fill(color=(0,0,0))
        dt = py_clock.tick(60) / 1000
        for draw in drawable:
            draw.draw(screen)
        for object in updatable:
            object.update(dt)
        for obstacle in asteroids_group:
            if obstacle.collision(py_player):
                print("Game Over")
                quit()
            
        #updatable.update()
        #drawable.draw()
        
        
        # Close function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()
