# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

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
    
    
    #Game loop initiation
    while True:
        
        #Check if loop is interrupted (ie. quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #fill game screen with black
        screen.fill("black")
        
        #Display update
        pygame.display.flip()
        
        #End of loop, regulate updating
        elapsed_miliseconds = clock.tick(60)
        dt = elapsed_miliseconds / 1000




if __name__ == "__main__":
    main()