import random
import time
import sys
import filecmp
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 9093))
# Assign Loss and Delay parameters
LOSS_RATE = 0.2
AVERAGE_DELAY = 100

#opens file for writing, and have newline set to \r\n (for windows)
f = open("outputfile.txt", "wb")

expect = 0

while True:
	rand = random.uniform(0, 1)

	message, address = serverSocket.recvfrom(513)

	#print(message)
	#print(message[0])

	#print(message[1:])
	# Decide whether to reply, or simulate packet loss. If rand is less than LOSS_RATE, we consider the packet lost and do not respond
	if rand < LOSS_RATE:
	   print("Lost packet or ack")
	   continue

	# Simulate network delay.
	delay = random.randint(0.0, 2*AVERAGE_DELAY)
	#print(delay)
	time.sleep(delay/1000);

	#last packet sent and if it is in correct order, write then close file and exit loop
	if(sys.getsizeof(message)<513 and (expect == message[0])):
		f.write(message[1:])
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)
		f.close()
		#print("done")
		break
	#check if sequence number matches what receiver is expecting
	elif(expect == message[0]):
		f.write(message[1:])
		#print("written")
		expect = abs(expect-1)
		#send ack
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)
	#receive duplicate therefore send ack, but dont write into file
	else:
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)
















