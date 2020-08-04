import pygame

# Pygame initialiseren
pygame.init()

# Screen aanmaken
screen = pygame.display.set_mode((700, 500))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False