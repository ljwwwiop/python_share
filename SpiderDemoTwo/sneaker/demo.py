'''
    贪吃蛇 pygame 和 freegames
'''

from turtle import *
from random import randrange
from freegames import square,vector
import pygame
import time
import turtle

class Greedy_snake(turtle.Turtle):
    # 定义初始化变量,猎物，蛇，前进和长度信息
    def __init__(self):
        self.prey = vector(0,0)
        self.snake = [vector(10,0)]
        self.target = vector(0,-10)

    # 改变蛇运行的方向
    def cha_dire(self,x,y):
        self.target.x = x
        self.target.y = y

    '''
    蛇的移动，是利用了人们的视觉误差，其实贪吃蛇就是不断的添加新的位置信息，
    同时将位于列表最前部的位置剔除，
    如果蛇吃掉了食物，那么就不剔除列表最前面的元素
    '''
    # 判断是否触碰到了边界
    def inside(self,head):
        return -220<head.x< 220 and -220 <head.y<220

    # 初级模式
    def crawl_pri(self):
        head = self.snake[-1].copy()
        head.move(self.target)

        if not self.inside(head) or head in self.snake:
            square(head.x,head.y,11,'red')
            update()
            return  # 不停的运动
        self.snake.append(head)

        if head == self.prey:
            print("Snake:",len(self.snake))
            self.prey.x = randrange(-15,15) * 10
            self.prey.y = randrange(-15,15) * 10
        else:
            self.snake.pop(0) # pop 堆栈的思想
        clear() # 清空重新画蛇
        # time.sleep(2)
        for i in self.snake:
            square(i.x,i.y,11,'black')

        square(self.prey.x,self.prey.y,11,'yellow')
        update() # 请屏幕
        ontimer(self.crawl_pri,250) # 每隔300ms 重新执行函数

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
        ontimer(self.crawl_mid, 180)

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
    '''
        头部位置判断，通过self.inside(head) or head in self.snake来
        判断当蛇的头部碰到边界或者是蛇的头部碰到自己的身体时，蛇应当“死亡”。
        
        判断是否吃到食物 head == self.prey，当蛇吃到食物的时候，食物的位置应该重新定义，
        如果蛇没有吃到食物，那么蛇就应当减少一个vector（self.snake.pop(0)），否则蛇的身体会不断的增长。
    '''

    # 第三部分 界面等级设计
    def button(self,screen,position,text):
        bwidth = 305
        bheight = 30
        left,top = position
        pygame.draw.rect(screen,(100,100,100),(left,top,bwidth,bheight))
        font = pygame.font.Font(r'D:\python\pycharm\ziti\simhei.ttf',50)
        text_render = font.render(text,1,(0,255,0))
        return screen.blit(text_render, (left + 50,top + 10))

    def init_surface(self,screen):
        clock = pygame.time.Clock()
        # background = pygame.image.load("bg1.png")
        while True:
            button_pri = self.button(screen,(100,50),"初级玩家")
            button_mid = self.button(screen,(100,200),"中级玩家")
            button_adv = self.button(screen,(100,350),"高级玩家")
            # 利用pygame中的键盘监控，当不同的按钮捕获到了鼠标在自己的范围内被按下时，
            # 便返回对应的数字，通过返回对应的数字，便可以知道玩家进入的是哪个玩家模式。
            for event in pygame.event.get():
                if event.type ==pygame.MOUSEBUTTONDOWN:
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
        pygame.display.set_caption('Greek snk - by 未加连 v1.0')
        mode = self.init_surface(screen)
        pygame.quit()
        return mode

    def start(self):
        mode = self.mode_choice()
        screen = getscreen()
        screen.title("Greedy Snake - by 未加连 v1.0")
        setup(500,550,120,200)
        bgpic("bg1.png")
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda :self.cha_dire(10,0),'Right')
        onkey(lambda: self.cha_dire(-10, 0), 'Left')
        onkey(lambda: self.cha_dire(0, 10), 'Up')
        onkey(lambda: self.cha_dire(0, -10), 'Down')
        # 速度控制
        # self.crawl(size = size,speed = speed)
        if mode ==1:
            self.crawl_pri()
        elif mode == 2:
            self.crawl_mid()
        else:
            self.crawl_adv()
        done()

if __name__ == '__main__':
    snake = Greedy_snake()
    snake.start()

