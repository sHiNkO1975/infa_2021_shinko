import pygame
import pygame.draw
from random import randint
import pygame.gfxdraw
import pygame.image
pygame.init()
pygame.font.init() 


WINDOWSIZE = (800,600)
FPS = 60
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
summary = 0
number_of_targets=6
direction = [[1,1] for i in range(number_of_targets+1)]
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    
    '''возвращает параметры шарика'''
    
    x = randint(100, 700)
    y = randint(100, 500)
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    r = randint(40, 70)
    color = COLORS[randint(0, 5)]
    return [color, [x,y], r, vx, vy, 1]

def draw_fopf():
    '''
    рисует котика и возвращает его параметры
    '''
    x = randint(100, 400)
    y = randint(100, 400)
    vx = randint(-15,15)
    vy = randint(-15, 15)
    image = pygame.Surface((1000,1000), pygame.SRCALPHA)
    image.fill((0,0,0,0))
    img = pygame.image.load('cat_ava.png')
    image.blit(img,(0,0))
    new_image = pygame.transform.scale(image, (200, 200))
    return  [new_image, [x, y], 200 , vx, vy, 3]

myfont = pygame.font.SysFont('Comic Sans MS', 50)
screen = pygame.display.set_mode(WINDOWSIZE)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

x, y, radius = ([0 for i in range(number_of_targets+1)],
        [0 for i in range(number_of_targets+1)],
        [0 for i in range(number_of_targets+1)])


pool=[new_ball() for i in range(number_of_targets)]
pool.insert(0,draw_fopf())
start = False

while not finished:
    clock.tick(FPS)
    if start == False:
        print('Enter your name:')
        name = input()
        start = True
        summary = 0
    else:
        for i in range(number_of_targets+1):
            
            ball = pool[i]
            x[i] = ball[1][0]
            y[i] = ball[1][1]
            clr = ball[0]
            vx = ball[3]
            vy = ball[4]
            radius[i] = ball[2]        
                        
            if x[i] < 0 or x[i] > WINDOWSIZE[0]:
                direction[i][0] *= -1
                x[i] += 5
            if y[i] < 0 or y[i] > WINDOWSIZE[1]:
                direction[i][1] *= -1
                y[i]+= 5
            
            pool[i][1][0] += vx * direction[i][0]
            pool[i][1][1] -= vy * direction[i][1]
            
            if type(clr) != pygame.Surface:
                pygame.draw.circle(screen, clr, (x[i], y[i]), radius[i])
            else:
                if direction[i][0]*vx > 0:
                    clr = pygame.transform.flip(clr,1,0) 
                screen.blit(clr, [x[i],y[i]])
                    
            textsurface = myfont.render("Result: " + str(summary), False, (255, 255, 255))
            screen.blit(textsurface,(0,0))
    
    pygame.display.update()
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                document = open('result.txt', 'a')
                document.write(name+ ': ' +str(summary) + '\n')
                document.close()
            elif event.type == pygame.MOUSEBUTTONDOWN and start == True:
                mouse_coord = (event.pos)
                for i in range(number_of_targets+1):
                    if ((mouse_coord[0]-x[i])**2 + (mouse_coord[1]-y[i])**2 <= radius[i]**2):
                        summary+=pool[i][5]
                        pool.pop(i)
                        if randint(0, 7) == 7:
                            pool.insert(0, draw_fopf())
                        else:
                            pool.append(new_ball())
                        
    screen.fill(BLACK)
pygame.quit()