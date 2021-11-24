import random
import time
import sys
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind('', 9093)
# Assign Loss and Delay parameters
LOSS_RATE = 0
AVERAGE_DELAY = 0



