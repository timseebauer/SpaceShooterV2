# V_@_
import arcade
from src.views import WIDTH, HEIGHT, MenuView


"""
Main method that starts the game
"""
def main():
    window = arcade.Window(WIDTH, HEIGHT, "Meteors! V_@_", fullscreen=False)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


# Code used to have the IDE always run main.py
if __name__ == "__main__":
    main()
