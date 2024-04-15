# V_@_
import arcade
import weapons

from hitbox import Hitbox


"""
Main spaceship class
"""
class SpaceShip(arcade.Sprite):
    # Initialize attributes
    def __init__(self, image, scale, speed, hp_max):
        super().__init__(image, scale)
        self.speed = speed
        self.hp_max = hp_max
        self.hp_current = hp_max
        self.weapon = weapons.WEAPON_DEFAULT
        self.damage_multiplier = 1
        self.speed_multiplier = 1

        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 0.7 * self.width / 2)

    # set Initial position of spaceship
    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y
        # Set position of the hitbox
        self.hitbox.set_position(self.center_x, self.center_y)

    # Move the spaceship according to its speed and multiplier
    def move(self, x, y):
        self.center_x += self.speed * x * self.speed_multiplier
        self.center_y += self.speed * y * self.speed_multiplier
        # Update position of hitbox
        self.hitbox.set_position(self.center_x, self.center_y)

    # Method for shooting current weapon
    def shoot(self):
        return self.weapon.shoot(self.center_x, self.center_y)

    # Method for center bullet of triple shot weapon
    def shoot_center(self):
        return self.weapon.shoot(self.center_x, self.center_y + 30)

    # Method for left bullet of triple shot weapon
    def shoot_left(self):
        return self.weapon.shoot(self.center_x - 30, self.center_y)

    # Method for right bullet of triple shot weapon
    def shoot_right(self):
        return self.weapon.shoot(self.center_x + 30, self.center_y)
