import math
from random import choice
import random
import pygame
import pygame.image


FPS = 30
mu = 0.7
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 5000

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        self.live -= 1
        if self.x < 10 and self.vx < 0 :
            self.vx *= -mu
            self.x += 5
        if self.x > WIDTH-10 and self.vx > 0:
            self.vx *= -mu
            self.x -= 5
        if self.y < 10:
            self.vy *= -mu
            self.vx *= mu
            self.y += 10
        if self.y > HEIGHT-10:
            self.vy *= -mu
            self.vx *= mu
            self.y -= 10

    def draw(self):
        if self.live >= 0:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )
        else:
            pass

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2 + (self.y-obj.y)**2 <= (obj.r + self.r)**2:
            return True
        else: 
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 20
        self.y = 450
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
            
    def move(self, key):
        """Передвижение пушки"""
        if key[pygame.K_LEFT]:
            self.x -= 5
        if key[pygame.K_RIGHT]:
            self.x += 5
        if key[pygame.K_UP]:
            self.y -= 5
        if key[pygame.K_DOWN]:
            self.y += 5

    def draw(self):
        gun_screen = pygame.Surface((10,30), pygame.SRCALPHA)
        gun_screen.fill((255,255,255,200))
        pygame.draw.rect(gun_screen, BLACK, (0, 0, 5*self.f2_power/10, 15*self.f2_power/10))
        gun = pygame.transform.rotate(gun_screen, (270-self.an*180/math.pi))
        screen.blit(gun, (self.x-20, self.y-5))
        for ball in balls:
            ball.draw()
        
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
            
            
class Target:
    def __init__(self, screen):
        self.points = 0
        self.live = 1
        self.new_target()
        self.screen = screen

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = random.randint(600, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(2, 50)
        self.vx = random.randint(-10,10)
        self.vy = random.randint(-10,10)
        color = self.color = RED
        self.live = 1

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.x < 10 and self.vx < 0 :
            self.vx *= -1
            self.x += 5
        if self.x > WIDTH-10 and self.vx > 0:
            self.vx *= -1
            self.x -= 5
        if self.y < 10:
            self.vy *= -1
            self.y += 10
        if self.y > HEIGHT-10:
            self.vy *= -1
            self.y -= 10
        
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        if self.live == 1:
            pygame.draw.circle(
                screen,
                self.color,
                (self.x, self.y),
                self.r)

points = 0
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
dt = 0
balls = []
targets = []
clock = pygame.time.Clock()
gun = Gun(screen)
targets.append(Target(screen))
targets.append(Target(screen))
finished = False
myfont = pygame.font.SysFont('Comic Sans MS', 25)

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for t in targets:
        t.draw()
    countsurface = myfont.render(str(points), False, (0,0,0))
    screen.blit(countsurface,(0,0))
    for b in balls:
        b.draw()
        if abs(b.vx) < 1:
            balls.pop(balls.index(b))
    if dt > 0:
        textsurface = myfont.render("Вы уничтожили цель за " + str(bullet) + ' выстрелов', False, (22,222,222))
        screen.blit(textsurface,(110,110))
        dt -= 1
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        gun.move(pygame.key.get_pressed())
    for b in balls:
        for t in targets:
            b.move()
            t.move()
            if b.hittest(t) and t.live:
                dt = 60
                t.live = 0
                t.hit()
                t.new_target()
                points += t.points
    gun.power_up()
pygame.quit()