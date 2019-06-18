from machine import I2C, Pin

I2C_SCL = 27
I2C_SDA = 32

i2c = I2C(scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
i2c.scan()

from bme280 import BME280
BME280_I2CADDR = 0x76 # 118

bme = BME280(i2c=i2c, address=BME280_I2CADDR)

(t, p, h) = bme.read_compensated_data()



import machine, display, time, _thread, math

tft = display.TFT()
tft.init(tft.ILI9341, width=240, height=320, miso=19,mosi=23,clk=18,cs=0,dc=15, bgr=True)  # SR EXTERNAL
tft.clear()

tft.rect(0, 150, 240, 30)
tft.circle(120, 165, 120)


while True:
	tft.text(10, 160, '%s, %s, %s' % bme.values)
	time.sleep(0.5)