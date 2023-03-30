from pygame import *
WINDOW_SIZE = (700, 500)
Sprite_Size = (65, 65)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BlacK = (0, 0, 0)
FPS = 60
BALL_SIZE = (50,50)

window = display.set_mode(WINDOW_SIZE)
font.init()
font = font.Font(None, 18)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x_pos, y_pos, speed, size):
        super().__init__()
        self.image = transform.scale(image.load(image_name), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WINDOW_SIZE[1] - 100:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WINDOW_SIZE[0] - 50:
            self.rect.x += self.speed