import pygame
from pygame.draw import *
import pygame.gfxdraw
from pygame.image import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

def backyard():
    rect(screen, (100,249,255),(0,0,400,350))
    rect(screen, (230,230,230),(0,350,400,600))
    line(screen, (0,0,0) ,(0,350),(400,350))
    
    ellipse(screen, (90,90,90), (220,425,150,50))
    ellipse(screen, (0,0,0), (220,425,150,50),width=1)
    ellipse(screen, (0,102,102), (235,440,125,35))
    ellipse(screen, (0,0,0), (235,440,125,35),width=1)
    
def sun():
    sun = pygame.Surface((300,300),pygame.SRCALPHA)
    ellipse(sun,(255,255,204,100),(0,0,300,300),width=20)
    line(sun,(255,255,204,100),(150,0),(159,300),width=20)
    line(sun,(255,255,204,100),(0,150),(300,150),width=20)
    ellipse(sun, (255,255,204),(10,140,20,20),width =0)
    ellipse(sun, (255,255,204),(270,140,20,20),width =0)
    ellipse(sun, (255,255,204),(140,10,20,20),width =0)
    ellipse(sun, (255,255,204),(140,270,20,20),width =0)
    ellipse(sun,(255,255,204),(140,140,40,40),width=0)
    screen.blit(sun,(150,-70))

def pbear():
    ellipse(screen, (240,240,240),(70,215,100,45)) #face
    ellipse(screen, (0,0,0),(70,215,100,45),width=1)
    
    ellipse(screen,(0,0,0),(110,225,5,5))#eye
    
    pygame.draw.arc(screen, (0,0,0), [75,190,115,55], -3.14/4-0.7,-3.14/4) #smile
    
    ellipse(screen, (250,250,250),[80,215,15,10],width=0) #ear
    pygame.draw.arc(screen, (0,0,0),[80,215,15,10],-3.14/3,3.14*4/3,width=1)
        
    ellipse(screen, (240,240,240), (10,250,140,230)) #body
    ellipse(screen, (0,0,0), (10,250,140,230),width=1)
    
    pygame.draw.arc(screen, (0,0,0), [140,300,250,230], 3.14*4/5-0.1,3.14*5/6+0.3,width=4) #snail
    line(screen, (0,0,0), (178,330),(330,140),width=4)
    line(screen,(0,0,0), (330,140),(325,460))

    ellipse(screen, (240,240,240),(120,320,60,25)) #arm
    ellipse(screen, (0,0,0),(120,320,60,25),width=1)
    
    ellipse(screen, (240,240,240),(90,430,100,70)) #leg1
    ellipse(screen, (0,0,0),(90,430,100,70),width =1)
    
    ellipse(screen, (240,240,240),(150,480,60,30)) #leg2
    ellipse(screen, (0,0,0),(150,480,60,30),width=1)

def fish():
    image = pygame.Surface((369,199 ))
    img = pygame.image.load(r'C:\Users\shink\Desktop\karas.png')
    image.blit(img,(0,0))
    new_image = pygame.transform.scale(image, (100, 70))
    screen.blit(new_image,(250,480))

backyard()
sun()
pbear()
fish()

#save(screen, 'wow.png')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()