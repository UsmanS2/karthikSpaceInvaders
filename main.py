import pygame, random
from alien import *
from laser import *

screen = pygame.display.set_mode((600, 600))
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

ship = pygame.sprite.Sprite()
ship_height = 75
ship_width = 75
shipImage = pygame.image.load("spaceShip.png")
shipImage = pygame.transform.scale(shipImage, (ship_width, ship_height))

ship.image = shipImage

ship.rect = pygame.Rect(260, 500, ship_width, ship_height)

ship.xspeed = 0

def updateShip():
    ship.rect.x += ship.xspeed

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.xspeed = 4
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.xspeed = -4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.xspeed = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.xspeed = 0

    updateShip()
    alienGroup.update()

    screen.blit(ship.image, ship.rect)
    for alien in alienGroup.sprites():
        screen.blit(alien.image, alien.rect)

    pygame.display.flip()
    clock.tick(60)
