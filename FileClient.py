import socket


def Main():

	host = '192.168.0.132'

	port = 5000

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
	#s = socket.socket()

	s.connect((host,port))

	filename = raw_input("Filename? -> ")

	if filename !='q':

		s.send(filename)

		data = s.recv(1024)

		if data[:6] == 'EXISTS':
#if receive data top 6 words =EXISTS
			filesize = long(data[6:])
#get filesize after data 6 words
			message = raw_input("File Existts, " + str(filesize)+"Bytes, download? (Y/N)? -> ")

			if message == 'Y':

				s.send('OK')
#send "OK", for FileServer line 11,
				f = open('' + filename, 'wb')#new a file ,and write type is wb

				data = s.recv(1024)
#receive data
				totalRecv = len(data)
#first run to write filelength
				f.write(data)
#write data to newfile
				while totalRecv < filesize:

					data = s.recv(1024)

					totalRecv += len(data)

					f.write(data)

					print( "{0:.2f}".format((totalRecv / float(filesize))*100) + "% Done")

				print ("Download Complete!")

				f.close()
			else:
				print "Download is canceled"
		else:

			print("File does not Exist!")
	s.close()

if __name__ == '__main__':

	Main()