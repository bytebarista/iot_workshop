import math

from machine import Pin, ADC
from array import array


class Thumbslide:
    x_center = 1580
    y_center = 1769

    def __init__(self, pinx, piny, atten=ADC.ATTN_11DB, width=ADC.WIDTH_12BIT, tolerance=300):
        self._pinX = pinx
        self._pinY = piny
        self._tolerance = tolerance

        ADC.vref(vref=1150)

        self._x = ADC(Pin(self._pinX))
        self._x.atten(atten)
        self._x.width(width)

        self._y = ADC(Pin(self._pinY))
        self._y.atten(atten)
        self._y.width(width)

        self._angle = 0

    @property
    def X(self):
        return self._x

    @property
    def Y(self):
        return self._y

    def read(self):
        return array('i', self._x.read(), self._y.read())

    def readX(self):
        return self._x.read()

    def readY(self):
        return self._y.read()

    def _get_internal_calc_xy_dist(self, x, y):
        x = x if x else self._x.read()
        y = y if y else self._y.read()

        x_dist = x - Thumbslide.x_center
        y_dist = y - Thumbslide.y_center

        return x_dist, y_dist

    def moved(self, x=None, y=None):
        x_dist, y_dist = self._get_internal_calc_xy_dist(x, y)
        dist = math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2))
        return dist >= self._tolerance

    def angle(self, x=None, y=None):
        x_dist, y_dist = self._get_internal_calc_xy_dist(x, y)
        return math.atan2(y_dist, x_dist)
