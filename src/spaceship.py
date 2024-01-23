from src.bullet import Bullet
from src.player_pos import PlayerPos


class Spaceship(PlayerPos):
    def __init__(self, x, y, move_speed, hp, sprite):
        super().__init__(x, y)
        self.move_speed = move_speed
        self.hp = hp
        self.sprite = sprite

    def move(self, x, y):
        pass

    def shoot(self) -> Bullet:
        pass
