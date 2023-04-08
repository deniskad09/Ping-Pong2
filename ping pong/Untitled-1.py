from pygame import *
# необходимые классы

img_racket = 'racket.png'
img_ball = 'tenis_ball.png'


# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 # конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
       # Вызываем конструктор класса (Sprite):
       super().__init__() 
 
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (widht, height))
       self.speed = player_speed
 
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 # метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
# класс главного игрока
class Player(GameSprite):
   # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        

# Создаем окошко
back = (200,255,255)  # цвет фона - синий
win_width = 600
win_height = 500
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
window.fill(back)



game = True
finish = False
clock = time.Clock()
FPS = 60



# создаем спрайты (размеры неверные)
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player(img_racket, 530, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None,35)
lose1 = font.render('Игрок 1 проиграл', True, (180,0,0))
lose2 = font.render('Игрок 2 проиграл', True, (180,0,0))
speed_x = 5 
speed_y = 5

# Основной цикл игры:
while game:

    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False          
    # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if finish != True:
        window.fill(back)

        # производим движения спрайтов
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        # если мяч достиг границы левой или правой то он долден поменять направление
        if ((ball.rect.y > win_height - 30) or (ball.rect.y < 0) ): # 30 зависит от размера спрайта
            speed_y *= -1
            
        #если мяч улетел дальше ракетки, то проигрыш
        if (ball.rect.x < 0):
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
            
      
        #если мяч улетел даьлше ракетки, выводим условие lose2 для второго игрока
        if (ball.rect.x > win_width):
            finish = True
            window.blit(lose2, (200,200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()
            

        

        display.update()
        clock.tick(FPS)