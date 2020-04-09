import pygame
from demo2 import *

#对象的思想  先写出游戏框架和包 属性
# 在初始化后面 添加游戏窗口
# 2 创建游戏的时钟
# 3 完成创建

class   PlaneGame(object):
    #飞机大战精灵游戏
    def __init__(self):
        print("游戏初始化")
        #1 创建游戏窗口
        # 窗口方法
        pygame.display.set_caption('飞机大战')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2 时钟创建
        self.clock = pygame.time.Clock()
        # 3 完成创建  创建私有方法
        self.__creat_sprites()
        # 4 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY,1000) #1000 是1 秒
        pygame.time.set_timer(HERO_FIRE,500) #1000 是1 秒



    def __creat_sprites(self):
        # 调用方法 传入图片
        bg1 = BackGround('./bg_menu.jpg')
        bg2 = BackGround('./bg1_startcg.jpg')
        bg2.rect.y = -bg2.rect.height  #默认出现在上方
        self.back_group = pygame.sprite.Group(bg1,bg2) #加入一个背景组  可以衔接图片滚动
        self.enemy_group = pygame.sprite.Group()
        self.hero= Hero()
        self.hero_group = pygame.sprite.Group(self.hero)  #添加hero对象
    #游戏循环开始 刷新帧率
    def start_game(self):
        print("游戏开始")
        while True:
            # 1 设置刷新
            self.clock.tick(60)
            # 2 监听事件
            self.__event_handler()
            # 3 碰撞检测
            self.__check_collied()
            # 4 更新绘制
            self.__update_sprites()
            # 5 显示更新
            pygame.display.update()
            #定义私有属性
    def __event_handler(self):
        #遍历 发生的事件 退出  事件判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY:
                #print('敌机出场')
                # 将敌机对象 添加
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE:
                self.hero.fire()
        #捕获用户的操作  操作是数组数据
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collied(self):
        #碰撞检测  子弹 和敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 敌机和本机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        #只出现了一个背景精灵,还需要再来一个反复出现  绘制精灵
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()
