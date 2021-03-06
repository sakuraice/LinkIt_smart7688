import time
import sys  
import httplib, urllib
import json

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient


deviceId = "DCj0Rnam"
deviceKey = "kPiH1PR1RVE6qWfk"


integer = 1
float = 3.1415926535

def post_to_mcslite(payload):
    headers = {"Content-type": "text/csv", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10) 

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    value = bridgeclient()
    t0 = value.get("t")
    integer = integer+1
    float = float+0.3
    IntData = "DataInteger,,"+str(integer)
    FloatData = "DataOther,,"+str(float)
    t0String = "DataString,," + time.strftime("%c") + "\n" +IntData + "\n" + FloatData+"\n"
    payload =  t0String
    post_to_mcslite(payload)
    time.sleep(10)
