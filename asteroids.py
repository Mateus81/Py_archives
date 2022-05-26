import pygame
import math
import random

pygame.init()

sh: int = 800
sw: int = 800

bg = pygame.image.load("starbg.png")
alienImg = pygame.image.load('alienShip.png')
playerRocket = pygame.image.load('spaceRocket.png')
star = pygame.image.load('star.png')
asteroid50 = pygame.image.load('asteroid50.png')
asteroid100 = pygame.image.load('asteroid100.png')
asteroid150 = pygame.image.load('asteroid150.png')

shoot = pygame.mixer.Sound('sounds/sounds_shoot.wav')
bangLarge = pygame.mixer.Sound('sounds/sounds_bangLarge.wav')
bangSmall = pygame.mixer.Sound('sounds/sounds_bangSmall.wav')
shoot.set_volume(.25)
bangLarge.set_volume(.25)
bangSmall.set_volume(.25)

pygame.display.set_caption('Asteroids')
window = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

gameover: bool = False
lives: int = 3
score: int = 0
rapid_fire: bool = False
rf_start: int = -1
isSoundOn: bool = True
highScore: int = 0


class Player(object):
    def __init__(self):
        self.img = playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle: int = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, window):
        #  window.blit(self.img, [self.x, self.y, self.w, self.h])
        window.blit(self.rotatedSurf, self.rotatedRect)

    def turn_left(self):
        self.angle += 10
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def turn_right(self):
        self.angle -= 10
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def move_forward(self):
        self.x += self.cosine * 10
        self.y -= self.sine * 10
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def update_location(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < - 50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0


class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w: int = 7
        self.h: int = 7
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.w, self.h])

    def check_off_screen(self):
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:
            return True


