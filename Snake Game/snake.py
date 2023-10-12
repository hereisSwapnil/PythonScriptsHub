import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def reset_game():
    global snake, snake_direction, snake_growth, food, game_over, score
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (1, 0)
    snake_growth = False
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0
    game_over = False

# Initialize Snake
reset_game()

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

def show_score():
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

def game_over_screen():
    screen.fill(WHITE)
    game_over_text = font.render("Game Over", True, RED)
    replay_text = font.render("Press 'R' to replay", True, GREEN)
    score_text = font.render(f"Your Score: {score}", True, GREEN)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 70, HEIGHT // 2))
    screen.blit(replay_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))
    pygame.display.update()

def draw_start_screen():
    screen.fill(WHITE)
    start_text = font.render("Press 'Space' to Start", True, GREEN)
    screen.blit(start_text, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.update()
    wait_for_space()

def wait_for_space():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Initial start screen
draw_start_screen()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
            if event.key == pygame.K_r and game_over:
                reset_game()
            if event.key == pygame.K_SPACE and game_over:
                reset_game()

    if game_over:
        game_over_screen()
        wait_for_space()

    else:
        # Move the Snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        # Check for collisions
        if new_head == food:
            snake_growth = True
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            score += 1
        elif new_head in snake or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            game_over = True

        snake.insert(0, new_head)
        
        if not snake_growth:
            snake.pop()
        else:
            snake_growth = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw Snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw Food
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Show the score
        show_score()

        # Update the display
        pygame.display.update()

        # Control the speed of the game
        pygame.time.Clock().tick(SNAKE_SPEED)
