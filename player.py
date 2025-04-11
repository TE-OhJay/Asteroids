import pygame
import constants 
from circleshape import CircleShape


class Player(CircleShape):
    
    def __init__(self, x, y):
        
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.rate_limit = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    
    def shoot(self):
        bang = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        bang.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.SHOT_SPEED       
    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt) #rotate left
            
        if keys[pygame.K_d]:
            self.rotate(dt) #rotate right
        
        if keys[pygame.K_w]:
            self.move(dt) #forward
        
        if keys[pygame.K_s]:
            self.move(-dt) #backward
        
        if keys[pygame.K_SPACE] and self.rate_limit <= 0:
            self.shoot()
            self.rate_limit = constants.PLAYER_SHOT_COOLDOWN
        elif self.rate_limit > 0:
            self.rate_limit -= dt
    
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    