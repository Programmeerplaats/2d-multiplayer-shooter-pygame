import pygame

# Pygame initialiseren
pygame.init()

# Screen aanmaken
screen = pygame.display.set_mode((700, 500))

# Achtergrond afbeelding laden
bg = pygame.image.load('war-background.jpg')

# Game loop
running = True
while running:

    # RGB background
    screen.fill((255, 255, 255))

    # blit method aanroepen om achtergrond afbeelding op scherm te krijgen
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False