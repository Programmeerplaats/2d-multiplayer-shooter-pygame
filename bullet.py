class Bullet:

    x = 0
    y = 0
    state = "ready"

    def __init__(self, x):
        self.x = x

    def shoot(self, screen, bulletimage, y):
        self.y = y
        screen.blit(bulletimage, (self.x, self.y))
