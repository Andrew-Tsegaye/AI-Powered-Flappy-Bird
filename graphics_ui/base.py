import pygame
import os

# Load and scale the base image
BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))

# Base class represents the moving ground in the game
class Base:
    # Ground movement speed
    VELOCITY = 5

    # Get the width of the scaled base image
    WIDTH = BASE_IMAGE.get_width()

    # Store the scaled base image
    IMAGE = BASE_IMAGE

    # Initialize the Base object with its position and two x-coordinates
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    # Move the base to the left to create the scrolling effect
    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        # Reset the x-coordinates when the first instance of the base moves out of the screen
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        # Reset the x-coordinates when the second instance of the base moves out of the screen
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    # Draw the two instances of the base on the game window
    def draw(self, win):
        win.blit(self.IMAGE, (self.x1, self.y))
        win.blit(self.IMAGE, (self.x2, self.y))
