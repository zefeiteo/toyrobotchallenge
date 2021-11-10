class Table():
    """Defines a finite surface"""

    def __init__(self, dimX, dimY):
        """Defines 2D finite surface"""

        self.dimX = dimX
        self.dimY = dimY

    def __str__(self):
        return f"Table dimensions are {self.dimX}x{self.dimY}."