import unittest
import os
import sys

# Import from 'toyrobot' subfolder
sys.path.insert(0,'.')
from toyrobot.table import Table
from toyrobot.robot import Robot, InvalidPosError

# Clears terminal
os.system('cls')

# Variable table dimensions
tDimX = 5
tDimY = 5

# Define table dimensions
table = Table(tDimX, tDimY)

class TestComputeHead(unittest.TestCase):
    """Tests compute_head method"""

    def test_left(self):
        robot = Robot(0,0,'north')
        head = robot.compute_head('left')
        assert robot.currHead == 'west'

    def test_right(self):
        robot = Robot(0,0,'north')
        head = robot.compute_head('right')
        assert robot.currHead == 'east'

    def test_exceed_bound(self):
        robot = Robot(0,0,'north')
        coord = robot.compute_coord(table, tDimX+1, tDimY+1)
        head = robot.compute_head('left')
        assert robot.currX == 0                         # X does not change
        assert robot.currY == 0                         # Y does not change
        self.assertRaises(InvalidPosError)
        assert robot.currHead == 'west'                 # Heading is changed     

if __name__ == "__main__":
    unittest.main()