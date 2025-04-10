# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #initiate game clock to regulate loop
    clock = pygame.time.Clock()
    #delta time, clock interaction
    dt = 0
    
    #groups
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    #Player groups
    Player.containers = (updateable, drawable)    
    #asteroid groups:
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    #Bullets
    Shot.containers = (updateable, drawable, bullets)
    
    
    #Spawning player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #enabling calls to AsteroidField()
    asteroid_field = AsteroidField()
    
    #Game loop initiation
    while True:
        
        #Check if loop is interrupted (ie. quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #movement update before render
        updateable.update(dt)
        
        #fill game screen with black
        screen.fill("black")
        
        #re-render player per frame
        for obj in drawable:
            obj.draw(screen)
        
        #Display update
        pygame.display.flip()
        #End of loop, regulate updating
        elapsed_miliseconds = clock.tick(60)
        dt = elapsed_miliseconds / 1000
        
        #check for Asteroids colliding with the player
        for obj in asteroids:
            if not obj.collision_check(player):
                print("Game Over!")
                exit()
            #check for bullets colliding with Asteroids
            for bullet in bullets:
                if not obj.collision_check(bullet):
                    bullet.kill()
                    obj.split()



if __name__ == "__main__":
    main()