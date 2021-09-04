
def restart():
    import sys
    import random
    import pygame
    pygame.init()
    import sqlite3


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLUE_light = (20, 255, 236)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)

    color_list = [WHITE, RED, GREEN, BLUE, BLUE_light, ORANGE, YELLOW, PURPLE, PINK]


    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    #db.execute("SELECT color FROM AA where level=1 and rows=1 and column=3")
    # соединение с бд
    conn = sqlite3.connect('db.sqlite3')
    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    db = conn.cursor()

    db.execute("SELECT current_level FROM BB")
    currentLEVEL = db.fetchone()
    # замена перенных, тк питон жалуется на currentLEVEL[0] наверное тк это массив
    aa = currentLEVEL[0]


    W = 600
    H = 700
    clock = pygame.time.Clock()
    fps = 60

    screen = pygame.display.set_mode((W, H))
    f1 = pygame.font.SysFont('arial', 100)

    # кнопки передают text - текст, x - положение х, y - положение у, w - длина, h - ширина, colorrect - цвет прямоугольника, bf - размер большого шрифта, lf - размер маленького,
    # colortext - цвет текста, action - какое действие активировать какой def
    def button(text, x, y, w, h, colorrect, bf, lf, colortext, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # если навел мышь на кнопку
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            fontbig = pygame.font.SysFont('arial', bf)
            pygame.draw.rect(screen, colorrect, (x, y, w, h))
            textf = fontbig.render(text, True, colortext)
            textfpos = textf.get_rect(center=(x + (w / 2), (y + (h / 2))))
            screen.blit(textf, textfpos)
            # если кликнул по кпопке
            if click[0] == 1 and action != None:
                pygame.mouse.set_visible(False)
                pygame.time.wait(1000)
                action()
        # если мышка не в кнопке, то просто рисовать кнопку
        else:
            fontlittle = pygame.font.SysFont('arial', lf)
            pygame.draw.rect(screen, colorrect, (x, y, w, h))
            textf = fontlittle.render(text, True, colortext)
            textfpos = textf.get_rect(center = (x+(w/2), (y+(h/2))))
            screen.blit(textf, textfpos)

    # звук при сталкивания шара с обычными блоками
    def blockcrash():
        soundcrash = pygame.mixer.Sound('files/blockcrash.mp3')
        pygame.mixer.Sound.play(soundcrash)

    # фон
    def background():
        im1 = pygame.image.load('files/background1.jpg').convert_alpha()
        im1 = pygame.transform.scale(im1, (im1.get_width(), im1.get_height() * 2))
        im1.set_alpha(200)
        screen.blit(im1, (0, 0))

    # если коснулся кубка, то прошел уровень
    def completedlevel():
        # завершие уровня и запись в бд что ты это прошел на другой уровень
        db.execute("SELECT current_level FROM BB")
        currentLEVEL = db.fetchone()
        current = currentLEVEL[0]
        current += 1
        db.execute("UPDATE BB SET current_level=%s" % (current))
        conn.commit()
        pygame.mouse.set_visible(True)
        background()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    conn.close()
                    sys.exit()
            button('NEXT LEVEL', 140, 100, 330, 80, ORANGE, 60, 40, BLACK, restart)
            clock.tick(fps)
            pygame.display.flip()


    # цикл меню
    def game_menu():
        menu = True
        pygame.mouse.set_visible(True)
        screen.fill(WHITE)
        background()
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        menu = False
                        # текст загрузки
                        #text2 = f1.render('loading..', True, ORANGE)
                        #pos2 = text2.get_rect(center=(W//2+200, H//2))
                        #screen.blit(text2, pos2)
                        #pygame.mouse.set_visible(False)
            # текст текущий левел
            text1 = f1.render('current level - %a' % aa, True, BLUE_light)
            pos1 = text1.get_rect(center=(W//2, 100))
            screen.blit(text1, pos1)

            # кнопки в меню
            button('PLAY', 30, 400, 200, 100, GREEN, 80, 50, BLACK, game_play)
            button('EXIT', 30, 520, 200, 100, RED, 80, 50, BLACK, game_exit)
            pygame.display.flip()

        pygame.time.wait(2500)

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

    player = Player(WHITE, W//2, H-100)
    player_group.add(player)


    blocks_group = pygame.sprite.Group()
    blocks_group_unbreakable = pygame.sprite.Group()

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
        for y in range(0,20,1):
            for x in range(0,15,1):
                db.execute("SELECT color FROM AA where level=1 and unbreakable=0 and rows=%s and column=%s" % (x,y))
                results = db.fetchone()
                if results is None:
                    results = (99,0)
                # отрисовка кирпича с его случайным цветом
                if results[0]==0:
                    color = random.choice(color_list)
                    block = Blocks(color, x*51, y*25)
                    blocks_group.add(block)


        reward = Reward('files/reward.png', W / 2, 32)
        reward_group.add(reward)

    def level2():
        for y in range(0,20,1):
            for x in range(0,15,1):
                db.execute("SELECT color FROM AA where level=2 and unbreakable=0 and rows=%s and column=%s " % (x,y))
                results = db.fetchone()
                if results is None:
                    results = (99,0)
                # отрисовка кирпича с его случайным цветом
                if results[0]==0:
                    pass
                    color = random.choice(color_list)
                    block = Blocks(color, x*51, y*25)
                    blocks_group.add(block)
        for y in range(0, 20, 1):
            for x in range(0, 15, 1):
                db.execute("SELECT unbreakable FROM AA where level=2 and rows=%s and column=%s" % (x, y))
                results1=db.fetchone()
                if results1 is None:
                    results1 = (99,0)
                if results1[0]==1:
                    block = Blocks(BLACK, x * 51, y * 25)
                    blocks_group_unbreakable.add(block)



        reward = Reward('files/reward.png', W / 2, 32)
        reward_group.add(reward)


    # запрос на какой уровень выбрать для прохождения
    db.execute("SELECT current_level FROM BB")
    currentLEVEL = db.fetchone()
    if currentLEVEL[0] == 1:
        level1()
    if currentLEVEL[0] == 2:
        level2()
    if currentLEVEL[0] == 3:
        level3()



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
                #self.naprx = random.randint(-7, 7)


            # столкновение с шаром по x
            #if self.naprx > 0 and pygame.sprite.spritecollide(ball, player_group, False) or self.naprx < 0 and pygame.sprite.spritecollide(ball, player_group, False):
            #    self.napry = -self.napry

            # сталкивание шара с простыми блоками
            if self.napry < 0 and pygame.sprite.spritecollide(ball, blocks_group, True) or self.napry > 0 and pygame.sprite.spritecollide(ball, blocks_group, True):
                blockcrash()
                self.napry = -self.napry
                self.naprx = random.randint(-5, 5)

            # старкивание шара с unbreakable блоками
            if self.napry < 0 and pygame.sprite.spritecollide(ball, blocks_group_unbreakable, False) or self.napry > 0 and pygame.sprite.spritecollide(ball, blocks_group_unbreakable, False):
                self.napry = -self.napry
                self.naprx = random.randint(-7, 7)

            #  сталкновение с кубком
            if pygame.sprite.spritecollide(ball, reward_group, True):
                pygame.time.wait(1500)
                completedlevel()

            # джижение шара по физике
            self.rect.x += self.naprx
            self.rect.y += self.napry


    # деф если шар упал ниже платформы im.get_width()//3, im.get_height()//3
    def drop():
            sounddrop = pygame.mixer.Sound('files/wastedgtav.mp3')
            sounddrop.play()
            pygame.time.wait(1200)

            background()

            im2 = pygame.image.load('files/wastedph1.png').convert_alpha()
            im2 = pygame.transform.scale(im2, (im2.get_width()*2, im2.get_height()*2))
            im2rect = im2.get_rect(center=(W//2, H//2+ 100))

            screen.blit(im2, im2rect)
            pygame.mouse.set_visible(True)


            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        conn.close()
                        sys.exit()
                button('RESTART', 30, 100, 400, 100, ORANGE, 80, 50, BLACK, restart)
                button('EXIT', 30, 220, 200, 100, RED, 80, 50, BLACK, game_exit)

                clock.tick(fps)
                pygame.display.flip()

    ball = Ball('files/ball.png', player.rect.centerx, player.rect.y-10)
    ball_group.add(ball)

    # деф для выхода
    def game_exit():
        pygame.quit()
        conn.close()
        sys.exit()

    # цикл игры
    def game_play():
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    conn.close()
                    sys.exit()

            if ball.rect.y >= H-25:
                drop()
            player_group.update(12)
            ball_group.update()

            screen.fill((42,54,59))

            player_group.draw(screen)
            blocks_group.draw(screen)
            blocks_group_unbreakable.draw(screen)
            ball_group.draw(screen)
            reward_group.draw(screen)

            pygame.draw.rect(screen, (WHITE), (0, 0, W, H), 5)
            pygame.display.flip()
            clock.tick(fps)

    game_menu()
    game_play()
    pygame.quit()
    quit()
restart()