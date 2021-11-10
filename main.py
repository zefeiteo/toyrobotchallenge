import os
from toyrobot.table import Table
from toyrobot.robot import Robot

def main():
    # Clears terminal
    os.system('cls')

    # Test cases
    test_table = Table(5,5)
    print(test_table)

    test_robot = Robot(0,1,'north')
    print(test_robot)

if __name__ == "__main__":
    main()