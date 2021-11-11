from toyrobot.table import Table
from toyrobot.robot import Robot

class ControllerGUI():
    """Graphical user interface for the terminal"""

    def __init__(self, robot, table):
        """Defines robot and table information"""

        self.tableX = table.dimX
        self.tableY = table.dimY
        self.robotX = robot.currX
        self.robotY = robot.currY
        self.robotHead = robot.currHead

    def lookup_headSym(self):
        """Looks up associated symbol for given heading"""

        headSym = {
            'north' : '^',
            'east'  : '>',
            'south' : 'v',
            'west'  : '<',
        }[self.robotHead]

        return headSym

    def display(self, headSym):
        matrix = []

        for row in range(self.tableX):
            tempRow = []
            for col in range(self.tableY):
                tempRow.append('_')
            matrix.append(tempRow)

        matrix[self.robotX][self.robotY] = headSym
        
        for col in reversed(range(self.tableY)):
            for row in range(self.tableX):
                print(matrix[row][col], end = " ")
            print()