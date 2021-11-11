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

class TestComputeCoord(unittest.TestCase):
    """Tests compute_coord method"""

    def test_within_Xbound(self):
        robot = Robot(0,0,'none')
        coord = robot.compute_coord(table, 1, 0)
        assert robot.currX == 1
        assert robot.currY == 0

    def test_within_Ybound(self):
        robot = Robot(0,0,'none')
        coord = robot.compute_coord(table, 0, 1)
        assert robot.currX == 0
        assert robot.currY == 1

    def test_exceed_Xbound(self):
        robot = Robot(0,0,'none')
        coord = robot.compute_coord(table, tDimX+1, 0)
        assert robot.currX == 0                         # X does not change
        assert robot.currY == 0
        self.assertRaises(InvalidPosError)

    def test_exceed_Ybound(self):
        robot = Robot(0,0,'none')
        coord = robot.compute_coord(table, 0, tDimY+1)
        assert robot.currX == 0
        assert robot.currY == 0                         # Y does not change
        self.assertRaises(InvalidPosError)

if __name__ == "__main__":
    unittest.main()