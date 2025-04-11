import pygame
import constants
import random
from circleshape import CircleShape

#Initiate and draw individual asteroids

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    #split asteroids, kill when they go below minimum size
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        else:
            angle = random.uniform(20, 50)
            vector1, vector2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            small_1 = Asteroid(self.position.x, self.position.y, new_radius)
            small_2 = Asteroid(self.position.x, self.position.y, new_radius)
            small_1.velocity = vector1 * 1.2
            small_2.velocity = vector2 * 1.2
            self.kill()
            return