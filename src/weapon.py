from src.bullet import Bullet


class Weapon:
    def __init__(self, cooldown):
        self.cooldown = cooldown

    def shoot(self, x, y) -> Bullet:
        pass
