import os
from toyrobot.table import Table
from toyrobot.robot import Robot
from toyrobot.controller import Controller

def main():
    # Clears terminal
    os.system('cls')

    # Initialise variables
    table = Table(5, 5)
    robot = Robot(0, 0, None)
    controller = Controller()

    # Start command line program
    controller.parse_cmd(robot, table)

if __name__ == "__main__":
    main()