import point

class Rect:
    """docstring for Rect
    Just rectangle with coordinates
"""
    def __init__(self, point1 = point.empty(), point2 = point.empty()):
        """Initialize rect with two points
        Note: The result will be:
            rect.left < rect.right
            rect.bottom < rect.top
        """
        self.__topLeft = point.empty()
        self.__rightBottom = point.empty()
        if point1.x < point2.x:
            self.__topLeft.x = point1.x
            self.__rightBottom.x = point2.x
        else:
            self.__topLeft.x = point2.x
            self.__rightBottom.x = point1.x

        if point1.y > point2.y:
            self.__topLeft.y = point1.y
            self.__rightBottom.y = point2.y
        else:
            self.__topLeft.y = point2.y
            self.__rightBottom.y = point1.y

    def __eq__(self, other):
        """Check if current rect is equal to other rect"""
        return (self.__topLeft == other.__topLeft and self.__rightBottom == other.__rightBottom)

    def topLeft(self):
        return self.__topLeft

    def rightBottom(self):
        return self.__rightBottom

    def topRight(self):
        """Get top right rect point"""
        return point.fromXY(self.__rightBottom.x, self.__topLeft.y)

    def leftBottom(self):
        """Get left bottom rect point"""
        return point.fromXY(self.__topLeft.x, self.__rightBottom.y)

    def centre(self):
        """Get rect centre point"""
        return point.fromXY((self.__rightBottom.x + self.__topLeft.x)/2.0, (self.__topLeft.y + self.__rightBottom.y)/2.0)

    def width(self):
        """Get rect width"""
        fres = self.__rightBottom.x - self.__topLeft.x
        if fres < 0:
            fres = -fres
        return fres

    def height(self):
        """Get rect height"""
        fres = self.__topLeft.y - self.__rightBottom.y
        if fres < 0:
            fres = -fres
        return fres

    def ptInRect(self, point):
        """If point is within the rect"""
        if point.x > self.__rightBottom.x:
            return False
        if point.x < self.__topLeft.x:
            return False
        if point.y > self.__topLeft.y:
            return False
        if point.y < self.__rightBottom.y:
            return False
        return True

    def union(self, rect):
        """Construct bounding box for this and other rect"""
        if self.__topLeft.x > rect.__topLeft.x:
            self.__topLeft.x = rect.__topLeft.x
        if self.__topLeft.y > rect.__topLeft.y:
            self.__topLeft.y = rect.__topLeft.y

        if self.__rightBottom.x < rect.__rightBottom.x:
            self.__rightBottom.x = rect.__rightBottom.x
        if self.__rightBottom.y < rect.__rightBottom.y:
            self.__rightBottom.y = rect.__rightBottom.y

    def shiftX(self, dx):
        """Move rect by X"""
        self.__topLeft.x += dx
        self.__rightBottom.x += dx

    def shiftY(self, dy):
        """Move rect by Y"""
        self.__topLeft.y += dy
        self.__rightBottom.y += dy

    def shift(self, dx, dy):
        """Move rect by XY"""
        self.shiftX(dx)
        self.shiftY(dy)

############################### CONSTRUCTION ###############################3

def empty():
    """Initialize empty rect"""
    return Rect(point.empty(), point.empty())

def fromPoints(point1, point2):
    """Initialize rect with two points"""
    return Rect(point1, point2)

def fromSizes(ptStart, rectWidth, rectHeight):
    """Initialize rect with starting point, width and length"""
    return Rect(ptStart, point.fromXY(ptStart.x+rectWidth, ptStart.y+rectHeight))

def fromRect(rect):
    """Initialize rect with other rect"""
    return Rect(rect.__topLeft, rect.__rightBottom)

############################### TESTING ###############################

import gamelogger
import logging
import unittest

class TestRect(unittest.TestCase):

    def testInitEmpty(self):
        lt = point.empty()
        rb = point.empty()
        rect = fromPoints(lt, rb)
        self.assertEqual(rect.topLeft(), lt)
        self.assertEqual(rect.rightBottom(), rb)
        self.assertEqual(rect.topRight(),   point.fromXY(rb.x,lt.y))
        self.assertEqual(rect.leftBottom(), point.fromXY(lt.x,rb.y))

    def testInitPointValues(self):
        lt = point.fromXY(4.0, 6.0)
        rb = point.fromXY(10.0,10.0)
        rect = fromPoints(lt, rb)
        self.assertEqual(rect.topLeft(),     point.fromXY(4.0,10.0))
        self.assertEqual(rect.rightBottom(), point.fromXY(10.0, 6.0))
        self.assertEqual(rect.topRight(),   point.fromXY(10.0, 10.0))
        self.assertEqual(rect.leftBottom(), point.fromXY(4.0, 6.0))

    def testCentre(self):
        lt = point.fromXY(4.0, 6.0)
        rb = point.fromXY(10.0,10.0)
        rect = fromPoints(lt, rb)
        pt = rect.centre()
        self.assertEqual(pt, point.fromXY(7.0, 8.0))

    def testNegativeCentre(self):
        lt = point.fromXY(-4.0, 6.0)
        rb = point.fromXY(10.0, -10.0)
        rect = fromPoints(lt, rb)
        pt = rect.centre()
        self.assertEqual(pt, point.fromXY(3.0, -2.0))

    def testShift(self):
        lt = point.fromXY(-4.0, 6.0)
        rb = point.fromXY(10.0, -10.0)
        rect = fromPoints(lt, rb)
        rect.shiftX(1.0)
        rect.shiftY(-1.0)
        self.assertEqual(rect.topLeft(),     point.fromXY(-3.0, 5.0))
        self.assertEqual(rect.rightBottom(), point.fromXY(11.0, -11.0))


if __name__ == '__main__':
    gamelogger.init('_test_rect.log')
    unittest.main()
