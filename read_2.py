#**************************************************** 
# Import Package                                                                           
#**************************************************** 
#-----telnet
import telnetlib
import time
HOST="192.168.0.50"
PORT="8501"

#------
import time  
import httplib, urllib  
import json  
import sys  
sys.path.append('/home/pi/rpi/code/Package')  
#import grovepi  
#from grove_rgb_lcd import *

#**************************************************** 
# Set Pin No, MediaTek Cloud Sandbox (MCS) Key                                                                          
#**************************************************** 

sensor = 5  
blue = 0    # The Blue colored sensor.  
white = 1   # The White colored sensor.

deviceId = ""		# DEVICE_ID
deviceKey = ""		# DEVICE_KEY

#**************************************************** 
# Set MediaTek Cloud Sandbox (MCS) Connection                                                   
#**************************************************** 

def post_to_mcs(payload):  #this is upload method
    headers = {"Content-type": "text/csv", "deviceKey": deviceKey}#this is devicekey request
    not_connected = 1 #I think this is whileloop switch
    while (not_connected):#if no anylink
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0#if link is success
        except (httplib.HTTPException, socket.error) as ex:#if link error return here,then wait ten second will be startagain
            print "Error: %s" % ex1
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers) #this have 4 request, 1.POST or GET 2.URL 3.data 4.header 
    response = conn.getresponse()#response
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()

#**************************************************** 
# Post MediaTek Cloud Sandbox (MCS)
#**************************************************** 

while True:
    tn=telnetlib.Telnet(HOST,PORT)
    print tn

    tn.write("rd cm703\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value1=str(data)

    tn.write("rd cm704\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value2=int(data)
    IntData = "DataInteger,," + str(fltWaterWheel_Value2)
    
    tn.write("rd cm705\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value3=float(data)
    FloatData = "DataOther,," + str(fltWaterWheel_Value3)
    
    #payload = {"datapoints":[{"dataChnId":"WaterWheel_led1","values":{"value":intWaterWheel_led1}},{"dataChnId":"WaterWheel_led2","values":{"value":intWaterWheel_led2}},{"dataChnId":"WaterWheel_led3","values":{"value":intWaterWheel_led3}},{"dataChnId":"WaterWheel_Value1","values":{"value":fltWaterWheel_Value1}},{"dataChnId":"WaterWheel_Value2","values":{"value":fltWaterWheel_Value2}},{"dataChnId":"WaterWheel_Value3","values":{"value":fltWaterWheel_Value3}},{"dataChnId":"WaterWheel_Value5","values":{"value":fltWaterWheel_Value5}},{"dataChnId":"WaterWheel_Value20","values":{"value":fltWaterWheel_Value20}}]}
    payload = "DataString,,"+ fltWaterWheel_Value1 + "\n" + IntData + "\n" + FloatData +"\n"
    post_to_mcs(payload)
    time.sleep(7)