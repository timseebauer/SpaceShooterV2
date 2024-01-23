from src.asteroid import Asteroid


class SmallAsteroid(Asteroid):
    def __init__(self, x, y, move_speed, dmg, hp, sprite):
        super().__init__(x, y, move_speed, sprite, dmg, hp)
