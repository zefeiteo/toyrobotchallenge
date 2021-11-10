class Robot():
    """Defines a robot"""

    def __init__(self, currX, currY, head):
        """Defines current position and heading"""

        self.currX = currX
        self.currY = currY
        self.head = head

    def __str__(self):
        return f"Robot is at ({self.currX},{self.currY}) and facing {self.head}."