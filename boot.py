try:
    import usocket as socket
except:
    import socket
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
ssid = 'MYPYKEYLIGHTAP'
password = 'mypykeylightap'

ap = network.WLAN(network.AP_IF)
ap.active(True)
#ap.config(essid=ssid, password=password)
ap.config(essid=ssid,authmode=network.AUTH_WPA_WPA2_PSK, password=password)

while ap.active() == False:
    pass
print(ap.ifconfig())

def web_page():
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head><body><h1>KEYLIGHT-CONTROLLER</h1></body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
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
