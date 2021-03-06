import sys
import time
import datetime
import requests
import json

# ******************************************************************************************
# Set Firebase URL, Date, Time, Location                                                                                                 
# ******************************************************************************************

IntData = 0
FloatData = 3.1415926535


firebase_url = 'https://fishfirebase.firebaseio.com/LinkItSmart7688'
t = time.time();
#date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

while True:
    value = bridgeclient()
    IntData = IntData + 1
    FloatData = FloatData + 0.3 
    date = time.strftime("%c")
    
    print date + str(IntData) + ',' + str(FloatData)
    
    # ******************************************************************************************
    # Insert Data                                                                              #
    # ******************************************************************************************    
    #************GET Method*************
    #request = requests.get("URL")
    #requeststr = request.text
    #a = requeststr.rindex(",")
    #b = len(requeststr)
    #print requeststr[a+1:b]
    #****************************
    data = {'StringData':date,'IntData':IntData,'FloatData':FloatData}
    result = requests.post(firebase_url + '/LinkItSmart7688.json', data=json.dumps(data))
    print 'Status Code = ' + str(result.status_code) + ', Response = ' + result.text
    request = requests.get("http://api.mediatek.com/mcs/v2/devices/DEb509qK/datachannels/DataInteger/datapoints.csv")
    print request.text
    time.sleep(5)
