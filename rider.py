import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
car_image = pygame.image.load('CAR.png').convert_alpha()
car_image = pygame.transform.scale(car_image, (150, 150))
coin_image = pygame.image.load('COIN.png').convert_alpha()
coin_image = pygame.transform.scale(coin_image, (70, 70))
train_image = pygame.image.load('train.png').convert_alpha()
train_image = pygame.transform.scale(train_image, (150, 150))

# Car setup
car_x, car_y = WIDTH // 2, HEIGHT - 120
car_speed = 0.8

# Train setup
train_width = 70
train_height = 100
train_x = random.randint(0, WIDTH - train_width)
train_y = -100
train_speed = 0.5

# Coin setup
coin_x = random.randint(0, WIDTH - 30)
coin_y = -100
coin_speed = 0.4
coins_collected = 0

# Font for score display
font = pygame.font.SysFont(None, 48)

def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

def draw_objects():
    screen.blit(background_image, (0, 0))
    screen.blit(car_image, (car_x, car_y))
    screen.blit(train_image, (train_x, train_y))
    screen.blit(coin_image, (coin_x, coin_y))
    draw_text(f"Coins: {coins_collected}", font, BLACK, WIDTH - 150, 10)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed

    # Train movement
    train_y += train_speed
    if train_y > HEIGHT:
        train_y = -train_height
        train_x = random.randint(0, WIDTH - train_width)

    # Coin movement
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -30
        coin_x = random.randint(0, WIDTH - 30)

    # Collision detection with train
    if (train_x < car_x < train_x + train_width or
        train_x < car_x + 50 < train_x + train_width) and \
        (train_y < car_y < train_y + train_height or
         train_y < car_y + 100 < train_y + train_height):
        print("Game Over")
        running = False

    # Collision detection with coin
    if (coin_x < car_x < coin_x + 30 or
        coin_x < car_x + 50 < coin_x + 30) and \
        (coin_y < car_y < coin_y + 30 or
         coin_y < car_y + 100 < coin_y + 30):
        coins_collected += 1
        coin_y = -30
        coin_x = random.randint(0, WIDTH - 30)

    # Draw everything
    draw_objects()
    pygame.display.update()

pygame.quit()
