# V_@_
import random
import arcade
import weapons
import powerups

from src.asteroids import BigAsteroid, SmallAsteroid, SplitAsteroid
from src.spaceship import SpaceShip

"""
Background engine stuff
"""
# Constants for screen width and height
WIDTH = 1920
HEIGHT = 1080

# Enables timings for FPS counter
arcade.enable_timings()

"""
Function to load high-score
"""
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


"""
Class that manages the menu screen
"""
class MenuView(arcade.View):
    # Initialize attributes of menu view
    def __init__(self):
        super().__init__()
        self.high_score = load_high_score()
        self.background = arcade.load_texture("bg_menu.png", width=1920, height=1080)
        self.music = arcade.load_sound("msc_menu.mp3")
        self.media_player = self.music.play()

    def on_show_view(self):
        self.media_player.play()

    # Render the menu screen
    def on_draw(self):
        # Render background image and start text
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            WIDTH, HEIGHT, self.background)
        arcade.draw_text("Meteors", WIDTH / 2, HEIGHT - 100,
                         arcade.color.WHITE, font_size=60, bold=True, anchor_x="center", font_name="Kenney Rocket")
        arcade.draw_text("Press Space to Start", WIDTH / 2, 60,
                         arcade.color.WHITE, font_size=25, anchor_x="center", font_name="Kenney Rocket")
        # Render high score
        high_score_text = f"High Score: {self.high_score}"
        arcade.draw_text(high_score_text, WIDTH / 2, HEIGHT - 160,
                         arcade.color.WHITE, 25, anchor_x="center", font_name="Kenney Rocket")

    # Check for menu key presses
    def on_key_press(self, key, modifiers):
        # Create the game view and start the game with Spacebar
        if key == arcade.key.SPACE:
            self.media_player.pause()
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        # Close the game with Escape
        if key == arcade.key.ESCAPE:
            arcade.close_window()


