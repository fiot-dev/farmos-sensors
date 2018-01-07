import json
import requests
import time

base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
public_key='PUBLIC_KEY'
private_key='PRIVATE_KEY'

url=base_url+public_key+'?private_key='+private_key

print(url)
    
#head = {'Content-type':'application/json', 'Accept':'application/json'}
             
payload ={ "timestamp": time.time(), "sensor1": 76.0, "sensor2": 60 }

print(payload)

r = requests.post(url, json=payload)
print(r.status_code)


