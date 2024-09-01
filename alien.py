import pygame, random

alienImg = pygame.image.load("alienShip.png")
alienGroup = pygame.sprite.Group()

class Alien(pygame.sprite.Sprite):
    # constructor Function
    def __init__(self, x, y, w, h, image, type):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.xspeed = 0
        self.yspeed = 0
        if self.type == "straight horizontal":
            if random.randint(1, 2) == 1:
                self.xspeed = -5
            else:
                self.xspeed = 5

    def update(self):
        if self.type == "straight horizontal":
            if self.rect.x > 580:
                self.xspeed = -5
            if self.rect.x < 20:
                self.xspeed = 5
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed


for i in range(20):
    bob = Alien(random.randint(10, 590), 50, 40, 40, alienImg, "straight horizontal")
    alienGroup.add(bob)

