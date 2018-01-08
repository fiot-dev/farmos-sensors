import json
import requests
import time

base_url='https://wolfesneck.farmos.net/farm/sensor/listener/'
public_key='PUBLIC_KEY'
private_key='PRIVATE_KEY'

url=base_url+public_key+'?private_key='+private_key
    
headers = {'Content-type':'application/json', 'Accept':'application/json'}
             
payload ={"switch_001": 0 }

def post_data():
    r=requests.post(url,data=json.dumps(payload),headers=headers)
    print('Status:',r.status_code)
    r.close()
    
post_data()
    





