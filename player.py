class Player:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, playerimage):
        screen.blit(playerimage, (self.x, self.y))

    def boundaries(self, y):
        if y <= 0:
            self.y = 0
        if y >= 436:
            self.y = 436
