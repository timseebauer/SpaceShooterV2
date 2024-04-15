# V_@_
import arcade
import math


"""
Main hitbox class
"""
class Hitbox:
    # Initialize attributes
    def __init__(self, x, y, r):
        self.center_x = x
        self.center_y = y
        self.radius = r

    # Set hitbox position
    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

    # Check for intersection with other hitboxes
    def collides_with(self, other):
        distance = math.sqrt((self.center_x - other.center_x)**2 + (self.center_y - other.center_y)**2)
        if distance <= self.radius + other.radius:
            return True
        else:
            return False

    # Draw function for debug mode
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.BLUE)
