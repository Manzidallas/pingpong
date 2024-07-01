import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 7

# Speeds
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
INC = 1.0001

ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Score
player1_score = 0
player2_score = 0
MAX_SCORE = 9

# Fonts
font = pygame.font.Font(None, 36)

# Paddle positions
player1_y = (HEIGHT - PADDLE_HEIGHT) // 2
player2_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Ball position and speed
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Main game loop
running = True
clock = pygame.time.Clock()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x, ball_speed_y = BALL_SPEED_X * random.choice([-1, 1]), BALL_SPEED_Y * random.choice([-1, 1])
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (20, 20))
    screen.blit(player2_text, (WIDTH - player2_text.get_width() - 20, 20))
    pygame.display.flip()
    pygame.time.wait(2000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED
    if keys[pygame.K_0]:
        pygame.quit()


    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ball_speed_x = float(ball_speed_x)*INC
    ball_speed_y = float(ball_speed_y)*INC

    # Ball collision with top and bottom
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (ball_x - BALL_RADIUS <= PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT) or \
       (ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds (left and right)
    if ball_x < 0:
        player2_score += 1
        reset_ball()

    elif ball_x > WIDTH:
        player1_score += 1
        reset_ball()

    # Drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (20, 20))
    screen.blit(player2_text, (WIDTH - player2_text.get_width() - 20, 20))

    pygame.display.flip()
    clock.tick(60)

    # if conditions for quitting the game
    if player1_score == MAX_SCORE:
        screen.fill(GREEN)
        pygame.display.flip()
        text = font.render("Player 1 wins!", True, WHITE)
        screen.blit(text, (WIDTH // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
    elif player2_score == MAX_SCORE:
        screen.fill(GREEN)
        pygame.display.flip()
        text = font.render("Player 2 wins!", True, WHITE)
        screen.blit(text, (WIDTH // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

pygame.quit()

