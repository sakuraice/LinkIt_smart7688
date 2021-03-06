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

deviceId = "DzC55sKi"  
deviceKey = "sDAI3AhY0ngAUb9k"

#**************************************************** 
# Set MediaTek Cloud Sandbox (MCS) Connection                                                   
#**************************************************** 

def post_to_mcs(payload):  #this is upload method
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}#this is devicekey request
    not_connected = 1 #I think this is whileloop switch
    while (not_connected):#if no anylink
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0#if link is success
        except (httplib.HTTPException, socket.error) as ex:#if link error return here,then wait ten second will be startagain
            print "Error: %s" % ex1
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) #this have 4 request, 1.POST or GET 2.URL 3.data 4.header 
    response = conn.getresponse()#response
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

#**************************************************** 
# Post MediaTek Cloud Sandbox (MCS)
#**************************************************** 

while True:
    tn=telnetlib.Telnet(HOST,PORT)
    print tn

    t1n.write("rd cm703\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value1=data
    #fltWaterWheel_Value1=fltWaterWheel_Value1/100;

    t1n.write("rd cm704\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value2=data
    #fltWaterWheel_Value1=fltWaterWheel_Value1/100;
    
    t1n.write("rd cm705\r\n")
    time.sleep(1)
    data=tn.read_very_eager()
    fltWaterWheel_Value3=data
    #fltWaterWheel_Value1=fltWaterWheel_Value1/100;

    #tn.write("rd d10000\r\n")
    #time.sleep(1)
    #data=tn.read_very_eager()
    #fltWaterWheel_Value1=float(data)
    #fltWaterWheel_Value1=fltWaterWheel_Value1/100;

    print(fltWaterWheel_Value1 + "\n" + fltWaterWheel_Value2 + "\n" + fltWaterWheel_Value3 +"\n")


    #[temp,humidity] = grovepi.dht(sensor,blue)
   
    #print("Oxygen = %.02f ppm Ph =%.02f% Temprature =%.02f%%"%(fltOxygen,fltPh,fltTemprature))
    #payload = {"datapoints":[{"dataChnId":"WaterWheel_led1","values":{"value":intWaterWheel_led1}},{"dataChnId":"WaterWheel_led2","values":{"value":intWaterWheel_led2}},{"dataChnId":"WaterWheel_led3","values":{"value":intWaterWheel_led3}},{"dataChnId":"WaterWheel_Value1","values":{"value":fltWaterWheel_Value1}},{"dataChnId":"WaterWheel_Value2","values":{"value":fltWaterWheel_Value2}},{"dataChnId":"WaterWheel_Value3","values":{"value":fltWaterWheel_Value3}},{"dataChnId":"WaterWheel_Value5","values":{"value":fltWaterWheel_Value5}},{"dataChnId":"WaterWheel_Value20","values":{"value":fltWaterWheel_Value20}}]}
    #post_to_mcs(payload)
    time.sleep(8)


1231231231321231312313

1231231231321231312313

1231231231321231312313
1231231231321231312313
1231231231321231312313

1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
1231231231321231312313
12312312313212313123131231231231321231312313
12312312313212313123131231231231321231312313
12312312313212313123131231231231321231312313
12312312313212313123131231231231321231312313
12312312313212313123131231231231321231312313
12312312313212313123131231231231321231312313
1231231231321231312313
12