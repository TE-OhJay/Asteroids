# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

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
    
    
    #Spawning player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #Game loop initiation
    while True:
        
        #Check if loop is interrupted (ie. quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill game screen with black
        screen.fill("black")
        
        #re-render player per frame
        player.draw(screen)
        
        #Display update
        pygame.display.flip()
        
        #End of loop, regulate updating
        elapsed_miliseconds = clock.tick(60)
        dt = elapsed_miliseconds / 1000




if __name__ == "__main__":
    main()