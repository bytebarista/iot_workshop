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
    print("network config:", wlan.ifconfig())

def do_webrepl():
	import webrepl
	import machine
	webrepl.start()
	pwd = machine.unique_id()
	# or, start with a specific password
	webrepl.start(password=pwd)

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)
