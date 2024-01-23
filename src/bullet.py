from src.player_pos import PlayerPos


class Bullet(PlayerPos):
    def __init__(self, x, y, dmg, sprite, move_speed):
        super().__init__(x, y)
        self.dmg = dmg
        self.sprite = sprite
        self.move_speed = move_speed

    def move(self, x, y):
        pass
