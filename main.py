import pygame

from player import Player

# Pygame initialiseren
pygame.init()

# Screen aanmaken
screen = pygame.display.set_mode((700, 500))

# Titel game
pygame.display.set_caption("2D MultiPlayer Shooter")

# Afbeeldingen laden
background = pygame.image.load('images/war-background.jpg')
player1Image = pygame.image.load('images/player1.png')
player2Image = pygame.image.load('images/player2.png')

# Objecten
p1 = Player()
p2 = Player()

p1.set_start_position(626, 400)
p2.set_start_position(10, 10)

# Game loop
running = True
while running:

    # blit method aanroepen om achtergrond afbeelding op scherm te krijgen
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        p1.y -= 2
    if keys[pygame.K_DOWN]:
        p1.y += 2
    if keys[pygame.K_w]:
        p2.y -= 2
    if keys[pygame.K_s]:
        p2.y += 2

    # Objecten op scherm plaatsen
    p1.draw(screen, player1Image)
    p2.draw(screen, player2Image)

    # Update het scherm
    pygame.display.update()