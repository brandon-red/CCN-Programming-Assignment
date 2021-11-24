from socket import *
import time
import sys
import random
import os
import filecmp

#checking command line for correct input
if (len(sys.argv) != 2):
	print("Required arguments: <server_ipaddress>")
	exit(0)

#initializeing server ip address and port number
serverIP = sys.argv[1]
serverPort = 9093

#create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

#bool variable representing file is an integral multiple of 512, I dont think we need this 
#if my understanding of the read function is correct
#integralMult = ((os.path.getsize("inputfile.txt") % 512)== 0)

#open the input file to be read in binary form
f = open("inputfile.txt", "r", newline = "\r\n")
newF = f.read().encode()

fileSend = True
lastPacket = False
seqNum = 0

#timer started for entire file transfer
start = time.perf_counter_ns()
while True:

	data = newF.read(512)
	print(sys.getsizeof(data))
	#indicate that this is the last packet to be sent
	if(sys.getsizeof(data) < 512):
		lastPacket = True

	seqNumInBytes = seqNum.to_bytes(1, 'big') 

	#creates message with seqNum header and 512 bytes unless it reaches end of file
	message = seqNumInBytes + data
	
	print(message)

	#retrainsmission loop for a max of 6 tries
	for i in range(6):
		print(seqNum)
		clientSocket.sendto(message, (serverIP, serverPort))
		#set timeout for 1 second
		clientSocket.settimeout(1)
		
		try:
			#get ack from server
			ack = clientSocket.recv(1)
			print(ack)
			#check if ack is correct
			if(ack == seqNumInBytes):
				#updates seqNum
				seqNum = abs(1-seqNum)
				#bool to know that packet was sent successfully
				packetSent = True
				break

		#if there is a timeout, retransmit
		except timeout:
			continue

	#if last packet is successesfully sent, end while loop 
	if(packetSent and lastPacket):
		print("done")
		transferTime = (time.perf_counter_ns() - start)/100000000
		f.close()
		clientSocket.close()
		break

	#if packet has been sent but not the last packet
	elif(packetSent and not lastPacket):
		continue

	else:
		print("no bueno")
		#indicate file could not be sent
		fileSend = False
		break

print(fileSend)
print(filecmp.cmp("inputfile.txt", "outputfile.txt", shallow = False))
#if the file was sent, and if the files are matching
if(fileSend and filecmp.cmp("inputfile.txt", "outputfile.txt", shallow = False)):
	print("sFTP: file sent successfully to {} in {:.3}secs".format(serverIP, transferTime))

else:
	print("sFTP: file transfer unsuccessful: packet retransmission limit reached")
	




