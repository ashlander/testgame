
class Point:
    """docstring for Point
    Just point with coordinates
"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

############################### CONSTRUCTION ###############################

def empty():
    return Point(x=0.0, y=0.0)

def fromXY(x, y):
    return Point(x,y)

def ftomPoint(point):
    return Point(point.x, point.y)

############################### TESTING ###############################

import gamelogger
import logging
import unittest

class TestPoint(unittest.TestCase):
    """docstring for TestRect
"""
    def testInitEmpty(self):
        pt = empty()
        self.assertEqual(pt.x, 0.0)
        self.assertEqual(pt.y, 0.0)

    def testInitPoint(self):
        pt = Point(1,-1)
        self.assertEqual(pt.x, 1.0)
        self.assertEqual(pt.y, -1.0)
        pt.y += 1.0
        self.assertEqual(pt.x, 1.0)
        self.assertEqual(pt.y, 0.0)
        pt.x -= 1.0
        self.assertEqual(pt.x, 0.0)
        self.assertEqual(pt.y, 0.0)
        pt.shift(3.0,5.0)
        self.assertEqual(pt.x, 3.0)
        self.assertEqual(pt.y, 5.0)

if __name__ == '__main__':
    gamelogger.init('_test_point.log')
    unittest.main()
