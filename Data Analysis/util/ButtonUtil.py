import pygame


class Button:
    def __init__(self, screen, centerXY, width, height, buttonColor, textColor, message, size):
        """初始化按钮属性"""
        self.screen = screen
        """按钮宽高"""
        self.width = width
        self.height = height
        self.buttonColor = buttonColor
        self.textColor = textColor
        self.font = pygame.font.SysFont("SimHei", size)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = centerXY[0]
        self.rect.centery = centerXY[1]
        self.dealMessage(message)

    def dealMessage(self, message):
        """将message渲染为图像, 并将其在按钮上居中"""
        self.messageImage = self.font.render(message, True, self.textColor, self.buttonColor)
        self.messageImageRect = self.messageImage.get_rect()
        self.messageImageRect.center = self.rect.center

    def drawButton(self):
        # 填充颜色
        self.screen.fill(self.buttonColor, self.rect)
        # 将图像绘制到屏幕外
        self.screen.blit(self.messageImage, self.messageImageRect)
