#оно живое
from pygame import *
font.init()
font1 = font.SysFont("Arial", 60)
win = font1.render('You WIN!', True, (0, 255, 0))
lose = font1.render('KO! You lost 10M', True, (255, 0, 0))
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
window = display.set_mode((700, 500))
display.set_caption("лабиринт")
class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - 65:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 700 - 65:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 700 - 50:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, w, h, color, x, y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player("magikarp.png", 60, 55, 5, 50, 400)
enemy = Enemy('rowlet.png', 60, 60, 10, 600, 300)

gold = GameSprite('suhariki.jpg', 70, 70, 1, 620, 420)
wall1 = Wall(30, 130, (255, 200, 0), 120, 400)
wall2 = Wall(30, 130, (255, 200, 0), 120, 300)
wall3 = Wall(120, 5, (255, 200, 0), 100, 300)
wall4 = Wall(30, 240, (255, 200, 0), 400, 200)
wall5 = Wall(300, 30, (255, 200, 0), 250, 200)
wall6 = Wall(30, 200, (255, 200, 0), 150, 10)
wall7 = Wall(15, 240, (255, 200, 0), 360, 200)
wall8 = Wall(30, 200, (255, 200, 0), 360, 90)
wall9 = Wall(45, 130, (255, 200, 0), 250, 300)
wall10 = Wall(15, 150, (255, 200, 0), 500, 400)  
wall11 = Wall(15, 100, (255, 200, 0), 500, 20)
walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11)  
background = transform.scale(image.load("piramida.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60
finish = False
while game:
    if finish == False:
        window.blit(background, (0, 0))
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        gold.reset()
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 50
            player.rect.y = 400
        if sprite.collide_rect(player, gold):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, enemy):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
