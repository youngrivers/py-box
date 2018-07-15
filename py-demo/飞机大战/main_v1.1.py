import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))
pygame.display.update()

# 绘制英雄
hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (200, 500))
pygame.display.update()

hero_rect = pygame.Rect(200,500,102,126)
clock = pygame.time.Clock()
while True:
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # exit()终止程序
            exit()
    hero_rect.y -= 1
    if hero_rect.y < 0:
        hero_rect.y = 500
    screen.blit(bg, (0, 0))
    screen.blit(hero, (hero_rect))
    print(hero_rect.y)
    pygame.display.update()
