from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            random_angle_pos = random.uniform(20, 50)
            random_angle_neg = random.uniform(20, 50) * -1

            velocity_a = self.velocity.rotate(random_angle_pos)
            velocity_b = self.velocity.rotate(random_angle_neg)
            
            old_radius -= ASTEROID_MIN_RADIUS

            asteroid_a = Asteroid(self.position.x, self.position.y, old_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, old_radius)

            asteroid_a.velocity = velocity_a * 1.2
            asteroid_b.velocity = velocity_b * 1.2