import threading

from Queue import Queue

import time

import random


address = ["192.168.0.50", "192.168.0.51", "192.168.0.52"]

global results

results = []

print_lock = threading.Lock()

def exampleJob(worker) :

	global results

	payload = ""

	time.sleep(0.5)

	integer = random.randint(0,60)

	if integer >=30 :

		payload += "DataInteger,," + str(integer) + "\n"

	float = random.uniform(1,10)

	if float >=5 :

		payload += "DataOther,," + str(float) + "\n"

	if payload != "" :

		with print_lock :

			results.append(payload)

	else :

		return exampleJob(worker)


def threader() :

	while True :

		worker = q.get()

		exampleJob(worker)

		q.task_done()


q = Queue()


while True :

	for x in range(3) :

		t = threading.Thread(target = threader)

		t.daemon = True

		t.start()


	start = time.time()


	for worker in range(len(address)) :

		q.put(worker)


	q.join()

	for i in range(len(results)) :

		print results[i]

	time.sleep(3)
