from collections import namedtuple

Point = namedtuple('Point', 'x, y')


class MyPoint:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(3, 4)

    print(Point(2, 3) in [p1, p2])  # True

    mp1 = MyPoint(2, 3)
    mp2 = MyPoint(3, 4)

    print(MyPoint(2, 3) in [mp1, mp2])  # False
