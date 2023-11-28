class Spaceship:
    def __init__(self, x, y):
        self.x = Vec2.x
        self.y = Vec2.y
        self.speed = 5
        self.hp = 5
        self.hitbox_radius = 3
        self.weapon = None
        self.sprite = None

    def move(self):
        pass

    def shoot(self):
        pass
