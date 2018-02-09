import socket

import time

def Main():

	host = '192.168.0.132'

	port = 5000
	while True:

		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

		s.connect((host,port))

		#filename = raw_input("Filename? -> ")

		filename = "test.jpg"

		s.send(filename)

		data = s.recv(1024)

		if data[:6] == 'EXISTS':
#if receive data top 6 words =EXISTS
			filesize = long(data[6:])
#get filesize after data 6 words


			s.send('OK')
#send "OK", for FileServer line 11,
			f = open('' + filename, 'wb')#new a file ,and write type is wb

			data = s.recv(1024)
#receive data
			total = len(data)
#first run to write filelength
			f.write(data)
#write data to newfile
			while total < filesize:

				data = s.recv(1024)

				total += len(data)

				f.write(data)

				print( "{0:.2f}".format((total / float(filesize))*100) + "% Done")

			print ("Download Complete!")

			f.close()
		else:

			
			print("File does not Exist!")
		s.close()
		time.sleep(15)

if __name__ == '__main__':

	Main()