import math


class Segment2D:
    """

    """

    def __init__(self, arg1, arg2):
        self.first_tuple = arg1
        self.second_tuple = arg2

    def length(self):
        x1, y1, = self.first_tuple
        x2, y2 = self.second_tuple

        line = math.sqrt(
            pow(2, (x2 - x1)) + pow(2, (y2 - y1))
        )
        return line

    def slope(self):
        x1, y1, = self.first_tuple
        x2, y2 = self.second_tuple

        slope = (y2 - y1) / (x2 - x1)
        return slope


if __name__ == '__main__':
    new1 = Segment2D((5, 4), (10, 7))
    print(new1.length())
    print(new1.slope())
