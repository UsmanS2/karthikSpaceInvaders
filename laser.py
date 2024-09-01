import pygame

laserimg = pygame.image.load("blueLaser.png")
laserimg = pygame.transform.rotate(laserimg, 90)
laserimg = pygame.transform.scale(laserimg, (40, 40))

laserGroup = pygame.sprite.Group()

class Laser(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = laserimg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 490
        self.yspeed = -5

    def update(self):
        self.rect.y += self.yspeed