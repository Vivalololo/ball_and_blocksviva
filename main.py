
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


ball_group = pygame.sprite.Group()
class Ball(pygame.sprite.Sprite):
    def __init__(self, filename, bx, by):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=(bx, by))
        self.naprx = 5
        self.napry = 7

    def update(self):
        if self.rect.centerx >= W or self.rect.centerx <= 0:
            self.naprx = -self.naprx
        if self.rect.centery >= H or self.rect.centery <= 0:
            self.napry = -self.napry
        if pygame.sprite.spritecollide(ball, player_group, False):
            self.napry = -self.napry
        self.rect.x += self.naprx
        self.rect.y += self.napry




ball = Ball('files/ball.png', W//2, H//2)
ball_group.add(ball)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player_group.update(12)
    ball_group.update()

    screen.fill((42,54,59))

    player_group.draw(screen)
    ball_group.draw(screen)

    pygame.draw.rect(screen, (WHITE), (0, 0, W, H), 13)
    pygame.display.flip()
    clock.tick(fps)
