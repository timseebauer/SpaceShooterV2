class Hitbox:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def collide_with(self, other_hitbox) -> bool:
        pass

    def update_position(self, x, y):
        pass
