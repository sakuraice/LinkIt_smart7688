import socket

import threading

import os

import time
confirm = "b'OK'"
def RetrFile(name ,sock):

	try:
		fname = ""
		file = os.listdir(os.getcwd())
		for f in file :
			if os.path.isfile(f):
				fname += f +"\n"
		sock.send(fname.encode())		
		filename = sock.recv(1024)

		if os.path.isfile(filename):

			EXIST = str(os.path.getsize(filename))
			sock.send("EXISTS ".encode() + EXIST.encode())

			print("data size step ok")
			#sock.send(str.encode("EXISTS " + EXIST))
			userResponse = sock.recv(1024)

			print(userResponse[:2])
			#if userResponse[:2] == confirm:#if Client type the Y

			if len(userResponse) >1:
				with open(filename,'rb') as f: 
					bytesToSend = f.read(1024)

					sock.send(bytesToSend)

					f.flush()
					#while bytesToSend != "":
					while len(bytesToSend) > 0:
						bytesToSend = f.read(1024)

						sock.send(bytesToSend)

						f.flush()
						#print(bytesToSend)
					f.close()
				f.close()
		else:

			sock.send("ERR".encode())
	except:
		pass
	finally:
		sock.close()
	


def Main():

	host = '192.168.0.132'

	port = 5000

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#s = socket.socket()
	s.bind((host,port))

	s.listen(5)

	print("Server Started")


	while True:

		c, addr = s.accept()

		print("client connected ip:<" + str(addr) +">")

		t = threading.Thread(target=RetrFile,args=("retrThread", c))

		t.start()


	s.close()


if __name__ == '__main__':

	Main()