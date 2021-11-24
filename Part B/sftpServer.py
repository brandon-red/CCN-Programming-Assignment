import random
import time
import sys
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 9093))
# Assign Loss and Delay parameters
LOSS_RATE = 0
AVERAGE_DELAY = 0

#opens file for writing, must write in text, so decode message from client
f = open("outputfile.txt", "w", newline="\r\n")

expect = 0

while True:
	rand = random.uniform(0, 1)

	message, address = serverSocket.recvfrom(513)

	#print(message)
	print(message[0])

	print(message[1:])
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
		f.write(message[1:].decode())
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)
		print("done")
		break
	#check if sequence number matches what receiver is expecting
	elif(expect == message[0]):
		print("written")
		f.write(message[1:].decode())
		expect = abs(expect-1)
		#send ack
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)
	#receive duplicate therefore send ack, but dont write into file
	else:
		serverSocket.sendto(message[0].to_bytes(1, "big"), address)















