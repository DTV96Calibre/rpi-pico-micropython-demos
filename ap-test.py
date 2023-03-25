from machine import Pin, Timer
import socket
import network
import gc
gc.collect()
ssid = 'RPI_PICO_AP'
password = 'ah1234567'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while ap.active() == False:
    pass
print('Connection is successful')
print(ap.ifconfig())
def web_page():
    html="""<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>Welcome to microcontrollerslab!</h1></body></html>"""
    return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s' % str(request))
    response = web_page()
    conn.send(response)
    conn.close()

led = Pin("LED", Pin.OUT)
led_timer = Timer()
    
def tick(led_timer):
    global led
    led.toggle()

led_timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)


    
