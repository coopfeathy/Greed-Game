import os
import turtle
import random

from actor import Actor
from artifact import Artifact
from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed: Gems & Stones"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/messages.txt"
WHITE = Color(255, 255, 255)
GREEN = Color(255, 233, 0)
BLUE = Color(0, 191, 191)
ORANGE = Color(255, 98, 15)
DEFAULT_ARTIFACTS = 20

window = turtle.Screen()
window.title("Greed: Gems and Stones")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(2)


def main():
    window.update()
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(GREEN)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the gem
    
    gems = []
    for n in range(DEFAULT_ARTIFACTS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # color = Color(BLUE)
        
        artifact = Artifact()
        artifact.set_text("*")
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(BLUE)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
        gem = turtle.Turtle()
        gem.speed = random.randint(2, 6)
        gems.append(artifact)
        while True:
            for artifact in gems:
                y = artifact.get_position()
                y -= MAX_Y
                artifact.set_position(y)

    
    # create the stone

    for n in range(DEFAULT_ARTIFACTS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # color = Color(ORANGE)
        
        artifact = Artifact()
        artifact.set_text("O")
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(ORANGE)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)

    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

    # for n in range(DEFAULT_ARTIFACTS):
    #     text = chr(random.randint(33, 126))
    #     message = messages[n]

    #     x = random.randint(1, COLS - 1)
    #     y = random.randint(1, ROWS - 1)
    #     position = Point(x, y)
    #     position = position.scale(CELL_SIZE)

    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = Color(r, g, b)
        
    #     artifact = Artifact()
    #     artifact.set_text(text)
    #     artifact.set_font_size(FONT_SIZE)
    #     artifact.set_color(color)
    #     artifact.set_position(position)
    #     artifact.set_message(message)
    #     cast.add_actor("artifacts", artifact)

    # for _ in gems:
    

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
