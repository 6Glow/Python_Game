import pygame
import random

pygame.init()
font = pygame.font.SysFont('Sans-serif', 36)

white = (255,255,255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
d = (0, 204, 204)
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

snake_x = screen_width / 2
snake_y = screen_height / 2
snake_speed = 15
snake_size = 10
snake_length = 10
snake_blocks = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 0

game_over = False

running = True
clock = pygame.time.Clock()

while running:

    if not game_over:
        screen.fill((255, 255, 255))

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_blocks.append(snake_head)

        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        for x in snake_blocks[:-1]:
            if x == snake_head:
                game_over = True

        for block in snake_blocks:
            pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])
        pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

        snake_x += speed_x
        snake_y += speed_y

        if snake_x == fruit_x and snake_y == fruit_y:
            fruit_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        if (snake_x >= screen_width or snake_x < 0 or

            snake_y >= screen_height or snake_y < 0):
            # Set game over to true
            game_over = True


    else:
        screen.fill(black)
        score = font.render('You scored: ' + str(snake_length), False, red)
        screen.blit(score, (10, screen_height / 2 - 100))
        text = font.render('You lost! Press \'ESC\' to quit, or \'Spacebar\' to play again', False, red)
        screen.blit(text, (10, screen_height / 2))

    pygame.display.flip()
    clock.tick(snake_speed)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                game_over = False
                snake_x = screen_width / 2
                snake_y = screen_height / 2
                snake_blocks = []
                snake_length = 1

            if event.key == pygame.K_UP:
                speed_x = 0 ** snake_speed
                speed_y = -10
            if event.key == pygame.K_DOWN:
                speed_x = 0 ** snake_speed
                speed_y = 10
            if event.key == pygame.K_LEFT:
                speed_y = 0 ** snake_speed
                speed_x = -10
            if event.key == pygame.K_RIGHT:
                speed_y = 0 ** snake_speed
                speed_x = 10

        if event.type == pygame.QUIT:
            running = False
