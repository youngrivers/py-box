import pygame

# 初始化模块
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 绘制背景
# 加载图片
bg = pygame.image.load('./images/background.png')
# 绘制图像
screen.blit(bg, (0, 0))
# 刷新窗口
pygame.display.update()

# 绘制英雄
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 500))
pygame.display.update()

# 定义飞机的初始位置
hero_rect = pygame.Rect(200,500,102,126)
# 创建游戏时钟对象
clock = pygame.time.Clock()
# 游戏循环
while True:
    clock.tick(60)  # 设置调用的频率
    # 修改飞机的位置
    hero_rect.y -= 1

    if hero_rect.y < 0:
        hero_rect.y = 500
    # 绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, (hero_rect))
    print(hero_rect.y)
    # 更新
    pygame.display.update()
    # pass
# 游戏结束之前清除
pygame.quit()