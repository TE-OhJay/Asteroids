import pygame
import constants 
from circleshape import CircleShape


class Player(CircleShape):
    
    def __init__(self, x, y):
        
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.rate_limit = 0
    
    #While the player looks like a triangle - he is actually a circle. Reason being that it is much easier to deal with.
    # Determines direction plyer, directions and turning
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #gotta be able to turn around
    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    
    #moving the player
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    #shooting Shot(s)
    def shoot(self):
        bang = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        bang.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.SHOT_SPEED       
    
    #movement of the player, pretty simple setup
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
        
        #Turns out that god-mode is boring, so shots have to be regulated
        if keys[pygame.K_SPACE] and self.rate_limit <= 0:
            self.shoot()
            self.rate_limit = constants.PLAYER_SHOT_COOLDOWN
        elif self.rate_limit > 0:
            self.rate_limit -= dt
    
    #make the player look like not-an-asteroid
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

# Kill stuff
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    