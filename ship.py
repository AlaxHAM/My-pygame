import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """初始化飞船并设置其初始位置"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

    # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # 将每艘新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # 在飞船的属性中 center 中存储小数值
        self.center = float(self.rect.centerx)

    # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1

        # 更新飞船的 center 值，而不是 rect
        # if self.moving_right:
        #     self.center += self.ai_settings.ship_speed_factor
        # if self.moving_left:
        #     self.center -= self.ai_settings.ship_speed_factor

        if self.moving_right and self.rect.right < self.screen_rect.right:
            # print(self.rect.right, self.screen_rect.right)
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # print(self.rect.left, self.screen_rect.left)
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 的值来更新 rect 对象    rect 只会取值的整数部分
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx







