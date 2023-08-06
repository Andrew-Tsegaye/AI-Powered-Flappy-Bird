import pygame
import neat
import time
import os
import random

# Set up the window dimensions
WIN_WIDTH = 500
WIN_HEIGHT = 800

# Load bird images, pipe image, base image, and background image
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png"))),
]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


# Bird class definition
class Bird:
    # Bird class variables
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    # Bird object initialization
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    # Method to make the bird jump
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    # Method to handle bird movement
    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count**2

        # Limit the bird's falling speed
        if d >= 16:
            d = 16

        # Add a small offset when the bird is moving upwards
        if d < 0:
            d -= 2

        # Update the bird's position
        self.y = self.y + d

        # Adjust bird's tilt depending on its movement
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    # Method to draw the bird on the window
    def draw(self, win):
        self.img_count += 1

        # Handle bird animation
        if self.tilt < 0:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2
        else:
            # Handle bird animation when not falling
            if self.img_count < self.ANIMATION_TIME:
                self.img = self.IMGS[0]
            elif self.img_count < self.ANIMATION_TIME * 2:
                self.img = self.IMGS[1]
            elif self.img_count < self.ANIMATION_TIME * 3:
                self.img = self.IMGS[2]
            elif self.img_count < self.ANIMATION_TIME * 4:
                self.img = self.IMGS[1]
            elif self.img_count == self.ANIMATION_TIME * 4 + 1:
                self.img = self.IMGS[0]
                self.img_count = 0

        # Handle bird tilt when it's about to fall
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # Rotate and draw the bird on the window
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center
        )
        win.blit(rotated_img, new_rect.topleft)

    # Method to get the bird's collision mask
    def get_mask(self):
        return pygame.mask.from_surface(self.img)


# Pipe class definition
class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True

        return False


class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL


# Function to draw the window and bird
def draw_window(win, bird):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)
    pygame.display.update()


# Main function to run the game
def main():
    # Create a bird object
    bird = Bird(200, 200)

    # Set up the game window
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Move the bird and update the window
        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()


# Call the main function to start the game
main()
