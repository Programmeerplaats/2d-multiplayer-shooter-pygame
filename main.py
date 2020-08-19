import pygame

from pygame import mixer
from bullet import Bullet
from player import Player

# De pre_init() method aanroepen voor pygame.init(), om vertraging van schietgeluid te voorkomen
pygame.mixer.pre_init(44100, -16, 1, 512)

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
bulletPlayer1Image = pygame.image.load('images/bullet-player1.png')
bulletPlayer2Image = pygame.image.load('images/bullet-player2.png')

# Achtergrondmuziek en schietgeluid laden. Achtergrondmuziek ook afspelen
mixer.music.load('sounds/background-music.ogg')
mixer.music.play(-1)
shotSound = mixer.Sound('sounds/shot-sound.ogg')

# Objecten
p1 = Player(626, 400)
p2 = Player(10, 10)
b1 = Bullet(p1.x)
b2 = Bullet(p2.x)

# Game loop
running = True
while running:

    # blit() method aanroepen om achtergrond afbeelding op scherm te krijgen
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # De status van alle toetsenbord knoppen ophalen
    keys = pygame.key.get_pressed()

    # Checken welke toetsenbord knoppen worden gebruikt en players verticaal laten bewegen
    if keys[pygame.K_UP]:
        p1.y -= 2
    if keys[pygame.K_DOWN]:
        p1.y += 2
    if keys[pygame.K_w]:
        p2.y -= 2
    if keys[pygame.K_s]:
        p2.y += 2
    # Bij druk op bijbehorende knop checken of bullet state "ready" is, zoja dan y-coördinaat startpositie
    # van player geven aan y-coordinaat van bullet en status veranderen
    if keys[pygame.K_SPACE]:
        if b1.state == "ready":
            shotSound.play()
            b1.y = p1.y
            b1.state = "fire"
    if keys[pygame.K_d]:
        if b2.state == "ready":
            shotSound.play()
            b2.y = p2.y
            b2.state = "fire"

    # Grenzen scherm checken en players niet door grenzen heen laten gaan
    p1.boundaries(p1.y)
    p2.boundaries(p2.y)

    # Objecten op scherm plaatsen
    p1.draw(screen, player1Image)
    p2.draw(screen, player2Image)

    # Als state van bullet "fire" is, dan bullet op scherm laten vertonen en schieten
    if b1.state == "fire":
        b1.draw(screen, bulletPlayer1Image, b1.y)
        b1.x -= 3
    if b2.state == "fire":
        b2.draw(screen, bulletPlayer2Image, b2.y)
        b2.x += 3
    # Bullets resetten als zijkant van scherm wordt geraakt, zodat player daarna opnieuw kan schieten
    if b1.x <= 0:
        b1.x = p1.x
        b1.state = "ready"
    if b2.x >= 676:
        b2.x = p2.x
        b2.state = "ready"

    # Rechthoekige coördinaten van objecten opslaan
    player1Rect = pygame.Rect(p1.x, p1.y, 64, 64)
    player2Rect = pygame.Rect(p2.x, p2.y, 64, 64)
    bullet1Rect = pygame.Rect(b1.x, b1.y, 24, 24)
    bullet2Rect = pygame.Rect(b2.x, b2.y, 24, 24)

    # Botsing checken tussen kogel en player, bij botsing kogel weer resetten
    if bullet1Rect.colliderect(player2Rect):
        print("Botsing tussen kogel van player 1 en player 2")
        b1.x = p1.x
        b1.state = "ready"
    if bullet2Rect.colliderect(player1Rect):
        print("Botsing tussen kogel van player 2 en player 1")
        b2.x = p2.x
        b2.state = "ready"

    # Update het scherm
    pygame.display.update()
