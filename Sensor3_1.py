import time

import sys 

import httplib, urllib
import json

import random

import threading

from Queue import Queue

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 

deviceId = ["DCj0Rnam","deviceId2","deviceId3", "deviceId4","deviceId5"]

deviceKey = ["kPiH1PR1RVE6qWfk","deviceKey2", "deviceKey3" ,"deviceKey4" ,"deviceKey5"]


address = ["192.168.0.50", "192.168.0.51", "192.168.0.52"]

PORT = 8501

global results

results = []



print_lock = threading.Lock()



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

			time.sleep(5) 


	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints.csv", payload, headers)

	response = conn.getresponse()

	print( response.status, response.reason, payload, time.strftime("%c"))

	data = response.read()

	conn.close()


#********telnet to plc******** add HOST,PORT

def telnetplc(worker):

	payload = ""

	global results

	time.sleep(0.5)


	integer = random.randint(0,60)

	if integer >=30 :

		payload += "DataInteger,," + str(integer) + "\n"

	float = random.uniform(1,10)

	if float >= 5 :

		payload += "DataOther,," + str(float) + "\n"

	if payload != "" :

		with print_lock :

			payload += worker

			results.append(payload)

	else :

		#time.sleep(3)

		return telnetplc(worker)



def threader():

	while True :

		worker = q.get()

		telnetplc(worker)

		q.task_done()



q = Queue()


#上傳的裝置不同的話，需要修改post_to_mcslite傳入值新增deviceId,deviceKey
while True :

	results = []

	for x in range(3) :#thread amount

		t = threading.Thread(target = threader)

		t.daemon = True

		t.start()


	for i in range(len(address)) :

		q.put(address[i])


	q.join()

	for i in range(len(results)) :

		if results[i].find(address[0]) != -1 :
			results[i] = results[i][:results[i].find(address) -1]
		elif results[i].find(address[1]) != -1 :
			results[i] = results[i][:results[i].find(address) -1]
		elif results[i].find(address[2]) != -1 :
			results[i] = results[i][:results[i].find(address) -1]
		print results[i]

	time.sleep(10)