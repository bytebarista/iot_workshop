# Example of drawing a 20px red ball to the TFT and moving it around with the Thumbpad
# includes edge detection

import time
from machine import I2C, Pin
import machine
import display
import time
import _thread
import math
from thumbpad import Thumbpad
import pins

thumbpad = Thumbpad(pins.THUMBSLIDE_X, pins.THUMBSLIDE_Y)
analog_val_tol = 450
draw_step = 2
x_center = 1450
y_center = 1450

tft = display.TFT()
background = tft.BLACK
tft.init(tft.ILI9341, width=240, height=320, miso=19, mosi=23,
         clk=18, cs=0, dc=15, bgr=True, speed=40000000)  # SR EXTERNAL

tft.clear(background)
x_pos = 120
y_pos = 160

tft.circle(x_pos, y_pos, 20, color=tft.RED, fillcolor=tft.RED)
hit_edge = False

while True:
    changed = False
    x = thumbpad.readX()
    y = thumbpad.readY()

    if (x - x_center > analog_val_tol and x_pos > 21):
        changed = True
        x_pos -= draw_step
    elif (x_center - x > analog_val_tol and x_pos < 219):
        changed = True
        x_pos += draw_step

    if (y - y_center > analog_val_tol and y_pos < 299):
        changed = True
        y_pos += draw_step

    if (y_center - y > analog_val_tol and y_pos > 21):
        changed = True
        y_pos -= draw_step

    if (changed):
        if (x_pos < 220 and x_pos > 20 and y_pos < 300 and y_pos > 20):
            tft.circle(x_pos, y_pos, 30, color=background,
                       fillcolor=background)
            tft.circle(x_pos, y_pos, 20, color=tft.RED, fillcolor=tft.RED)
        elif (x_pos == 220):
            x_pos -= 1
        elif (x_pos == 20):
            x_pos += 1
        elif (y_pos == 300):
            y_pos -= 1
        elif (y_pos == 20):
            y_pos += 1
