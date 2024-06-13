# V_@_
from bullet import Bullet
from hitbox import Hitbox

"""
Weapon super class
"""
class Weapon:
    # Initialize attributes
    def __init__(self, reload_time, magazine_size):
        self.reload_time = reload_time
        self.magazine_size = magazine_size

    # Abstract method to be overwritten by subclasses
    def shoot(self, x, y):
        pass


"""
Subclass for the default weapon
"""
class DefaultWeapon(Weapon):
    # Initialize attributes
    def __init__(self):
        super().__init__(1, 20)

    # Method for shooting this specific weapon
    def shoot(self, x, y):
        bullet = Bullet("spr_bullet_default.png", 1, 400, 50)
        bullet.center_x = x
        bullet.center_y = y + 10
        return bullet


"""
Subclass for the rocket launcher weapon
"""
class RocketWeapon(Weapon):
    # Initialize attributes
    def __init__(self):
        super().__init__(2, 6)

    # Method for shooting this specific weapon
    def shoot(self, x, y):
        bullet = Bullet("spr_bullet_missile.png", 1.5, 300, 160)
        bullet.center_x = x
        bullet.center_y = y + 10
        bullet.hitbox = Hitbox(bullet.center_x, bullet.center_y, 3.5 * bullet.width / 2)
        return bullet


"""
Subclass for the triple shot weapon
"""
class TripleWeapon(Weapon):
    # Initialize attributes
    def __init__(self):
        super().__init__(1.5, 10)

    # Method for shooting this specific weapon
    def shoot(self, x, y):
        bullet = Bullet("spr_bullet_big.png", 1, 400, 35)
        bullet.center_x = x
        bullet.center_y = y + 10
        bullet.hitbox = Hitbox(bullet.center_x, bullet.center_y, 1 * bullet.width / 2)
        return bullet


"""
Constants for each weapon type to be accessed later
"""
WEAPON_DEFAULT = DefaultWeapon()
WEAPON_ROCKET = RocketWeapon()
WEAPON_TRIPLE = TripleWeapon()
