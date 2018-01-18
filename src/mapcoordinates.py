import coordinates

class MapCoordinates:
    def __init__(self, screenRect, screenZero, mapRect, tileSize=0):
        self.screenRect   = screenRect
        self.mapRect      = mapRect
        self.__screenZero = screenZero
        self.__tileSize   = tileSize
        self.__recalculate()

    def __recalculateLPix(self):
        if self.__tileSize == 0:
            self.__lPix = self.__getZoomToObserveMap()
        else:
            self.__lPix = self.__getZoomToObserveTiles(self.__tileSize)

    def __recalculateLT(self):
        self.__lptScreenLT = coordinates.pointDP2LP(point.empty(), self.__screenZero, self.__lPix)

    def __recalculate(self):
        self.__recalculateLPix()
        self.__recalculateLT()

    def __getZoomToObserveMap(self):
        lxPix = self.mapRect.width() / float(self.screenRect.width())
        lyPix = self.mapRect.height() / float(self.screenRect.height())
        return max(lxPix, lyPix)

    def __getZoomToObserveTiles(self, tileSize):
        return (1 / float(tileSize))

    def __zoom(self, coef):
        assert coef > 0, "Zoom coef %r should be more than 0" % coef
        if self.__tileSize == 0:
            self.__lPix *= coef
            self.__recalculateLT()
            #TODO check for MaxZoom MinZoom
        else:
            logging.warning("Tile size is set, no map zoom allowed")

    def xLP2DP(self, lpX):
        """Convert logical coordinates into device coordinates
            lpX   - x logical coordinate
            return coordinate in device coordinates
        """
        return coordinates.xLP2DP(lpX, self.__lptScreenLT, self.__lPix)

    def yLP2DP(self, lpY):
        """Convert logical coordinates into device coordinates
            lpY   - y logical coordinate
            return coordinate in device coordinates
        """
        return coordinates.yLP2DP(lpY, self.__lptScreenLT, self.__lPix)

    def pointCoordsLP2DP(self, lpX, lpY):
        """Convert logical coordinates into device coordinates
            lpX   - x logical coordinate
            lpY   - y logical coordinate
            return point in device coordinates
        """
        return coordinates.pointCoordsLP2DP(lpX, lpY, self.__lptScreenLT, self.__lPix)

    def pointLP2DP(self, lpoint):
        """Convert logical coordinates into device coordinates
            lpoint- point with logical coordinate
            return point in device coordinates
        """
        return coordinates.pointLP2DP(lpoint, self.__lptScreenLT, self.__lPix)

    def rectLP2DP(self, lpRect):
        """Convert logical coordinates into device coordinates
            lpRect- rect with logical coordinate
            return rect in device coordinates
        """
        return coordinates.rectLP2DP(lpRect, self.__lptScreenLT, self.__lPix)

    def xDP2LP(self, dpX):
        """Convert device coordinates into logical coordinates
            dpX   - x device coordinate
            return coordinate in logical coordinates
        """
        return coordinates.xDP2LP(dpX, self.__screenZero, self.__lPix)

    def yDP2LP(self, dpY):
        """Convert device coordinates into logical coordinates
            dpY   - y device coordinate
            return coordinate in logical coordinates
        """
        return coordinates.yDP2LP(dpY, self.__screenZero, self.__lPix)

    def pointCoordsDP2LP(self, dpX, dpY):
        """Convert device coordinates into logical coordinates
            dpX   - x device coordinate
            dpY   - y device coordinate
            return point in logical coordinates
        """
        return coordinates.pointCoordsDP2LP(dpX, dpY, self.__screenZero, self.__lPix)

    def pointDP2LP(self, dpoint):
        """Convert device coordinates into logical coordinates
            dpoint- point in device coordinate
            return point in logical coordinates
        """
        return coordinates.pointDP2LP(dpoint, self.__screenZero, self.__lPix)

    def rectDP2LP(self, dpRect):
        """Convert device coordinates into logical coordinates
            dpRect- rect in device coordinate
            return rect in logical coordinates
        """
        return coordinates.rectDP2LP(dpRect, self.__screenZero, self.__lPix)

    def zoomIn(self, xTimes):
        assert xTimes > 0, "Zoom coef %r should be more than 0" % xTimes
        self.__zoom(xTimes)

    def zoomOut(self, xTimes):
        assert xTimes > 0, "Zoom coef %r should be more than 0" % xTimes
        self.__zoom(1/xTimes)

    # def zoom(self, dpTileSize):
    #     assert dpTileSize > 0, "Tile size %r should be more than 0" % dpTileSize
    #     self.__zoom()

    def zoomDefault(self):
        if self.__tileSize == 0:
            self.__recalculate()
        else:
            logging.warning("Tile size is set, no map zoom allowed")

    def shift(self, dx, dy):
        self.__screenZero.shift(dx,dy)
        self.__lptScreenLT.shift(dx,dy)

############################### CONSTRUCTION ###############################3

import point
import rect

def constructPositive(screenWidth, screenHeight, mapWidth, mapHeight, tileSize=0):
    """Constructs map coordinates to place the map inside positive X and Y range to the centre of the screen"""
    screenRect = rect.fromSizes(point.fromXY(0.0,0.0), screenWidth, screenHeight) # set screen sizes
    mapRect    = rect.fromSizes(point.fromXY(0.0,0.0), mapWidth, mapHeight)       # set map sizes
    screenZero = screenRect.centre()                                 # set logical 0.0 to the centre of ths screen
    mapCoordinates = MapCoordinates(screenRect, screenZero, mapRect, tileSize) # construct map coordinates translator
    mapCoordinates.shift(mapRect.centre().x, mapRect.centre().y)     # place map at the centre of the screen
    return mapCoordinates

############################### TESTING ###############################

import gamelogger
import logging
import unittest

class TestCoordinates(unittest.TestCase):

    def testConversions(self):
        mapCoordinates = constructPositive(screenWidth=800, screenHeight=600, mapWidth=20, mapHeight=20)
        screenMapLeftBottom = mapCoordinates.pointCoordsLP2DP(0.0, 0.0)
        self.assertAlmostEqual(screenMapLeftBottom.x, 100)
        self.assertAlmostEqual(screenMapLeftBottom.y, 600)
        mapRect     = mapCoordinates.mapRect
        mapTopRight = mapRect.topRight()
        screenMapRightTop = mapCoordinates.pointCoordsLP2DP(mapTopRight.x, mapTopRight.y)
        self.assertAlmostEqual(screenMapRightTop.x, 700)
        self.assertAlmostEqual(screenMapRightTop.y, 0)

    def testTileConversions(self):
        mapCoordinates = constructPositive(screenWidth=800, screenHeight=600, mapWidth=20, mapHeight=20, tileSize=10)
        screenMapLeftBottom = mapCoordinates.pointCoordsLP2DP(0.0, 0.0)
        self.assertAlmostEqual(screenMapLeftBottom.x, 300)
        self.assertAlmostEqual(screenMapLeftBottom.y, 400)
        mapRect     = mapCoordinates.mapRect
        mapTopRight = mapRect.topRight()
        screenMapRightTop = mapCoordinates.pointCoordsLP2DP(mapTopRight.x, mapTopRight.y)
        self.assertAlmostEqual(screenMapRightTop.x, 500)
        self.assertAlmostEqual(screenMapRightTop.y, 200)

if __name__ == '__main__':
    gamelogger.init('_test_mapcoordinates.log')
    unittest.main()
