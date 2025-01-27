import pygame

pygame.init()
font = pygame.font.Font("font.ttf", 24)
SCREEN = pygame.display.set_mode((750, 850))
pygame.display.set_caption("五子棋")

class Button:
    def __init__(self, x, y, width, height, text, color, click_color, text_color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.click_color = click_color
        self.text_color = text_color
        self.clicked = False

    def draw(self, screen):
        if self.clicked:
            pygame.draw.rect(screen, self.click_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center = self.rect.center)
        SCREEN.blit(text_surface, text_rect)