import pygame

class Square(pygame.sprite.Sprite):

    pygame.font.init()
    SQUARE_SIZE = 84
    LEFT_MARGIN = 117
    PADDING = 20
    font = pygame.font.SysFont('Helvetica', 85)

    def __init__(self, x, y, num):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((Square.SQUARE_SIZE, Square.SQUARE_SIZE))
        #self.image.fill(pygame.Color('white'))
        self.rect = self.image.get_rect()

        self.set_coordinates(x, y)

        self.num = num

        self.clicked = False

        self.show_number()

    def on_click(self):
        self.image.fill(pygame.Color('black'))
        self.clicked = True
        print("clicked")

    def hide_number(self):
        self.image.fill(pygame.Color('white'))

    def show_number(self):
        self.image.fill(pygame.Color('black'))
        text_surface = self.font.render(str(self.num), 1, pygame.Color('white'))
        text_rect = text_surface.get_rect(center=(Square.SQUARE_SIZE // 2, Square.SQUARE_SIZE // 2))

        self.image.blit(text_surface, text_rect)

    def set_coordinates(self, x, y):
        self.rect.x = Square.LEFT_MARGIN + Square.PADDING * x + Square.SQUARE_SIZE * (x - 1)
        self.rect.y = Square.PADDING * y + Square.SQUARE_SIZE * (y - 1)

