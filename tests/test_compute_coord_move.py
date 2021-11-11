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

class TestCheckCoord(unittest.TestCase):
    """Tests check_coord method"""

    def test_move_North(self):
        robot = Robot(2,2,'north')
        dX, dY = robot.check_coord()
        robot.compute_coord(table, dX, dY)
        assert robot.currX == 2
        assert robot.currY == 3

    def test_move_East(self):
        robot = Robot(2,2,'east')
        dX, dY = robot.check_coord()
        robot.compute_coord(table, dX, dY)
        assert robot.currX == 3
        assert robot.currY == 2

    def test_move_South(self):
        robot = Robot(2,2,'south')
        dX, dY = robot.check_coord()
        robot.compute_coord(table, dX, dY)
        assert robot.currX == 2
        assert robot.currY == 1

    def test_move_West(self):
        robot = Robot(2,2,'west')
        dX, dY = robot.check_coord()
        robot.compute_coord(table, dX, dY)
        assert robot.currX == 1
        assert robot.currY == 2

    def test_exceed_bound(self):
        robot = Robot(tDimX, tDimY,'north')
        dX, dY = robot.check_coord()
        robot.compute_coord(table, dX, dY)
        assert robot.currX == tDimX                         # X does not change
        assert robot.currY == tDimY                         # Y does not change

if __name__ == "__main__":
    unittest.main()