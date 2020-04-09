import pygame
import random
#屏幕常量定义
SCREEN_RECT = pygame.Rect(0,0,480,800)
#敌机
CREATE_ENEMY = pygame.USEREVENT
#开火   用户事件唯一
HERO_FIRE = pygame.USEREVENT + 1
pygame.display.set_caption('飞机大战')

class GameSprites(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name,speed=1):
        super().__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name)
        #输入图片
        self.rect = self.image.get_rect()
        # 设置大小
        self.speed = speed
        #给速度一个默认的值

        #重写父类方法  父类不满足  子类重写方法
        #保持在水平方向移动
    def update(self, *args):
        self.rect.y +=self.speed

class BackGround(GameSprites):
    #游戏背景类
    def update(self, *args):
        super().update()#继承父类
        #调用height属性  向上为负  向下为正  左为负
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprites):
    #敌机类
    def __init__(self):
        # 敌机模型
        super().__init__('./loading1@2x.png')
        # 敌机速度
        self.speed = random.randint(1,3)
        # 敌机随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill() #clear 不再屏幕内后删除，避免占内存

    #对象结束之前最后调用的
    def __del__(self):
        pass

class Hero(GameSprites):
    #英雄
    def __init__(self):
        super().__init__('./hero0.png',0)#速度为0
        self.rect.centerx = SCREEN_RECT.centerx #初始位置为X轴中间位子
        self.rect.bottom = SCREEN_RECT.bottom - 25 #在X轴上面50px
        self.bullets = pygame.sprite.Group()

    #左右移动 控制速度
    def update(self, *args):
        self.rect.x +=self.speed
        if self.rect.x<0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right= SCREEN_RECT.right

    #定义开火
    def fire(self):
        #创建子弹精灵
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)

    #子弹类
class Bullet(GameSprites):
    def __init__(self):
        super().__init__('p-f02.png',-4) #照片和速度

    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