"""
Class that manages the pause screen
"""
class PauseView(arcade.View):
    # Initialize attributes of pause screen
    def __init__(self, game_view):
        super().__init__()
        # Passing the game view so you can return to it
        self.game_view = game_view
        self.high_score = load_high_score()

    def on_show_view(self):
        self.game_view.media_player.pause()

    # Render the pause screen
    def on_draw(self):
        # Render the pause text
        arcade.draw_text("PAUSED", WIDTH / 2, HEIGHT - 80,
                         arcade.color.WHITE, font_size=50, anchor_x="center", font_name="Kenney Rocket")

        # Render tip to return or reset
        arcade.draw_text("Press Esc. to return", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center", font_name="Kenney Rocket")
        arcade.draw_text("Press Enter to reset", WIDTH / 2, HEIGHT / 2 - 30,
                         arcade.color.WHITE, font_size=20, anchor_x="center", font_name="Kenney Rocket")
        # Render current score and high score
        high_score_text = f"High Score: {self.high_score}"
        score_text = f"Score: {self.game_view.score}"
        arcade.draw_text(score_text, WIDTH / 2, HEIGHT / 2 - 150,
                         arcade.color.WHITE, 25, anchor_x="center", font_name="Kenney Rocket")
        arcade.draw_text(high_score_text, WIDTH / 2, HEIGHT / 2 - 110,
                         arcade.color.WHITE, 25, anchor_x="center", font_name="Kenney Rocket")

    # Check for key presses in pause menu
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:   # Resume the game with Escape
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # Reset the game with Enter
            menu = MenuView()
            self.window.show_view(menu)


"""
Class that manages the game over screen
"""
class GameOverView(arcade.View):
    # Initialize attributes of game over screen
    def __init__(self):
        super().__init__()
        self.high_score = load_high_score()
        self.background = arcade.load_texture("bg_gameover.png", width=1920, height=1080)
        self.music = arcade.load_sound("msc_gameover.mp3")
        self.media_player = self.music.play()

    def on_show_view(self):
        self.media_player.play()

    # Render the game over view
    def on_draw(self):
        # Render game over text
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        arcade.draw_text("Game Over", WIDTH / 2, HEIGHT - 80,
                         arcade.color.WHITE, 54, anchor_x="center", font_name="Kenney Rocket")
        arcade.draw_text("Press Enter to restart", WIDTH / 2, 80,
                         arcade.color.WHITE, 24, anchor_x="center", font_name="Kenney Rocket")
        arcade.draw_text("Press Escape to exit", WIDTH / 2, 40,
                         arcade.color.WHITE, 24, anchor_x="center", font_name="Kenney Rocket")
        # Render current score and high score
        high_score_text = f"High Score: {self.high_score}"
        arcade.draw_text(high_score_text, WIDTH / 2, HEIGHT - 120,
                         arcade.color.WHITE, 25, anchor_x="center", font_name="Kenney Rocket")

    # Check for key presses in game over screen
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:   # Close the game with Escape
            arcade.close_window()
        elif key == arcade.key.ENTER:  # Restart the game with Enter
            self.media_player.pause()
            menu = MenuView()
            self.window.show_view(menu)


"""
Class that manages the main game screen
"""
class GameView(arcade.View):
    # Initialize attributes of game view
    def __init__(self):
        super().__init__()
        # Main attributes
        self.spaceship = None
        self.asteroids = []
        self.bullets = []
        self.powerups = []
        self.split_asteroids = []
        self.colliding_asteroids = []
        # Background attributes
        self.shot_timer = 0
        self.shots_fired = 0
        self.min_asteroids = 3
        self.score = 0
        self.high_score = load_high_score()
        self.gameover = False
        self.background = arcade.load_texture("bg_game.png", width=1920, height=1080)
        self.music = arcade.load_sound("msc_game.mp3")
        self.media_player = self.music.play()
        self.laser_sound = arcade.load_sound("snd_laser.wav")
        self.player_hit_sound = arcade.load_sound("snd_playerhit.wav")
        self.explosion_sound = arcade.load_sound("snd_explosion.wav")
        self.powerup_sound = arcade.load_sound("snd_powerup.wav")
        # Dictionary for key states
        self.key_states = {}
        # Debug mode
        self.debug_hitbox = False
        self.debug_stats = False

    def on_show_view(self):
        self.media_player.play()

    # Method for overwriting high score
    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    # Called once before the game starts
    def setup(self):
        # Initialize the spaceship
        self.spaceship = SpaceShip("spr_spaceship.png", 1.5, 500, 5)
        self.spaceship.set_position(WIDTH / 2, self.spaceship.height - 20)
        self.spaceship.weapon = weapons.WEAPON_DEFAULT
        # Reset the background attributes
        self.score = 0
        self.asteroids = []
        self.bullets = []
        self.powerups = []
        self.split_asteroids = []
        self.shot_timer = 0
        self.shots_fired = 0

    # Called every frame of the game
    def update(self, delta_time: float):
        # Move spaceship if LEFT or RIGHT is pressed
        if self.is_key_pressed(arcade.key.RIGHT):
            self.spaceship.move(delta_time, 0)
        elif self.is_key_pressed(arcade.key.LEFT):
            self.spaceship.move(-delta_time, 0)

        # Move Asteroids
        for asteroid in self.asteroids:
            asteroid.move(0, -delta_time)

        # Move split asteroids
        for asteroid in self.split_asteroids:
            if asteroid.move_dir == 2:
                asteroid.move(delta_time, -delta_time)
            else:
                asteroid.move(-delta_time, -delta_time)

        for powerup in self.powerups:
            powerup.move(0, -delta_time)

        # Move bullets
        for bullet in self.bullets:
            bullet.move(0, delta_time)

        # Handle Collisions
        self.handle_collisions()

        # Remove Asteroids that are out of screen
        lose_asteroids = [asteroid for asteroid in self.asteroids if asteroid.center_y < 0]
        lose_split_asteroids = [asteroid for asteroid in self.split_asteroids if asteroid.center_y < 0]
        oob_asteroids = [asteroid for asteroid in self.split_asteroids
                         if asteroid.center_x < 5 or asteroid.center_x > WIDTH - 5]
        if len(lose_asteroids) != 0 or len(lose_split_asteroids) != 0:
            self.media_player.pause()
            game_over = GameOverView()
            self.window.show_view(game_over)
        self.split_asteroids = [asteroid for asteroid in self.split_asteroids if asteroid not in oob_asteroids]

        # Remove powerups that are out of screen
        oob_powerups = [powerup for powerup in self.powerups if powerup.center_y < 0]
        self.powerups = [powerup for powerup in self.powerups if powerup not in oob_powerups]

        # Spawn new asteroids and a powerup if there is less than or 1 asteroid
        if len(self.asteroids) <= 1:
            self.min_asteroids += 1
            for i in range(self.min_asteroids):
                self.spawn_asteroid()
            self.spawn_powerup()

        # Fire rate check for player
        if self.shots_fired >= self.spaceship.weapon.magazine_size:
            self.shot_timer += delta_time
            if self.shot_timer >= self.spaceship.weapon.reload_time:
                self.shots_fired = 0
                self.shot_timer = 0

        # Overwrite highscore if score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        # Keep spaceship on screen
        if self.spaceship.left + 30 < 0:
            self.spaceship.left = -30
        if self.spaceship.right - 30 > WIDTH:
            self.spaceship.right = WIDTH + 30

        # Player hp check
        if self.spaceship.hp_current <= 0:
            self.media_player.pause()
            game_over = GameOverView()
            self.window.show_view(game_over)

    # Render the game view
    def on_draw(self):
        # Render spaceship, asteroids and bullets
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, WIDTH, HEIGHT, self.background)
        self.spaceship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        for asteroid in self.split_asteroids:
            asteroid.draw()
        for powerup in self.powerups:
            powerup.draw()

        # Render the current score on screen
        score_text = self.score
        arcade.draw_text("Score:", WIDTH - 10, HEIGHT - 40,
                         arcade.color.WHITE, 20, font_name="Kenney Rocket", anchor_x="right")
        arcade.draw_text(score_text, WIDTH - 10, HEIGHT - 70,
                         arcade.color.WHITE, 20, font_name="Kenney Rocket", anchor_x="right")

        # Render player stats
        player_hp_text = f"HP: {self.spaceship.hp_current}"
        arcade.draw_text(player_hp_text, 10, HEIGHT - 40,
                         arcade.color.WHITE, 20, font_name="Kenney Rocket")
        player_speed_text = f"Speed: x{self.spaceship.speed_multiplier:.2f}"
        arcade.draw_text(player_speed_text, 10, HEIGHT - 70,
                         arcade.color.WHITE, 20, font_name="Kenney Rocket")
        player_damage_text = f"Damage: x{self.spaceship.damage_multiplier:.2f}"
        arcade.draw_text(player_damage_text, 10, HEIGHT - 100,
                         arcade.color.WHITE, 20, font_name="Kenney Rocket")

        # Render hitboxes if hitbox debug mode is on
        if self.debug_hitbox:
            self.spaceship.hitbox.draw()

            for a in self.asteroids:
                a.hitbox.draw()

            for b in self.bullets:
                b.hitbox.draw()

            for a in self.split_asteroids:
                a.hitbox.draw()

            for p in self.powerups:
                p.hitbox.draw()

        # Render stats if stats debug mode is on
        if self.debug_stats:
            # FPS counter for debug mode
            text = f"FPS: {arcade.get_fps(60):5.1f}"
            arcade.draw_text(text, 10, WIDTH, arcade.color.WHITE, 22)
            # Debug for shooting
            player_shots_fired_text = f"Shots fired: {self.shots_fired}"
            arcade.draw_text(player_shots_fired_text, 10, HEIGHT - 125,
                             arcade.color.WHITE, 15, font_name="Kenney Rocket")
            player_shots_timer_text = f"Reload Timer: {self.shot_timer:.2f}"
            arcade.draw_text(player_shots_timer_text, 10, HEIGHT - 140,
                             arcade.color.WHITE, 15, font_name="Kenney Rocket")

    # Check for key presses
    def on_key_press(self, key, modifiers):
        self.key_states[key] = True
        # Check for pause
        if key == arcade.key.ESCAPE:
            pause_view = PauseView(self)
            self.window.show_view(pause_view)

        # Check for shoot
        if (key == arcade.key.LCTRL and self.shots_fired < self.spaceship.weapon.magazine_size
                or key == arcade.key.RCTRL and self.shots_fired < self.spaceship.weapon.magazine_size):
            arcade.play_sound(self.laser_sound)
            if self.spaceship.weapon == weapons.WEAPON_TRIPLE:
                self.shots_fired += 1
                self.bullets.append(self.spaceship.shoot_center())
                self.bullets.append(self.spaceship.shoot_left())
                self.bullets.append(self.spaceship.shoot_right())
            else:
                self.shots_fired += 1
                self.bullets.append(self.spaceship.shoot())

    # Check key release
    def on_key_release(self, key, modifiers):
        self.key_states[key] = False

    # Check for held down key
    def is_key_pressed(self, key):
        return self.key_states.get(key, False)

    # Method for spawning asteroids
    def spawn_asteroid(self):
        # Set random position and choose size of asteroid
        x = random.randint(5, WIDTH - 5)
        y = random.randint(HEIGHT, HEIGHT + 350)
        t = random.randint(1, 3)

        if t < 3:
            # Spawn big asteroid
            hp = random.randint(80, 170)
            speed = random.randint(20, 90)
            asteroid = BigAsteroid("spr_asteroid_big.png", 2, speed, 1, hp)
            asteroid.set_position(x, y)
            self.asteroids.append(asteroid)
        else:
            # Spawn small asteroid
            hp = random.randint(50, 80)
            speed = random.randint(60, 130)
            asteroid = SmallAsteroid("spr_asteroid_small.png", 2, speed, 1, hp)
            asteroid.set_position(x, y)
            self.asteroids.append(asteroid)

    # Method for spawning the split asteroids
    def spawn_split_asteroid(self, asteroid):
        # Set position to position of asteroid from which it split and give it a random move direction
        x = asteroid.center_x
        y = asteroid.center_y
        hp = random.randint(30, 60)
        speed = random.randint(30, 60)
        move_dir = random.randint(1, 2)
        asteroid = SplitAsteroid("spr_asteroid_small.png", 2, speed, 1, hp, move_dir)
        asteroid.set_position(x, y)
        self.split_asteroids.append(asteroid)


    def spawn_powerup(self):
        # Set random position and choose the powerup
        x = random.randint(10, WIDTH - 10)
        y = random.randint(HEIGHT, HEIGHT + 350)
        speed = random.randint(40, 180)
        p = random.randint(1, 6)

        if p == 1:
            powerup = powerups.RegenPowerUp(":resources:onscreen_controls/shaded_dark/wrench.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)
        elif p == 2:
            powerup = powerups.HealthPowerUp(":resources:images/items/gemGreen.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)
        elif p == 3:
            powerup = powerups.SpeedPowerUp(":resources:onscreen_controls/shaded_dark/play.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)
        elif p == 4:
            powerup = powerups.DamagePowerUp(":resources:images/items/gemRed.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)
        elif p == 5:
            powerup = powerups.RocketPowerUp(":resources:images/topdown_tanks/tankRed_barrel1_outline.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)
        elif p == 6:
            powerup = powerups.TriplePowerUp(":resources:images/topdown_tanks/tankGreen_barrel1_outline.png", 1, speed)
            powerup.set_position(x, y)
            self.powerups.append(powerup)

    # Method for checking collisions
    def handle_collisions(self):
        # Lists for asteroids, bullets and powerups to be removed
        colliding_asteroids = []
        colliding_bullets = []
        colliding_powerups = []

        for asteroid in self.asteroids:
            for bullet in self.bullets:
                # Check for collision between asteroid and bullet
                if asteroid.hitbox.collides_with(bullet.hitbox):
                    # Check for asteroid hp
                    if asteroid.hp_current > 0:
                        asteroid.hp_current -= bullet.damage * self.spaceship.damage_multiplier
                        colliding_bullets.append(bullet)
                    # Remove bullet and check split chance
                    else:
                        split = random.randint(0, 100)
                        colliding_bullets.append(bullet)
                        # Check for big asteroid and split chance, remove bullet and spawn 2 small asteroids
                        if isinstance(asteroid, BigAsteroid) and split < asteroid.split_percent:
                            self.spawn_split_asteroid(asteroid)
                            self.spawn_split_asteroid(asteroid)
                            colliding_asteroids.append(asteroid)
                            arcade.play_sound(self.explosion_sound)
                            self.score += 1
                        # Remove asteroid if small asteroid
                        else:
                            colliding_asteroids.append(asteroid)
                            arcade.play_sound(self.explosion_sound)
                            self.score += 1
            # Check for collision between asteroid and spaceship
            if asteroid.hitbox.collides_with(self.spaceship.hitbox):
                # Check for spaceship hp
                if self.spaceship.hp_current > 0:
                    self.spaceship.hp_current -= asteroid.damage
                    arcade.play_sound(self.player_hit_sound)
                    colliding_asteroids.append(asteroid)
                # Move to game over if spaceship hp < 0
                else:
                    self.media_player.pause()
                    game_over = GameOverView()
                    self.window.show_view(game_over)

        # Extra check for split asteroid collisions because it didn't work otherwise
        for asteroid in self.split_asteroids:
            for bullet in self.bullets:
                # Check for collision between split asteroid and bullet
                if asteroid.hitbox.collides_with(bullet.hitbox):
                    # Reduce split asteroid hp and remove bullet
                    if asteroid.hp_current > 0:
                        asteroid.hp_current -= bullet.damage * self.spaceship.damage_multiplier
                        colliding_bullets.append(bullet)
                    # Remove split asteroid and bullet
                    else:
                        colliding_asteroids.append(asteroid)
                        arcade.play_sound(self.explosion_sound)
                        colliding_bullets.append(bullet)
                        self.score += 1
                # Check for collision between split asteroid and spaceship
            if asteroid.hitbox.collides_with(self.spaceship.hitbox):
                # Reduce spaceship hp and remove split asteroid
                if self.spaceship.hp_current >= 0:
                    self.spaceship.hp_current -= asteroid.damage
                    arcade.play_sound(self.player_hit_sound)
                    colliding_asteroids.append(asteroid)
                # Move to game over if spaceship hp < 0
                else:
                    self.media_player.pause()
                    game_over = GameOverView()
                    self.window.show_view(game_over)

        # Check for Collision between powerup and player
        for powerup in self.powerups:
            if powerup.hitbox.collides_with(self.spaceship.hitbox):
                arcade.play_sound(self.powerup_sound)
                # Health regeneration power up
                if isinstance(powerup, powerups.RegenPowerUp):
                    self.spaceship.hp_current = self.spaceship.hp_max
                # Max health power up
                elif isinstance(powerup, powerups.HealthPowerUp):
                    self.spaceship.hp_max += 1
                    self.spaceship.hp_current = self.spaceship.hp_max
                # Speed multiplier power up
                elif isinstance(powerup, powerups.SpeedPowerUp):
                    self.spaceship.speed_multiplier += 0.2
                # Damage multiplier power up
                elif isinstance(powerup, powerups.DamagePowerUp):
                    self.spaceship.damage_multiplier += 0.2
                # Rocket launcher weapon power up
                elif isinstance(powerup, powerups.RocketPowerUp):
                    self.spaceship.weapon = weapons.WEAPON_ROCKET
                    self.shots_fired = 0
                elif isinstance(powerup, powerups.TriplePowerUp):
                    self.spaceship.weapon = weapons.WEAPON_TRIPLE
                    self.shots_fired = 0
                # Remove the collected power up
                colliding_powerups.append(powerup)

        # Reset lists of asteroids and bullets to remove destroyed asteroids
        self.asteroids = [asteroid for asteroid in self.asteroids if asteroid not in colliding_asteroids]
        self.split_asteroids = [asteroid for asteroid in self.split_asteroids if asteroid not in colliding_asteroids]
        self.bullets = [bullet for bullet in self.bullets if bullet not in colliding_bullets]
        self.powerups = [powerup for powerup in self.powerups if powerup not in colliding_powerups]
