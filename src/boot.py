def do_connect(ssid="kubernetes lifeline", pwd="workwork"):
    import network
    import time
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        time.sleep(0.1)
        print("connecting to network... ", end="")
        wlan.connect(ssid, pwd)
        while not wlan.isconnected():
            time.sleep(1)
            wlan.connect(ssid, pwd)
    print("Done!")
    from machine import DAC, Pin

    dac = DAC(26)
    sh = Pin(2, Pin.OUT, Pin.PULL_UP)  # old pin=4
    sh.value(1)
    t = DAC.SINE
    f = 500
    dac.waveform(f, type=t, scale=0)
    time.sleep(0.025)
    dac.stopwave()
    print("network config:", wlan.ifconfig())

do_connect()
