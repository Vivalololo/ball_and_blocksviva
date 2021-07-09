import pygame
import random




blocks_group = pygame.sprite.Group()
def map():
    blocks_group = pygame.sprite.Group()

    class Blocks(pygame.sprite.Sprite):
        def __init__(self, color, blx, bly):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((40, 20))
            self.image.fill(color)
            self.rect = self.image.get_rect(topleft=(blx, bly))

    for x in range (0+3, main.W-3, 43):
        for y in range (main.H-300-24, main.H-300, 23):
            color1 = random.randint(0, 255)
            color2 = random.randint(0, 255)
            color3 = random.randint(0, 255)
            block = Blocks((color1, color2, color3), x, y)
            blocks_group.add(block)

    for x in range (0+3, main.W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-370)
        blocks_group.add(block)
    for x in range (main.W//2 + 88, main.W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-370)
        blocks_group.add(block)
    for x in range (main.W//2-143, main.W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H - 410)
        blocks_group.add(block)


    for x in range (0+3, main.W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-450)
        blocks_group.add(block)
    for x in range (main.W//2 + 88, main.W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-450)
        blocks_group.add(block)
    for x in range (main.W//2-143, main.W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-490)
        blocks_group.add(block)


    for x in range (0+3, main.W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-530)
        blocks_group.add(block)
    for x in range (main.W//2 + 88, main.W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-530)
        blocks_group.add(block)
    for x in range (main.W//2-143, main.W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-570)
        blocks_group.add(block)


    for x in range (0+3, main.W//2-100, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-610)
        blocks_group.add(block)
    for x in range (main.W//2 + 88, main.W-3, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-610)
        blocks_group.add(block)
    for x in range (main.W//2-143, main.W//2+131, 43):
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        color3 = random.randint(0, 255)
        block = Blocks((color1, color2, color3), x, main.H-640)
        blocks_group.add(block)
    return blocks_group

