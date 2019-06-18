import mcp

# SPI
SPI_CLK = 18
SPI_DATA = 4
SPI_MISO = 19
SPI_MOSI = 23

# Display
TFT_CS = 0
TFT_DC = 15
TFT_RST = 5

# SD CARD
SDCARD_CS = 14

# LEDs
LEDS = 4
LED_CLK = 13

# GPIO / I2C
I2C_SCL = 27
I2C_SDA = 32

# Thumbslide
THUMBSLIDE_X = 39
THUMBSLIDE_Y = 34

# Touchpad
TOUCHPAD = 12 

# Sound
MIC = 35
DAC = 26
SPEAKER = 2


class _IOExpander:
    def __init__(self, I2C_SCL = 27, I2C_SDA = 32):
        self.io = mcp.MCP23017(address=0x20, gpioScl=I2C_SCL, gpioSda=I2C_SDA)

    def make_pin(self, pin_num):
        return _IOExpanderPin(self.io, pin_num)


class _IOExpanderPin:
    def __init__(self, io: _IOExpander, pin_num: int):
        self.io = io
        self.io.setup(pin_num, mcp.IN)
        self.io.pullup(pin_num, True)
        self.pin_num = pin_num

    def value(self):
        return not self.io.input(self.pin_num)


_io = _IOExpander()

BTN_DOWN_PIN = _io.make_pin(4)
BTN_LEFT_PIN = _io.make_pin(5)
BTN_RIGHT_PIN = _io.make_pin(6)
BTN_UP_PIN = _io.make_pin(7)

PAD_UP_PIN = _io.make_pin(8)
PAD_LEFT_PIN = _io.make_pin(9)
PAD_RIGHT_PIN = _io.make_pin(10)
PAD_DOWN_PIN = _io.make_pin(11)


import machine, display, time, _thread, math

tft = display.TFT()
tft.init(tft.ILI9341, width=240, height=320, miso=19,mosi=23,clk=18,cs=0,dc=15, bgr=True, speed=40000000)  # SR EXTERNAL
tft.clear()

x = 120
y = 160
r = 20

h_speed = 5
v_speed = 5

tft.circle(x, y, r)

while True:
	h_speed += PAD_RIGHT_PIN.value()*5
	h_speed -= PAD_LEFT_PIN.value()*5
	v_speed += PAD_UP_PIN.value()*5
	v_speed -= PAD_DOWN_PIN.value()*5

	if h_speed<5: h_speed = 5
	if v_speed<5: v_speed = 5

	x += BTN_RIGHT_PIN.value()*h_speed
	x -= BTN_LEFT_PIN.value()*h_speed
	y += BTN_DOWN_PIN.value()*v_speed
	y -= BTN_UP_PIN.value()*v_speed


	if x+r<0: x = 240-r
	if x-r>240: x = -r
	if y+r<0: y = 320-r
	if y-r>320: y=-r

	tft.clear()
	tft.circle(x, y, 20)
	# time.sleep(0.01)