from toyrobot.table import Table

class Robot():
    """Defines a robot"""

    # Definition of headings in a clockwise motion
    headStr = ['north', 'east', 'south', 'west']

    def __init__(self, currX, currY, currHead):
        """Defines current position and heading"""

        self.currX = currX
        self.currY = currY
        self.currHead = currHead

    def __str__(self):
        return f"Robot is at ({self.currX},{self.currY}) and facing {self.currHead}."

    def compute_coord(self, table, dX, dY):
        """Computes change in coordinates"""
        
        # Increments robot position
        self.propX = self.currX + dX
        self.propY = self.currY + dY

        # Prevents robot from exceeding Table dimensions
        if self.propX >= 0 and self.propX <= table.dimX-1:
            if self.propY >= 0 and self.propY <= table.dimY-1:
                self.currX = self.propX
                self.currY = self.propY
            else:
                InvalidPosError
        else:
            InvalidPosError

    def compute_coord_move(self):
        """Defines change in coordinates for given heading"""
        dX = {                      # Sine function can be used instead
            'north' : 0,
            'east'  : 1,
            'south' : 0,
            'west'  : -1,
        }[self.currHead]

        dY = {                      # Cosine function can be used instead
            'north' : 1,
            'east'  : 0,
            'south' : -1,
            'west'  : 0,
        }[self.currHead]
        
        return dX, dY

    def compute_head(self, dHead):
        """Computes change in heading"""

        # Matches current heading to its index in an enumerated list
        for index, head in enumerate(self.headStr):
            if head == self.currHead:
                currHeadIndex = index
                break
        
        # Updates index according to change in heading
        if dHead == 'left':
            listIndex = (currHeadIndex-1)%len(self.headStr)
        elif dHead == 'right':
            listIndex = (currHeadIndex+1)%len(self.headStr)

        # Applies heading
        self.currHead = self.headStr[listIndex]

class InvalidPosError(Exception):
    """Raises error if Table bounds exceeded"""

    pass