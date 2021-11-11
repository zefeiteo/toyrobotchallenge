import sys
import argparse

from toyrobot.table import Table
from toyrobot.robot import Robot

class Controller():
    """Command line program that controls the robot"""

    def __init__(self):
        """Defines parser"""

        self.parser = argparse.ArgumentParser(description="Controls a robot")

    def parse_cmd(self, robot, table):
        """Parses commands fed to the controller"""
        
        # Positional arguments
        self.parser.add_argument("-p", "--place", nargs = 3,
                            help="Sets robot home position & heading")
        self.parser.add_argument("-m", "--move", action="store_true",
                            help="Moves robot 1 step forward")
        self.parser.add_argument("-l", "--left", action="store_true",
                            help="Rotate robot -90deg")
        self.parser.add_argument("-r", "--right", action="store_true",
                            help="Rotate robot +90deg")
        self.parser.add_argument("--report", action="store_true",
                            help="Report robot position")
        self.parser.add_argument("-x", "--exit", action="store_true",
                            help="Exits program")
    
        # Initialises robot with place command
        args, _ = self.parser.parse_known_args(input("\nPlace me somewhere: ").split())
        robot.currX = int(args.place[0])
        robot.currY = int(args.place[1])
        robot.currHead = args.place[2]

        # Receives commands
        while True:
            args, _ = self.parser.parse_known_args(input("\nYour wish is my command: ").split())
            
            if args.move:
                dX, dY = robot.compute_coord_move()
                robot.compute_coord(table, dX, dY)
            elif args.left:
                robot.compute_head('left')
            elif args.right:
                robot.compute_head('right')
            elif args.report:
                print(robot)
            elif args.exit:
                print("\nExiting the program.\n")
                sys.exit(0)