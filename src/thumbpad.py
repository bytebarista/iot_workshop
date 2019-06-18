from machine import Pin, ADC
from array import array


class Thumbpad:
    def __init__(self, pinx, piny, atten=ADC.ATTN_11DB, width=ADC.WIDTH_12BIT):
        self._pinX = pinx
        self._pinY = piny
        ADC.vref(vref=1150)

        self._x = ADC(Pin(self._pinX))
        self._x.atten(atten)
        self._x.width(width)

        self._y = ADC(Pin(self._pinY))
        self._y.atten(atten)
        self._y.width(width)

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
