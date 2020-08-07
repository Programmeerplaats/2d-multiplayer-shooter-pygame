class Player:

    x = 0
    y = 0

    def __init__(self):
        print('Als je een object aanmaakt, zie je dit op je scherm!')

    def set_start_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, player):
        screen.blit(player, (self.x, self.y))
