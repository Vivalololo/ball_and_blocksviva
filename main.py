import sys
import random
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUE_light = (20,255,236)

W = 600
H = 700
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((W, H))
#pygame.mouse.set_visible(False)

player_group = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
    def __init__(self, color, plx, ply):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(plx, ply))

    def update(self, speed):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -speed
        if keystate[pygame.K_RIGHT]:
            self.speedx = speed
        self.rect.x += self.speedx
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left < 0:
            self.rect.left = 0

player = Player((WHITE), W//2, H-100)
player_group.add(player)


blocks_group = pygame.sprite.Group()
class Blocks(pygame.sprite.Sprite):
    def __init__(self, color, blx, bly):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(blx, bly))

reward_group = pygame.sprite.Group()
class Reward(pygame.sprite.Sprite):
    def __init__(self, filename, rex, rey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))
        self.rect = self.image.get_rect(center=(rex, rey))


def level1():
    for x in range (0+3, W-3, 43):
        for y in range (H-300-24, H-300, 23):
            color1 = random.randint(0, 255)
            color2 = random.randint(0, 255)
            color3 = random.randint(0, 255)
            block = Blocks((color1, color2, color3), x, y)
            blocks_group.add(block)
    for x in range (0+3, W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-370)
        blocks_group.add(block)
    for x in range (W//2 + 88, W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-370)
        blocks_group.add(block)
    for x in range (W//2-143, W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H - 410)
        blocks_group.add(block)
    for x in range (0+3, W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-450)
        blocks_group.add(block)
    for x in range (W//2 + 88, W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-450)
        blocks_group.add(block)
    for x in range (W//2-143, W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-490)
        blocks_group.add(block)
    for x in range (0+3, W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-530)
        blocks_group.add(block)
    for x in range (W//2 + 88, W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-530)
        blocks_group.add(block)
    for x in range (W//2-143, W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-570)
        blocks_group.add(block)
    for x in range (0+3, W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-610)
        blocks_group.add(block)
    for x in range (W//2 + 88, W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-610)
        blocks_group.add(block)
    for x in range (W//2-143, W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, H-640)
        blocks_group.add(block)
    reward = Reward('files/reward.png', W / 2, 32)
    reward_group.add(reward)

level1()

ball_group = pygame.sprite.Group()
class Ball(pygame.sprite.Sprite):
    def __init__(self, filename, bax, bay):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(bax, bay))
        self.naprx = 3
        self.napry = 7

    def update(self):
        if self.rect.centerx >= W or self.rect.centerx <= 0:
            self.naprx = -self.naprx
        if self.rect.centery >= H or self.rect.centery <= 0:
            self.napry = -self.napry

        # столкновение с платформой
        if pygame.sprite.spritecollide(ball, player_group, False):
            self.napry = -self.napry
            #self.naprx = -self.naprx

        # столкновение с шаром по x
        #if self.naprx > 0 and pygame.sprite.spritecollide(ball, player_group, False) or self.naprx < 0 and pygame.sprite.spritecollide(ball, player_group, False):
        #    self.napry = -self.napry

        # сталкивание шара с блоками
        if self.napry < 0 and pygame.sprite.spritecollide(ball, blocks_group, True) or self.napry > 0 and pygame.sprite.spritecollide(ball, blocks_group, True):
            self.napry = -self.napry

        #  сталкновение с кубком
        if pygame.sprite.spritecollide(ball, reward_group, True):
            pygame.time.wait(5000)

        # выход, если шар упал ниже платформы
        #if self.rect.y >= player.rect.y+70:
        #    sys.exit()

        # джижение шара по физике
        self.rect.x += self.naprx
        self.rect.y += self.napry


ball = Ball('files/ball.png', player.rect.centerx, player.rect.y-10)
ball_group.add(ball)




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player_group.update(12)
    ball_group.update()

    screen.fill((42,54,59))

    player_group.draw(screen)
    blocks_group.draw(screen)
    ball_group.draw(screen)
    reward_group.draw(screen)

    pygame.draw.rect(screen, (WHITE), (0, 0, W, H), 13)
    pygame.display.flip()
    clock.tick(fps)
