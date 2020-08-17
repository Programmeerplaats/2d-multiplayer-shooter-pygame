class Player:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, player):
        screen.blit(player, (self.x, self.y))
