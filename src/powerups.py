# V_@_
import arcade

from src.hitbox import Hitbox


"""
PowerUp super class
"""
class PowerUp(arcade.Sprite):
    # Initialize attributes of class powerup
    def __init__(self, image, scale, speed):
        super().__init__(image, scale)
        self.speed = speed
        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 0.7 * self.width / 2)

    # Sets initial position of the powerup
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
Subclasses for the different power-ups
"""
class RegenPowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)


class SpeedPowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)


class RocketPowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)


class HealthPowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)


class DamagePowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)


class TriplePowerUp(PowerUp):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale, speed)