class Asteroid(object):
    def __init__(self, rank: int):
        self.rank: int = rank
        if rank == 1:
            self.image = asteroid50
        elif rank == 2:
            self.image = asteroid100
        elif rank == 3:
            self.image = asteroid150
        self.w = rank * 50
        self.h = rank * 50
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w),
                                        random.choice([- 1 * self.h - 5, sh + 5])),
                                       (random.choice([- 1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw // 2:
            self.xdir = 1
        else:
            self.xdir = -1

        if self.y < sh // 2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))


class Star(object):
    def __init__(self):
        self.img = star
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w),
                                        random.choice([- 1 * self.h - 5, sh + 5])),
                                       (random.choice([- 1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw // 2:
            self.xdir = 1
        else:
            self.xdir = -1

        if self.y < sh // 2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


class Alien(object):
    def __init__(self):
        self.img = alienImg
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w),
                                        random.choice([- 1 * self.h - 5, sh + 5])),
                                       (random.choice([- 1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw // 2:
            self.xdir = 1
        else:
            self.xdir = -1

        if self.y < sh // 2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


class AlienBullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w: int = 4
        self.h: int = 4
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.w, self.h])


def redraw_game_window():
    window.blit(bg, (0, 0))
    font = pygame.font.SysFont('arial', 30)
    lives_text = font.render('Lives: ' + str(lives), True, (255, 255, 255))
    play_again_text = font.render('Press Space to Play Again', True, (255, 255, 255))
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    highscore_text = font.render('Highscore: ' + str(highScore), True, (255, 255, 255))

    player.draw(window)
    for ast in asteroids:
        ast.draw(window)
    for bull in playerBullets:
        bull.draw(window)
    for st in stars:
        st.draw(window)
    for al in aliens:
        al.draw(window)
    for abull in alienBullets:
        abull.draw(window)

    if rapid_fire:
        pygame.draw.rect(window, (0, 0, 0), [sw // 2 - 51, 19, 102, 22])
        pygame.draw.rect(window, (255, 255, 255), [sw // 2 - 50, 20, 100 - 100 * (count - rf_start) / 500, 20])

    if gameover:
        window.blit(play_again_text, (sw // 2 - play_again_text.get_width() // 2, sh // 2 - play_again_text.get_height()
                                      // 2))
    window.blit(score_text, (sw - score_text.get_width() - 25, 25))
    window.blit(lives_text, (25, 25))
    window.blit(highscore_text, (sw - highscore_text.get_width() - 25, 35 + score_text.get_height()))
    pygame.display.update()


player = Player()
playerBullets: list = []
asteroids: list = []
count: int = 0
stars: list = [Star()]
aliens: list = [Alien()]
alienBullets: list = []

run: bool = True
while run:
    clock.tick(60)
    count += 1
    if not gameover:
        if count % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(ran))
        if count % 1000 == 0:
            stars.append(Star())
        if count % 750 == 0:
            aliens.append(Alien())
        for i, a in enumerate(aliens):
            a.x += a.xv
            a.y += a.yv
            if a.x > sw + 150 or a.x + a.w < - 100 or a.y > sh + 150 or a.y + a.h < - 100:
                aliens.pop(i)
            if count % 60 == 0:
                alienBullets.append(AlienBullet(a.x + a.w // 2, a.y + a.h // 2))

            for b in playerBullets:
                if a.x <= b.x <= a.x + a.w or a.x <= b.x + b.w <= a.x + a.w:
                    if a.y < b.y <= a.y + a.h or a.y <= b.y + b.h <= a.y + a.h:
                        aliens.pop(i)
                        if isSoundOn:
                            bangLarge.play()
                        score += 50
                        break

        for i, b in enumerate(alienBullets):
            b.x += b.xv
            b.y += b.yv
            if player.x - player.w // 2 <= b.x <= player.x + player.w // 2 or player.x - player.w // 2 <= b.x + b.w <= \
                    player.x + player.w // 2:
                if player.y - player.h // 2 < b.y <= player.y + player.h // 2 or player.y - player.h // 2 <= b.y + b.h \
                        <= player.y + player.h // 2:
                    lives -= 1
                    alienBullets.pop(i)
                    break

        player.update_location()
        for b in playerBullets:
            b.move()
            if b.check_off_screen():
                playerBullets.pop(playerBullets.index(b))

        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if player.x + player.w // 2 >= a.x >= player.x - player.w // 2 or player.x + player.w // 2 >= a.x + a.w >= \
                    player.x - player.w // 2:
                if player.y + player.h // 2 >= a.y >= player.y - player.h // 2 or \
                        player.y + player.h // 2 >= a.y + a.h >= player.y - player.h // 2:
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    if isSoundOn:
                        bangLarge.play()
                    break

            for b in playerBullets:
                if a.x <= b.x <= a.x + a.w or a.x <= b.x + b.w <= a.x + a.w:
                    if a.y < b.y <= a.y + a.h or a.y <= b.y + b.h <= a.y + a.h:
                        if a.rank == 3:
                            if isSoundOn:
                                bangLarge.play()
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            if isSoundOn:
                                bangSmall.play()
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 30
                            if isSoundOn:
                                bangSmall.play()
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
                        break

        for s in stars:
            s.x += s.xv
            s.y += s.yv
            if sw + 100 < s.x < - 100 - s.w or - s.h - 100 < s.y > sh + 100:
                stars.pop(stars.index(s))
                break
            for b in playerBullets:
                if s.x <= b.x <= s.x + s.w or s.x <= b.x + b.w <= s.x + s.w:
                    if s.y < b.y <= s.y + s.h or s.y <= b.y + b.h <= s.y + s.h:
                        rapid_fire: bool = True
                        rf_start = count
                        stars.pop(stars.index(s))
                        playerBullets.pop(playerBullets.index(b))
                        break

        if lives <= 0:
            gameover: bool = True

        if rf_start != - 1:
            if count - rf_start > 500:
                rapid_fire: bool = False
                rf_start = - 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.move_forward()
        if keys[pygame.K_SPACE]:
            if rapid_fire:
                playerBullets.append(Bullet())
                if isSoundOn:
                    shoot.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    if not rapid_fire:
                        playerBullets.append(Bullet())
                        if isSoundOn:
                            shoot.play()
                else:
                    gameover: bool = False
                    lives: int = 3
                    asteroids.clear()
                    aliens.clear()
                    alienBullets.clear()
                    stars.clear()
                    if score > highScore:
                        highScore = score
                    score: int = 0
            if event.key == pygame.K_m:
                isSoundOn = not isSoundOn

    redraw_game_window()
pygame.quit()
