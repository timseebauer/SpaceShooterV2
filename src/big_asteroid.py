from src.asteroid import Asteroid


class BigAsteroid(Asteroid):
    def __init__(self, x, y, move_speed, dmg, hp, sprite):
        super().__init__(x, y, move_speed, dmg, hp, sprite)
        self.split_probability = 0.7

    def split(self):
        pass
