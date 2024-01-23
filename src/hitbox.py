from src.player_pos import PlayerPos


class Hitbox(PlayerPos):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def collide_with(self, other_hitbox) -> bool:
        pass

    def update_position(self, x, y):
        pass
