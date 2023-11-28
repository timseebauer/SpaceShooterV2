from vec2 import Vec2


class Spaceship:
    def __init__(self, pos: Vec2, speed, hp, hitbox_radius, weapon):
        self.pos = Vec2
        self.speed = speed
        self.hp = hp
        self.hitbox_radius = hitbox_radius
        self.weapon = None
        self.sprite = None

    def move(self):
        pass

    def shoot(self):
        pass
