class Asteroid:
    def __init__(self, x, y):
        self.x = Vec2.x
        self.y = Vec2.y
        self.speed = 0
        self.hitbox_radius = 3
        self.hp = 3
        self.damage = 1
        self.sprite = None

    def move(self):
        pass

    def split(self):
        pass