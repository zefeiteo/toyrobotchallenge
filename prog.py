import os
from toyrobot.table import Table
from toyrobot.robot import Robot

def main():
    # Clears terminal
    os.system('cls')

    # Initialise variables
    table = Table(5,5)
    
    # Test cases
    headings = ['north', 'east', 'south', 'west']
    for i, _ in enumerate(headings):
        robot = Robot(2,2,headings[i])
        dX, dY = robot.compute_coord_move()
        robot.compute_coord(table, dX, dY)
        print(robot)
    
if __name__ == "__main__":
    main()