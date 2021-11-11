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
    rotate = ['left', 'right']
    for i, headings in enumerate(rotate):
        robot.compute_head(rotate[i])
        print(robot)
    
if __name__ == "__main__":
    main()