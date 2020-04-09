from turtle import *
from random import randrange
from freegames import square, vector
import turtle
import pygame
import time


class Greedy_snake(turtle.Turtle):
    def __init__(self):#定义初始的变量，包括猎物、蛇和前进的步长信息
        self.prey = vector(0, 0)
        self.snake = [vector(10, 0)]
        self.target = vector(0, -10)

    def cha_dire(self,x, y):#改变蛇的运行方向
        self.target.x = x
        self.target.y = y

    def inside(self,head):#判断是否触碰到了边界
        return -220 < head.x < 220 and -220 < head.y < 220

    def crawl_pri(self):#初级模式
        head = self.snake[-1].copy()
        head.move(self.target)

        if not self.inside(head) or head in self.snake:
            square(head.x, head.y, 11, 'red')
            update()
            return #目的是让其停止不动
        self.snake.append(head)

        if head == self.prey:
            print('Snake:', len(self.snake))
            self.prey.x = randrange(-15, 15) * 10
            self.prey.y = randrange(-15, 15) * 10
        else:
            self.snake.pop(0)
        clear()#清空屏幕，重新画出蛇、食物
        # time.sleep(1)
        for i in self.snake:
            square(i.x, i.y, 11, 'black')

        square(self.prey.x, self.prey.y, 11, 'yellow')
        update()#更新屏幕
        ontimer(self.crawl_pri, 300)#每隔300ms重新执行函数

    def crawl_mid(self):
        head = self.snake[-1].copy()
        head.move(self.target)

        if not self.inside(head) or head in self.snake:
            square(head.x, head.y, 10, 'red')
            update()
            return  # 目的是让其停止不动
        self.snake.append(head)

        if head == self.prey:
            print('Snake:', len(self.snake))
            self.prey.x = randrange(-15, 15) * 10
            self.prey.y = randrange(-15, 15) * 10
        else:
            self.snake.pop(0)
        clear()
        for i in self.snake:
            square(i.x, i.y, 10, 'black')

        square(self.prey.x, self.prey.y, 10, 'yellow')
        update()
        ontimer(self.crawl_mid, 200)

    def crawl_adv(self):
        head = self.snake[-1].copy()
        head.move(self.target)

        if not self.inside(head) or head in self.snake:
            square(head.x, head.y, 9, 'red')
            update()
            return  # 目的是让其停止不动
        self.snake.append(head)

        if head == self.prey:
            print('Snake:', len(self.snake))
            self.prey.x = randrange(-15, 15) * 10
            self.prey.y = randrange(-15, 15) * 10
        else:
            self.snake.pop(0)
        clear()
        for i in self.snake:
            square(i.x, i.y, 9, 'black')

        square(self.prey.x, self.prey.y, 9, 'yellow')
        update()
        ontimer(self.crawl_adv, 100)

    def button(self,screen, position, text):
        bwidth = 305
        bheight = 60
        left, top = position
        pygame.draw.rect(screen, (100, 100, 100), (left, top, bwidth, bheight))
        font = pygame.font.Font(r'D:\python\pycharm\ziti\simhei.ttf', 50)
        text_render = font.render(text, 1, (0, 255, 0))
        return screen.blit(text_render, (left + 50, top + 10))

    def init_surface(self, screen):
        clock = pygame.time.Clock()
        # background = pygame.image.load("bg1.png")
        while True:
            button_pri = self.button(screen, (100, 50), '初级玩家')
            button_mid = self.button(screen, (100,200), '中级玩家')
            button_adv = self.button(screen, (100, 350), '高级玩家')

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_pri.collidepoint(pygame.mouse.get_pos()):
                        return 1
                    elif button_mid.collidepoint(pygame.mouse.get_pos()):
                        return 2
                    elif button_adv.collidepoint(pygame.mouse.get_pos()):
                        return 3

            clock.tick(60)
            pygame.display.update()

    def mode_choice(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Greedy Snak')
        mode = self.init_surface(screen)
        pygame.quit()
        return mode

    def start(self):
        mode = self.mode_choice()
        screen = getscreen()
        screen.title("Greedy Snake")
        setup(500, 500,120,200)
        bgpic('bg1.png')
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: self.cha_dire(10, 0), 'Right')
        onkey(lambda: self.cha_dire(-10, 0), 'Left')
        onkey(lambda: self.cha_dire(0, 10), 'Up')
        onkey(lambda: self.cha_dire(0, -10), 'Down')
        # self.crawl(size=size,speed=speed)
        if mode == 1:
            self.crawl_pri()
        elif mode == 2:
            self.crawl_mid()
        else:
            self.crawl_adv()
        done()


if __name__ == '__main__':

    snake = Greedy_snake()
    snake.start()