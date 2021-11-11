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
        return f"{self.currX},{self.currY},{self.currHead.upper()}"

    def compute_coord(self, table, dX, dY):
        """Computes change in coordinates"""

        # Increments robot position
        propX = self.currX + dX
        propY = self.currY + dY

        # Prevents robot from exceeding Table dimensions
        if propX >= 0 and propX <= table.dimX-1:
            if propY >= 0 and propY <= table.dimY-1:
                self.currX = propX
                self.currY = propY
            else:
                print("Table bounds exceeded in y-direction, please try again.\n")
                return InvalidPosError
        else:
            print("Table bounds exceeded in x-direction, please try again.\n")
            return InvalidPosError

    def check_coord(self):
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

    def check_head(self, userHead):
        """Checks if user-defined heading is valid"""

        # Checks heading against enumerated list
        for index, head in enumerate(self.headStr):
            if head == userHead:
                self.currHead = userHead
                break
        else:
            print("Invalid heading entered, please try again.\n")
            return InvalidHeadError

class InvalidPosError(Exception):
    """Raises error if Table bounds exceeded"""

    pass

class InvalidHeadError(Exception):
    """Raises error if heading is invalid"""

    pass