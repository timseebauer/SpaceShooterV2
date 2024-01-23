class BigAsteroid:
    def __init__(self, x, y, move_speed, dmg, hp, sprite):
        self.x = x
        self.y = y
        self.moveSpeed = move_speed
        self.dmg = dmg
        self.hp = hp
        self.split_probability = 0.7
        self.sprite = sprite

    def move(self, x, y):
        pass

    def split(self):
        pass
