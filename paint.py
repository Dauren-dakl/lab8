import pygame
import os
pygame.init()
os.chdir(r"C:\\Users\\Acer\\Desktop\\PP2")

screen = pygame.display.set_mode((1080, 900))

clock = pygame.time.Clock()

RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

eraser = pygame.image.load('erase.jpg')
eraser = pygame.transform.scale(eraser, (70, 70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

def draw_circle(surface, color, pos, radius=40):
    pygame.draw.circle(surface, color, pos, radius)

def draw_triangle(surface, color, pos):
    x, y = pos
    points = [(x, y - 40), (x - 35, y + 40), (x + 35, y + 40)]
    pygame.draw.polygon(surface, color, points)

def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
        elif 180 <= x <= 220 and 0 <= y <= 40:
            return "circle"
        elif 230 <= x <= 270 and 0 <= y <= 40:
            return "triangle"
    return color

def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color == 'circle':
            draw_circle(screen, WHITE, (x, y))
        elif color == 'triangle':
            draw_triangle(screen, WHITE, (x, y))
        else:
            pygame.draw.circle(screen, color, (x, y), 27)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(colors)):
        draw_rect(i)
    screen.blit(eraser, (1010, 0))
    pygame.draw.circle(screen, WHITE, (200, 20), 20)
    pygame.draw.polygon(screen, WHITE, [(250, 0), (230, 40), (270, 40)])

    color = pick_color()
    painting(color)

    clock.tick(60)
    pygame.display.update()
