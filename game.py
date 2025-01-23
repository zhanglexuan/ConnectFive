import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#二维列表
map = [0] * 15
for i in range(15):
    map[i] = [0] * 15

pygame.init()
SCREEN = pygame.display.set_mode((750, 750))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = round((y - 25)/50)
            col = round((x - 25)/50)
            map[row][col] = 1

    SCREEN.fill("#EE9A49")

    #画竖线
    for x in range(15):
        pygame.draw.line(SCREEN, BLACK, (25+50*x, 25), (25+50*x, 725), 2)
    #画横线
    for y in range(15):
        pygame.draw.line(SCREEN, BLACK, (25, 25+50*y), (725, 25+50*y), 2)
    #确定中心点
    pygame.draw.circle(SCREEN, BLACK, (25+50*7, 25+50*7), 8)

    #鼠标位置获取
    x, y = pygame.mouse.get_pos()
    x = round((x - 25)/50) * 50 + 25
    y = round((y - 25)/50) * 50 + 25

    #落子提醒
    pygame.draw.rect(SCREEN, WHITE, (x - 25, y - 25, 50, 50), 2)

    #绘制棋子
    for row in range(15):
        for col in range(15):
            if map[row][col] == 1:
                pygame.draw.circle(SCREEN, BLACK, (col*50+25, row*50+25), 25)

    pygame.display.update()

pygame.quit()