from models import *

background = transform.scale(image.load("back.jpeg"),WINDOW_SIZE)
player1 = Player("player.png", Sprite_Size[0], WINDOW_SIZE[1] - Sprite_Size[1], 5, Sprite_Size)
player2 = Player("player.png", WINDOW_SIZE[0] - Sprite_Size[0]*2, 0, 5, Sprite_Size)

ball = GameSprite("ball.png", WINDOW_SIZE[0]/2-BALL_SIZE[0]/2,WINDOW_SIZE[1]/2-BALL_SIZE[1]/2,0,BALL_SIZE)
speed_x = 3
speed_y= 3

clock = time.Clock()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            finish == True
        
    if not finish:
        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <= 0 or ball.rect.y >= WINDOW_SIZE[1]-ball.rect.height:
            speed_y *= -1.1

        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            speed_x *= -1.1

        player1.reset()
        player2.reset()
        ball.reset()

        player1.move()
        player2.move()

    clock.tick(FPS)
    display.update()