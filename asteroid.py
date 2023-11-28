from vec2 import Vec2


class Asteroid:
    def __init__(self, pos: Vec2, speed, hitbox_radius, hp, damage, sprite):
        self.pos = Vec2
        self.speed = speed
        self.hitbox_radius = hitbox_radius
        self.hp = hp
        self.damage = damage
        self.sprite = None

    def move(self):
        pass

    def split(self):
        pass