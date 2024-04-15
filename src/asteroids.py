# V_@_
import arcade
import random

from src.hitbox import Hitbox


"""
Asteroid super class
"""
class Asteroid(arcade.Sprite):
    def __init__(self, image, scale, speed, damage, hp):
        # Check that the game isn't trying to spawn instance of asteroid super class
        if type(self) is Asteroid:
            raise Exception("Asteroid is an abstract class and cannot be instantiated directly.")
        super().__init__(image, scale)
        # Initialize attributes of class asteroid
        self.speed = speed
        self.damage = damage
        self.hp_max = hp
        self.hp_current = hp
        self.split_percent = 70
        self.angle = random.randint(0, 360)
        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 1.1 * self.width / 2)

    # Sets initial position of the asteroid
    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y
        # Set position of the hitbox
        self.hitbox.set_position(self.center_x, self.center_y)

    # Method for moving asteroid according to its speed
    def move(self, x, y):
        self.center_x += self.speed * x
        self.center_y += self.speed * y
        # Update position of hitbox
        self.hitbox.set_position(self.center_x, self.center_y)


"""
Big Asteroid subclass
"""
class BigAsteroid(Asteroid):
    def __init__(self, image, scale, speed, damage, hp):
        super().__init__(image, scale, speed, damage, hp)


"""
Small Asteroid subclass
"""
class SmallAsteroid(Asteroid):
    def __init__(self, image, scale, speed, damage, hp):
        super().__init__(image, scale, speed, damage, hp)


"""
Split Asteroid subclass
"""
class SplitAsteroid(SmallAsteroid):
    def __init__(self, image, scale, speed, damage, hp, move_dir):
        super().__init__(image, scale, speed, damage, hp)
        self.move_dir = move_dir
