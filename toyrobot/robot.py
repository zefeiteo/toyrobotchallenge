from toyrobot.table import Table

class Robot():
    """Defines a robot"""

    def __init__(self, currX, currY, head):
        """Defines current position and heading"""

        self.currX = currX
        self.currY = currY
        self.head = head

    def __str__(self):
        return f"Robot is at ({self.currX},{self.currY}) and facing {self.head}."

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

class InvalidPosError(Exception):
    """Raises error if Table bounds exceeded"""
    pass