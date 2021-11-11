==============================================================
Tests conducted to demonstrate correct function of application
==============================================================

-->The use of Wireshark aided in being able to trace packets going through localhost and allowed me to confirm things were working correctly<--

-----------------------------------------------------------------
|Test 1: Printing messages in client, with no loss rate or delay|
-----------------------------------------------------------------

Source Output:
--------------

b'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
0
Reply sent.
b'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
0
Reply sent.
b'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
0
Reply sent.
b'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL'
0
Reply sent.
b'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
0
Reply sent.

Client Output: 
--------------

PING nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 127.0.0.1 0 0.968ms
PING eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 127.0.0.1 1 2.241ms
PING yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy 127.0.0.1 2 1.362ms
PING LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL 127.0.0.1 3 1.492ms
PING TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT 127.0.0.1 4 3.529ms

**From this test, and analyzing the trace on Wireshark I could confirm:
	-the messages were being delivered correctly
	-the 1 second wait in between pings was working
	-the rtt estimates calculated in my application were very close to the rtt values seen in the UDP Timestamps on Wireshark
	-the size of the packets are consistently 56 bytes

-------------------------------------------------------------------
|Test 2: Printing messages in client, with 20% loss rate and delay|
-------------------------------------------------------------------

Source Output:
--------------

b'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
59
Reply sent.
b'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
Reply not sent.
b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
155
Reply sent.
b'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
31
Reply sent.
b'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
192
Reply sent.

Client Output: 
--------------

PING uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu 127.0.0.1 0 54.127ms
PING 127.0.0.1 1 LOST
PING bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb 127.0.0.1 2 169.875ms
PING GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG 127.0.0.1 3 39.787ms
PING HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH 127.0.0.1 4 199.601ms

**From this test, and analyzing the trace on Wireshark I could confirm:
	-the handling of a lost packet works correctly
	-the rtt estimates were still very close to the values seen in the UDP Timestamps
	-the messages were being delivered correctly and with the right amount of time in between
	-the size of the packets are consistently 56 bytes