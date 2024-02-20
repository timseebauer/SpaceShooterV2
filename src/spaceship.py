from src.bullet import Bullet


class Spaceship:
    def __init__(self, x, y, move_speed, hp, sprite):
        self.x = x
        self.y = y
        self.move_speed = move_speed
        self.hp = hp
        self.sprite = sprite
        self.hitbox = None
        self.weapon = None

    def move(self, x, y):
        pass

    def shoot(self) -> Bullet:
        pass
