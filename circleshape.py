import pygame

#Base class for game object (might end up being ALL game objects, circles are easier it seems)
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #for future use
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    
    
    def collision_check(self, other_shape):
        
        distance = pygame.math.Vector2.distance_to(self.position, other_shape.position)   
        
        if distance >= (self.radius + other_shape.radius):
            return True
        else:
            return False
    
    
    def draw(self, screen):
        #must be overridden by sub-classes
        pass
    
    def update(self, dt):
        #must be overridden by sub-classes
        pass