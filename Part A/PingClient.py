from socket import *
import time
import sys
import random
import string

# function to create a random 56 byte message
def createString():
	letter = random.choice(string.ascii_letters)
	return letter*56

# checking command line for correct input
if (len(sys.argv) != 3):
    print("Required arguments: <host-name> <port-number>")
    exit(0)

# initializing server name and port number
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# in case of the first packet being lost, we need to have a server ip address ready
serverIP = gethostbyname(serverName)

# keeping track of number of pings
pingNum = 0

# send a ping 5 times
while pingNum < 5:
	# uses createString function to set message
	message = createString()
	# sends message in byte type(encode function) to server
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	# start timer measured in nanoseconds for rtt mesasurement
	start = time.perf_counter_ns()
	# set a 1 second timeout 
	clientSocket.settimeout(1)
	
	try:
		# get returned message from server confirming delivery with 128 byte buffer size 
		retMessage = clientSocket.recv(128)
	
	# timeout handling to avoid exiting program prematurely	
	except timeout:
		# if nothing recieved from server within 1 second, print this statement
		print("PING {} {} LOST".format(serverIP, pingNum))
		pingNum += 1
		# wait one second before sending another ping
		time.sleep(1)
		continue

	# stop timer and calculate rtt in milliseconds	
	end = time.perf_counter_ns()
	rttEstimate = (end - start)/1000000

	# print statement when client recieves reply from server
	print("PING {} {} {:.3f}ms".format(serverIP, pingNum, rttEstimate))
	pingNum += 1
	# wait one second before sending another ping
	time.sleep(1)


# closes the socket
clientSocket.close()