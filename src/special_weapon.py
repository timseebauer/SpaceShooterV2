from src.bullet import Bullet
from src.weapon import Weapon


class SpecialWeapon(Weapon):
    def __init__(self, cooldown):
        super().__init__(cooldown)

    def shoot(self, x, y) -> Bullet:
        pass
