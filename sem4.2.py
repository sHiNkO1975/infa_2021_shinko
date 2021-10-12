import pygame
from pygame.draw import *

#LIST OF PARAMETERS
screen_xsize = 800
screen_ysize = 600
FPS = 30


#LIST OF COLORS
bearcolor = (240, 240, 240)
bordercolor = (0, 0, 0)
floorcolor = (230, 230, 230)
holecolor = (90, 90, 90)
skycolor = (100, 249, 255)
suncolor = (255, 255, 204)
transpsuncolor = (255, 255, 204, 100)
watercolor = (0, 102, 102)


def background(screen, xsize, ysize, x, y):
    surf = pygame.Surface((400, 600), pygame.SRCALPHA)
    #SKY
    rect(surf, skycolor, (0, 0, 400, 350))
    #FLOOR
    rect(surf, floorcolor, (0, 350, 400, 600))
    #HORIZON
    line(surf, bordercolor, (0, 350), (400, 350), 2)
    #BLIT
    screen.blit(pygame.transform.scale(surf, (xsize, ysize)), (x, y))


def sun(screen, xsize, ysize, x, y):
    surf = pygame.Surface((300, 300), pygame.SRCALPHA)
    #RIM
    ellipse(surf, transpsuncolor, (0, 0, 300, 300), 20)
    #CROSSHAIR
    line(surf, transpsuncolor, (150, 0), (159, 300), 20)
    line(surf, transpsuncolor, (0, 150), (300, 150), 20)
    #SMALLCIRCLES
    ellipse(surf, suncolor, (0, 140, 25, 25))
    ellipse(surf, suncolor, (276, 140, 25, 25))
    ellipse(surf, suncolor, (140, 0, 25, 25))
    ellipse(surf, suncolor, (147, 275, 25, 25))
    #CENTRALCIRCLE
    ellipse(surf, suncolor, (135, 130, 40, 40))
    #BLIT
    screen.blit(pygame.transform.scale(surf, (xsize, ysize)), (x, y))


def bear(screen, xsize, ysize, x, y, orientation):
    surf = pygame.Surface((400, 600), pygame.SRCALPHA)
    #FACE
    ellipse(surf, bearcolor, (70, 215, 100, 45))
    ellipse(surf, bordercolor, (70, 215, 100, 45), 2)
    #EYE
    ellipse(surf, bordercolor, (110, 225, 5, 5))
    #SMILE
    arc(surf, bordercolor, [75, 190, 115, 55], -3.14 / 4 - 0.7, -3.14 / 4)
    #EAR
    ellipse(surf, bearcolor, [80, 215, 15, 10])
    arc(surf, bordercolor, [80, 215, 15, 10], -3.14 / 3, 3.14 * 4 / 3, 2)
    #EARSNAIL
    arc(surf, bordercolor, [140, 300, 250, 230], 3.14 * 4 / 5 - 0.1, 3.14 * 5 / 6 + 0.3, 4)
    #FISHINGHOLE
    ellipse(surf, holecolor, (220, 425, 150, 50))
    ellipse(surf, bordercolor, (220, 425, 150, 50), 2)
    ellipse(surf, watercolor, (235, 440, 125, 35))
    ellipse(surf, bordercolor, (235, 440, 125, 35), 2)
    #FISHINGROD
    line(surf, bordercolor, (178, 330), (330, 140), 3)
    line(surf, bordercolor, (330, 140), (325, 460), 2)
    #BODY
    ellipse(surf, bearcolor, (10, 250, 140, 230))
    ellipse(surf, bordercolor, (10, 250, 140, 230), 2)
    #ARM
    ellipse(surf, bearcolor, (120, 320, 60, 25))
    ellipse(surf, bordercolor, (120, 320, 60, 25), 2)
    #HIP
    ellipse(surf, bearcolor, (90, 430, 100, 70))
    ellipse(surf, bordercolor, (90, 430, 100, 70), 2)
    #LEG
    ellipse(surf, bearcolor, (150, 480, 60, 30))
    ellipse(surf, bordercolor, (150, 480, 60, 30), 2)
    #FISH
    fishimage = pygame.image.load('karas.png').convert_alpha()
    surf.blit(pygame.transform.scale(fishimage, (120, 70)), (225, 500))
    #SCALE
    surf = pygame.transform.scale(surf, (xsize, ysize))
    #FLIP AND BLIT
    if (orientation == 'right'):
        screen.blit(surf, (x, y))
    elif (orientation == 'left'):
        screen.blit(pygame.transform.flip(surf, True, False), (x, y))


pygame.init()
screen = pygame.display.set_mode((screen_xsize, screen_ysize))

background(screen, screen_xsize, screen_ysize, 0, 0)
sun(screen, screen_xsize//2, screen_ysize*7//12, screen_xsize*5//8, -screen_ysize//12)
#FIRST BEAR
bear(screen, screen_xsize//3, screen_ysize*2//3, screen_xsize//2, screen_ysize//5, 'right')
#SECOND BEAR
bear(screen, screen_xsize//2, screen_ysize, screen_xsize// 18, screen_ysize // 18, 'right')
#THIRDBEAR
bear(screen, screen_xsize//4, screen_ysize//2, screen_xsize*3//4, screen_ysize//2, 'left')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
