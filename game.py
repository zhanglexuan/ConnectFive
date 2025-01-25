import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player = 1
winner = 0

#二维列表
map = [0] * 15
for i in range(15):
    map[i] = [0] * 15

pygame.init()
SCREEN = pygame.display.set_mode((750, 750))
pygame.display.set_caption("五子棋")

#五子连珠
def check(row, col):
    #判断左右方向
    score = 1
    for i in range(4):
        if map[row][col + i] == map[row][col + i + 1]:
            score += 1
        else:
            break
    for i in range(4):
        if map[row][col - i] == map[row][col - i - 1]:
            score += 1
        else:
            break
    if score == 5:
            return True

    #判断上下方向
    score = 1
    for i in range(4):
        if map[row + i][col] == map[row + i + 1][col]:
            score += 1
        else:
            break
    for i in range(4):
        if map[row - i][col] == map[row - i - 1][col]:
            score += 1
        else:
            break
    if score == 5:
            return True

    #判断左斜方向
    score = 1
    for i in range(4):
        if map[row + i][col + i] == map[row + i + 1][col + i + 1]:
            score += 1
        else:
            break
    for i in range(4):
        if map[row - i][col - i] == map[row - i - 1][col - i - 1]:
            score += 1
        else:
            break
    if score == 5:
            return True

    #判断右斜方向
    score = 1
    for i in range(4):
        if map[row + i][col - i] == map[row + i + 1][col - i - 1]:
            score += 1
        else:
            break
    for i in range(4):
        if map[row - i][col + i] == map[row - i - 1][col + i + 1]:
            score += 1
        else:
            break
    if score == 5:
            return True


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = round((y - 25)/50)
            col = round((x - 25)/50)
            if map[row][col] == 0:
                map[row][col] = player
                if(check(row, col)):
                    winner = player
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                print("已有棋子")

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
            elif map[row][col] == 2:
                pygame.draw.circle(SCREEN, WHITE, (col*50+25, row*50+25), 25)

    if winner != 0:
        if winner == 1:
            text = "黑子赢了"
            color = BLACK
        if winner == 2:
            text = "白子赢了"
            color = WHITE
        font = pygame.font.Font("font.ttf", 70)
        font_surface = font.render(text, True, color)
        font_pos = (100, 100)
        SCREEN.blit(font_surface, font_pos)

    pygame.display.update()

pygame.quit()