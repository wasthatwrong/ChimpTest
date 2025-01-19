import pygame
import random
from Square import Square
import time

pygame.init()

NUM_SQUARES = 9

WIDTH = 8
HEIGHT = 5
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, display=0)

game_is_over = False

def game_over():
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(0.2)
    global game_is_over
    game_is_over = True

def generate_squares():
    coordinates_used = []
    sprite_list = pygame.sprite.Group()

    for i in range(1, NUM_SQUARES + 1):
        x = random.randrange(1, WIDTH + 1)
        y = random.randrange(1, HEIGHT + 1)

        while (x, y) in coordinates_used:
            x = random.randrange(1, WIDTH + 1)
            y = random.randrange(1, HEIGHT + 1)

        coordinates_used.append((x, y))
        sprite_list.add(Square(x, y, i))
    return sprite_list

font = pygame.font.SysFont(None, 30)
text = font.render("ESC to quit", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.bottomleft = (5, SCREEN_HEIGHT-5)
screen.blit(text, text_rect)

run = True
while run:
    current_num = 1
    hasClicked = False
    game_is_over = False

    squares = generate_squares()

    screen.fill((0, 0, 0))

    squares.draw(screen)
    screen.blit(text, text_rect)
    pygame.display.flip()

    while not hasClicked and run:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in squares:
                    if square.rect.collidepoint(event.pos):
                        hasClicked = True
                        if square.num != current_num:
                                print("fail")
                                game_over()
                                break
                        else:
                            for sprite in squares:
                                sprite.hide_number()
                            square.on_click()
                            current_num += 1
                            print("success")
                            break


    while hasClicked and run and not game_is_over:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                for square in squares:
                    if square.rect.collidepoint(event.pos):

                        if square.num != current_num:
                            print("fail")
                            game_over()
                            break

                        if current_num == NUM_SQUARES:
                            print("win")
                            game_over()
                            break

                        square.on_click()
                        current_num += 1
                        break


        screen.fill((0, 0, 0))

        squares.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()

pygame.quit()



