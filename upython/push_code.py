import ujson as json
import urequests as requests
import time

base_url = 'https://wolfesneck.farmos.net/farm/sensor/listener/'
public_key='PUBLIC_KEY'
private_key='PRIVATE_KEY'

url = base_url+public_key+'?private_key='+private_key

headers = {'Content-type':'application/json', 'Accept':'application/json'}
	
payload ={"sensor1": 10.9 }
 
def post_data():
    r = requests.post(url,data=json.dumps(payload),headers=headers)
    print('Status', r.status_code)
    r.close()

WIFI_NET = 'WIFI_NET'
WIFI_PASSWORD = 'WIFI_PASSWORD'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_NET, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


do_connect()
post_data()

