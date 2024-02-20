class Bullet:
    def __init__(self, x, y, dmg, sprite, move_speed):
        self.x = x
        self.y = y
        self.dmg = dmg
        self.sprite = sprite
        self.move_speed = move_speed
        self.hitbox = None

    def move(self, x, y):
        pass
