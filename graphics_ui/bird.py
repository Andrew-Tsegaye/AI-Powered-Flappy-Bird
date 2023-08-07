import pygame
import os

BIRD_IMAGES = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png"))),
]

class Bird:
    IMAGES = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0
        self.image = self.IMAGES[0]

    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        displacement = self.velocity * self.tick_count + 1.5 * self.tick_count**2

        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY

    def draw(self, win):
        self.img_count += 1

        if self.tilt < 0:
            self.image = self.IMAGES[1]
            self.img_count = self.ANIMATION_TIME * 2
        else:
            if self.img_count < self.ANIMATION_TIME:
                self.image = self.IMAGES[0]
            elif self.img_count < self.ANIMATION_TIME * 2:
                self.image = self.IMAGES[1]
            elif self.img_count < self.ANIMATION_TIME * 3:
                self.image = self.IMAGES[2]
            elif self.img_count < self.ANIMATION_TIME * 4:
                self.image = self.IMAGES[1]
            elif self.img_count == self.ANIMATION_TIME * 4 + 1:
                self.image = self.IMAGES[0]
                self.img_count = 0

        if self.tilt <= -80:
            self.image = self.IMAGES[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_img = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_img.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_img, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
