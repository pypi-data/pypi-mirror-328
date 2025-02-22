
class Tap:
    """
    Represents a tap detected on the smartphone screen.
    
    Attributes:
        - x (int): The x coordinate of the tap [0..100]. See: :ref:`screen`.
        - y (int): The y coordinate of the tap [0..100]. See: :ref:`screen`.
        - zone (string): Returns the area of the smartphone screen. Takes one of the following values: 'forehead', 'eye', 'right', 'left', 'mouth' or 'chin'.

        .. image:: _static/tap_areas.jpg
            :scale: 50 %
            :alt: Image showing the different possible tap areas on the screen, each one of them being a square or a rectangle. The upper part is the 'forehead'. Excluding the forehead, the right part is 'right' and the left part is 'left'. Excluding those parts, there are four zones remaining. From top to bottom, they are: the 'eye', which is the biggest of all zones, an undefined zone, the 'mouth' and the 'chin'.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.zone = self.coordsToZone(x,y)

    def coordsToZone (self, x, y):
        if (y == 0) and (x == 0):
            return None
        elif y < 17:
            return "forehead"
        elif self.rangeFun(y, "between", 17, 56) and self.rangeFun(x, "between", 15, 85):
            return 'eye'
        elif self.rangeFun(y, "between", 65, 77) and self.rangeFun(x, "between", 25, 75):
            return "mouth"
        elif self.rangeFun(x, "between", 0, 15):
            return "left"
        elif self.rangeFun(x, "between", 85, 100):
            return "right"
        elif self.rangeFun(y, "between", 77, 100) and self.rangeFun(x, "between", 15, 85):
            return "chin"

    def rangeFun (self, input, type, r1, r2):
        if type == "between":
            if r1 < r2:
                if (input > r1) and (input < r2):
                    return True
                else:
                    return False
            else:
                if (input > r2) and (input < r1):
                    return True
                else:
                    return False
        else:
            if r1 < r2:
                if (input < r1) or (input > r2):
                    return True
                else:
                    return False
            else:
                if (input < r2) or (input > r1):
                    return True
                else:
                    return False

    def __str__(self):
        return "Tap, (x,y): "+ str(self.x) +", " +str(self.y) + ", zone: " + str(self.zone)
