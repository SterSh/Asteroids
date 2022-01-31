"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import random
import math

from abc import ABC
from abc import abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Point():
    """
    this class initiates a location on x and y coordinates
    """
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
class Velocity():
    """
    A class to set a random velocity of the ball
    """
    def __init__(self):
        self.dx = 0
        self.dy = 0

class FlyingObject(ABC):
    """
    Base class for flying objects (bullets, rocks, ship) with applicable class methods
    """
    def __init__(self, img):
        #initialize flying object
        self.center = Point()
        self.velocity = Velocity()
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = SHIP_RADIUS
        self.angle = 0
        self.speed = 0
        self.direction = 0
        self.alive = True

    def draw(self):
        """
        Flying Object draw method.  
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)

    def advance(self):
        """
        Method to advance flying objects by the dx and dy velocity
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def is_alive(self):
        """
        Returns whether 
        """
        return self.alive

class Asteroid(FlyingObject):
    """
    Base asteroid class, which the asteroids are based off of.  
    *May not be needed 
    """
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0

class SmallRock(Asteroid):
    """
    Small Asteroid class, defines the properties of a small sized asteroid
    *not fully built out, inherates from asteroid class
    """
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_small1.png")
        self.radius = 0.0

class MediumRock(Asteroid):
    """
    Medium Asteroid class, defines the properties of a medium sized asteroid
    *not fully built out, inherates from asteroid class
    """
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_med1.png")
        self.radius = 0.0

class LargeRock(Asteroid):
    """
    Large Asteroid class, defines the properties of a Large sized asteroid
    *not fully built out, inherates from asteroid class
    """
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_big1.png")
        self.radius = 0.0
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

class Bullet(FlyingObject):
    """
    Bullet class which inherits from the FlyingObject class
    *not fully built out 
    """
    def __init__(self):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
    #fire stub method
    def fire(self):
        pass

class Ship(FlyingObject):
    """
    Ship class, defines the player ship and needed methods
    *not fully built out
    """
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.angle = 1
        self.center.x  = (SCREEN_WIDTH/2)
        self.center.y = (SCREEN_HEIGHT/2)
        self.radius = SHIP_RADIUS
    
    def left(self):
        pass

    def right(self):
        pass

    def thrust(self):
        pass

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        self.asteroids = []
        for i in range(INITIAL_ROCK_COUNT):
            bigAst = LargeRock()
            self.asteroids.append(bigAst)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()

        self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time

        for asteroid in self.asteroids:
            asteroid.advance()

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()