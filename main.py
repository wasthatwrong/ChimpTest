import pygame
import random
from Square import Square
import time

pygame.init()
click_sound = pygame.mixer.Sound("sounds/click.mp3")
NUM_SQUARES = 9

WIDTH = 8
HEIGHT = 5
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
best_time = None

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), display=0)
fullscreen = False
game_is_over = False

def draw():
    screen.fill((0, 0, 0))
    squares.draw(screen)
    screen.blit(text, text_rect)
    screen.blit(best_time_text, best_time_text_rect)

    curr_time_text = font.render(f"Time: {elapsed_time:.3f}", True, (255, 255, 255))
    screen.blit(curr_time_text, curr_time_text_rect)

    pygame.display.flip()

def game_over():
    for square in squares:
        square.on_click()

    draw()
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

best_time_text = font.render("Best time: ", True, (255, 255, 255))
best_time_text_rect = text.get_rect()
best_time_text_rect.topleft = (5, 5)
screen.blit(best_time_text, best_time_text_rect)

curr_time_text = font.render(f"Time: 0.000", True, (255, 255, 255))
curr_time_text_rect = text.get_rect()
curr_time_text_rect.topleft = (5, 25)
screen.blit(curr_time_text, curr_time_text_rect)

start_button = pygame.Rect((0, 0, 200, 50))
start_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
start_text = font.render("Start", True, (0, 0, 0))
start_text_rect = start_text.get_rect()
start_text_rect.center = start_button.center
pygame.draw.rect(screen, (255, 255, 255), start_button)
screen.blit(start_text, start_text_rect)
pygame.display.flip()

run = True
ready = False
while run and not ready:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
            ready = True
            click_sound.play()

while run:
    current_num = 1
    hasClicked = False
    game_is_over = False

    squares = generate_squares()
    elapsed_time = 0

    draw()
    start = time.perf_counter()

    while not hasClicked and run:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in squares:
                    if square.rect.collidepoint(event.pos):
                        click_sound.play()
                        hasClicked = True
                        if square.num != current_num:
                                game_over()
                                break
                        else:

                            for sprite in squares:
                                sprite.hide_number()
                            square.on_click()
                            current_num += 1
                            break
        elapsed_time = time.perf_counter() - start
        draw()

    while hasClicked and run and not game_is_over:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

            if event.type == pygame.MOUSEBUTTONDOWN:

                for square in squares:
                    if square.rect.collidepoint(event.pos):
                        click_sound.play()
                        if square.num != current_num:
                            print("fail")
                            game_over()
                            break

                        if current_num == NUM_SQUARES:
                            elapsed = time.perf_counter() - start
                            if best_time is None or elapsed < best_time:
                                best_time = elapsed
                                best_time_text = font.render(f"Best time: {best_time:.3f}", True, (255, 255, 255))
                                curr_time_text = font.render(f"Time: {elapsed_time:.3f}", True, (255, 255, 255))
                            print("win")
                            game_over()
                            break

                        square.on_click()
                        current_num += 1
                        break

        elapsed_time = time.perf_counter() - start
        draw()
pygame.quit()

if best_time is not None:
    print(f"Best time: {best_time:.3f}")


