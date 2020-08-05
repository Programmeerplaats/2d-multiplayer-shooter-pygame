import pygame

# Pygame initialiseren
pygame.init()

# Screen aanmaken
screen = pygame.display.set_mode((700, 500))

# Titel game
pygame.display.set_caption("2D MultiPlayer Shooter")

# Achtergrond afbeelding laden
background = pygame.image.load('images/war-background.jpg')

# Game loop
running = True
while running:

    # blit method aanroepen om achtergrond afbeelding op scherm te krijgen
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update het scherm
    pygame.display.update()