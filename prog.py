import os
from toyrobot.table import Table
from toyrobot.robot import Robot

def main():
    # Clears terminal
    os.system('cls')

    # Initialise variables
    table = Table(5,5)
    robot = Robot(0,1,'north')

    # Test cases
    robot.compute_coord(table, 1, 3)
    print(robot)
    
if __name__ == "__main__":
    main()