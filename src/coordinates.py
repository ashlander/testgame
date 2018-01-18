import point
import rect

def xLP2DP(lpX, lptLT, lPix = 1.0):
    """Convert logical coordinates into device coordinates
        lpX   - x logical coordinate
        lptLT - logical coordinates of left top screen corner
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return coordinate in device coordinates
    """
    return (lpX - lptLT.x) / lPix

def yLP2DP(lpY, lptLT, lPix = 1.0):
    """Convert logical coordinates into device coordinates
        lpY   - y logical coordinate
        lptLT - logical coordinates of left top screen corner
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return coordinate in device coordinates
    """
    return (lptLT.y - lpY) / lPix

def pointCoordsLP2DP(lpX, lpY, lptLT, lPix = 1.0):
    """Convert logical coordinates into device coordinates
        lpX   - x logical coordinate
        lpY   - y logical coordinate
        lptLT - logical coordinates of left top screen corner
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return point in device coordinates
    """
    return point.fromXY(xLP2DP(lpX, lptLT, lPix), yLP2DP(lpY, lptLT, lPix))

def pointLP2DP(lpoint, lptLT, lPix = 1.0):
    """Convert logical coordinates into device coordinates
        lpoint- point with logical coordinate
        lptLT - logical coordinates of left top screen corner
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return point in device coordinates
    """
    return pointCoordsLP2DP(lpoint.x, lpoint.y, lptLT, lPix)

def rectLP2DP(lpRect, lptLT, lPix = 1.0):
    """Convert logical coordinates into device coordinates
        lpRect- rect with logical coordinate
        lptLT - logical coordinates of left top screen corner
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return rect in device coordinates
    """
    return rect.fromPoints( point.fromXY(pointLP2DP(top_left, lptLT, lPix),
        point.fromXY(pointLP2DP(right_bottom, lptLT, lPix))))

def xDP2LP(dpX, dptZero, lPix = 1.0):
    """Convert device coordinates into logical coordinates
        dpX   - x device coordinate
        dptZero - device coordinates of logical 0,0 point
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return coordinate in logical coordinates
    """
    return (dpX - dptZero.x) * lPix

def yDP2LP(dpY, dptZero, lPix = 1.0):
    """Convert device coordinates into logical coordinates
        dpY   - y device coordinate
        dptZero - device coordinates of logical 0,0 point
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return coordinate in logical coordinates
    """
    return (dptZero.y - dpY) * lPix;    

def pointCoordsDP2LP(dpX, dpY, dptZero, lPix = 1.0):
    """Convert device coordinates into logical coordinates
        dpX   - x device coordinate
        dpY   - y device coordinate
        dptZero - device coordinates of logical 0,0 point
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return point in logical coordinates
    """
    return point.fromXY(xDP2LP(dpX, dptZero, lPix), yDP2LP(dpY, dptZero, lPix))

def pointDP2LP(dpoint, dptZero, lPix = 1.0):
    """Convert device coordinates into logical coordinates
        dpoint- point in device coordinate
        dptZero - device coordinates of logical 0,0 point
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return point in logical coordinates
    """
    return pointCoordsDP2LP(dpoint.x, dpoint.y, dptZero, lPix)

def rectDP2LP(dpRect, dptZero, lPix = 1.0):
    """Convert device coordinates into logical coordinates
        dpRect- rect in device coordinate
        dptZero - device coordinates of logical 0,0 point
        lPix  - zoom value, number of logical points inside one device point (aka pixel)
        return rect in logical coordinates
    """
    return rect.fromPoints( point.fromXY(pointDP2LP(top_left, dptZero, lPix),
        point.fromXY(pointDP2LP(right_bottom, dptZero, lPix))))

############################### TESTING ###############################

import gamelogger
import logging
import unittest

#class TestCoordinates(unittest.TestCase):

    # def testConversions(self):
    #     screenRect = rect.fromSizes(point.fromXY(0.0,0.0), 800, 600)
    #     mapRect = rect.fromSizes(point.fromXY(0.0,0.0), 20, 20)
    #     mainMap = MapCoordinates(screenRect, mapRect)
    #     lPix = mainMap.getZoomToObserveMap()
    #     #screenCentre = screenRect.centre()
    #     screenCentre = point.empty()
    #     lptScreenLT = pointDP2LP(0.0, 0.0, screenCentre, lPix)
    #     logging.info("lPix = %f", lPix)
    #     logging.info("screenCentre = (%f, %f)", screenCentre.x, screenCentre.y)
    #     lptCentre = pointDP2LP(screenCentre.x, screenCentre.y, screenCentre, lPix) # temp
    #     logging.info("screenCentre lpt = (%f, %f)", lptCentre.x, lptCentre.y)
    #     dptMapEnd = pointLP2DP(mapRect.topRight(), lptScreenLT, lPix) # temp
    #     logging.info("dptMapEnd = (%f, %f)", dptMapEnd.x, dptMapEnd.y)
    #     logging.info("lptScreenLT = (%f, %f)", lptScreenLT.x, lptScreenLT.y)
    #     #self.assertEqual(rect.top_left, lt)
    #     #self.assertEqual(rect.right_bottom, rb)
    #     #self.assertEqual(rect.topRight(),   point.fromXY(rb.x,lt.y))
    #     #self.assertEqual(rect.leftBottom(), point.fromXY(lt.x,rb.y))

# if __name__ == '__main__':
#     gamelogger.init('_test_coordinates.log')
#     unittest.main()
