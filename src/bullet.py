# V_@_
import arcade

from src.hitbox import Hitbox


"""
Main bullet class
"""
class Bullet(arcade.Sprite):
    # Initialize attributes
    def __init__(self, image, scale, speed, damage):
        super().__init__(image, scale)
        self.speed = speed
        self.damage = damage
        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 0.7 * self.width / 2)

    # Set initial position of the bullet
    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y
        # Set position of hitbox
        self.hitbox.set_position(self.center_x, self.center_y)

    # Method for moving the bullet according to its speed
    def move(self, x, y):
        self.center_x += self.speed * x
        self.center_y += self.speed * y
        # Update position of hitbox
        self.hitbox.set_position(self.center_x, self.center_y)
