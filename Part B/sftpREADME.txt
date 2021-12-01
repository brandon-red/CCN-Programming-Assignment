---------------------------
Print statements explained:
---------------------------

************
***Client***
************
------------------------------------
+print size of data, not including header to ensure 512 bytes of data
+print packet content (1 byte header + 512 bytes data) to ensure header and data is correct and matches what is recieved by the server
+print seqNum before sending to server to ensure that it is correct and changing the way it should after every packet sent
+print ACK number to ensure it is correct and matches what the server output
+print when there is a timeout to ensure timeout is working and the output following that is the correct handling of a timeout
+print "packet sent" after every packet that is successfully sent to the server
+print "file not sent" when indicators show that a packet has not been sent after maximum retransmissions, to show that the code is correctly flowing, and we can therefore go to the unsuccessful send print statement
+print "last packet being sent" when it is recognized that the data being sent is less than 512 bytes
+print "file sent" when packet sent successfully indicator and last packet indicator are true, this indicates file send is complete
+print output of file comparison function between input and output files
+print final output line and make sure that is correct based on the previous print statement
------------------------------------

************
***Server***
************
------------------------------------
print what sequence number the server is expecting
print packet content (1 byte header + 512 bytes of data) recieved by the client to see if it matches what the client sent out 
print "lost packet or ACK"if there is a loss 
print "data written, ACK # sent" if there is a successful packet recieved
print "ACK # sent, duplicate data not written" if there is a packet received, but expected sequence number does not match the packet header
print "File transfer complete" when server recieves data less than 512, and the expect matches the header, to indicate the server has finished writing
------------------------------------

------------------------------------
Test 1: No Loss, No Delay, 2KB file:
------------------------------------

*******************
***Client Output***
*******************

------------------------------------
Size of data (bytes): 512
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
Sequence Number: 0 
ACK: b'\x00' 
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'    
Sequence Number: 1
ACK: b'\x01'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
Sequence Number: 0
ACK: b'\x00'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
Sequence Number: 1 
ACK: b'\x01' 
Packet sent    

Size of data (bytes):165
Last packet being sent
Packet content:b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
Sequence Number: 0
ACK: b'\x00'
Packet sent    

File sent
File contents are the same:True
sFTP: file sent successfully to 127.0.0.1 in 0.010secs   
------------------------------------

*******************
***Server Output***
*******************

------------------------------------
Expecting seqNum: 0
Packet content: b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
data written, ACK 0 sent

File transfer complete
------------------------------------

*****************
***Conclusions***
*****************
+We can see that there is a consistent sending of 512 bytes of data, except for last packet
+We can confirm that server is recieving correct data
+We can confirm sequence numbers and ACKs are being sent and changing correctly
+We can confirm that connection closing works when the last packet has less that 512B of data
+We can confirm that file writing is correct as the files are the same upon comparison at the end of transfer

----------------------------------------
Test 2: 10% Loss, 200ms Delay, 2KB file:
----------------------------------------

*******************
***Client Output***
*******************

------------------------------------
Size of data (bytes): 512
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
Sequence Number: 0
ACK: b'\x00'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
Sequence Number: 1
ACK: b'\x01'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
Sequence Number: 0
ACK: b'\x00'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
Sequence Number: 1
Timeout occured
Sequence Number: 1
ACK: b'\x01'
Packet sent

Size of data (bytes): 165
Last packet being sent
Packet content: 
b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
Sequence Number: 0
ACK: b'\x00'
Packet sent

File sent
File contents are the same: True
sFTP: file sent successfully to 127.0.0.1 in 2.103secs
------------------------------------

*******************
***Server Output***
*******************

------------------------------------
Expecting seqNum: 0
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
Lost packet or ACK

Expecting seqNum: 1
Packet content:
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: 
b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
data written, ACK 0 sent

File transfer complete
------------------------------------

*****************
***Conclusions***
*****************
+We can confirm that both client and server can handle a lost packet/ack
+We can confirm that timeout handling of client is correct, it is not shown, but packet will resend until correct ack is received before timeout

-----------------------------------------
Test 3: 10% Loss, 1000ms Delay, 2KB file:
-----------------------------------------

*******************
***Client Output***
*******************

------------------------------------
Size of data (bytes): 512
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
Sequence Number: 0
Timeout occured
Sequence Number: 0
Timeout occured
Sequence Number: 0
ACK: b'\x00'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
Sequence Number: 1
Timeout occured
Sequence Number: 1
ACK: b'\x00'
Sequence Number: 1
Timeout occured
Sequence Number: 1
ACK: b'\x01'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
Sequence Number: 0
ACK: b'\x01'
Sequence Number: 0
Timeout occured
Sequence Number: 0
ACK: b'\x01'
Sequence Number: 0
ACK: b'\x00'
Packet sent

Size of data (bytes): 512
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
Sequence Number: 1
ACK: b'\x00'
Sequence Number: 1
ACK: b'\x00'
Sequence Number: 1
Timeout occured
Sequence Number: 1
ACK: b'\x00'
Sequence Number: 1
ACK: b'\x01'
Packet sent

Size of data (bytes): 165
Last packet being sent
Packet content: 
b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
Sequence Number: 0
Timeout occured
Sequence Number: 0
ACK: b'\x01'
Sequence Number: 0
Timeout occured
Sequence Number: 0
ACK: b'\x01'
Sequence Number: 0
ACK: b'\x01'
Sequence Number: 0
ACK: b'\x01'
File not sent
File contents are the same: False
sFTP: file transfer unsuccessful: packet retransmission limit reached
------------------------------------

*******************
***Server Output***
*******************

------------------------------------
Expecting seqNum: 0
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
Lost packet or ACK

Expecting seqNum: 0
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: 
b'\x00YpcblemVFWJKSDTnojHCYXriGjSoUhoQwennBugcJYKFPxHaoqwPpELrmzsGPbcEnvywGrIguMPnflRaPHMyphsHTYvlXgQgwmGBkUUCWXCgUdqPUIjxLHNufQGeeBNPtniKLvFRlZuskZeaMBKGCXTOKhiViFMkHswWgdYYNGKNeUhfqQbHqrDCzekfnoPVkmjpdUbXTTfzABcpkeRSCfqxIKxOlMjRnmJCZaqXHZXpAMRHKJoSXkEDhofsgBFJGMvnCKvxsQTNhTDsFyLrFpNRcdCYbROtEkAevfImYFfRdKzQsNIcJWZbpZCwEcGFVqeTDdRyXhcbABvZbtXdaonumxEvrkZYSSxWULrYVoDbVSeFFJxWkJGOliMOAUWgfOLYUmFkJPJKmpNrTQUVQZBhMLqigFoThkZBAhMyDbmdKDYxekwjDEnqDrOWYOmOCjshNbckJalFISFzKUadBGJEZzJxRLn'
ACK 0 sent, duplicate data not written

Expecting seqNum: 1
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
Lost packet or ACK

Expecting seqNum: 0
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x01ChbTGMlnKtVtaXEFhXMFipmDTFifFSNYjsBvSghzrYBDbMkDgBaDAntxsXfKNerxiZqLDvwqsiZAcuCnvtohoRBFWOOJNePPOvvySPdMKKvqvCBaePCsTMYXlMqNunwpuXIaikVFpEGlxLQFSPATEWIWWCrXyvYjnSJrrXsAdjAHVfMVVTYJiHUYIyQKzNRgOalsklyAlRnIqKwLtBqUqyfHRGuOcaDzJfSUJJZJwYMENCAHjeWqozhsVGcpuULWhKDozbDJgOQWDaUrpYNVwIjasNaqRYafWqrXVRpzDNsJZMwXLfcKumwAnjzaliAArbLSTcqjECvLHYODmkREIrrDgNotNxxEwLOAAjubbJRJxKSUlbsdIbBPDObRIpiMyrZagzWGKOximkvbWtTLpTrqvipdYTfXkwIYWZxskgeDuUHAiVKYJLTGbhrjajgyTMAKSXUBFKeczNdJUsTVAzTLyJkkeRc'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
data written, ACK 0 sent

Expecting seqNum: 1
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
ACK 0 sent, duplicate data not written

Expecting seqNum: 1
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
ACK 0 sent, duplicate data not written

Expecting seqNum: 1
Packet content: 
b'\x00EHgCnWgemPqRWLzViFHICTJLSPwIHnvfDLgfSBJLtRXhxsvBRiPFKbmmjACOVxDuXRzFVULYjwuiZTsNqmnaojKoUgHKUeNIbpodnPaATaeFmUQslxZiDkozYezHVJPiyuRiZGerykuiLKcoHeakoWkqHbvykrRoKqZNUtZIUPhZoOWWKMDeXbUrXGQzIGtRTHtXJTkfmWqhZBQdqHtgTuRppddIKDfrKcshYxLWOBuATQARqxZPxKGylItQTMJDMOkciTLCSaPHPxuYyrAwsVwLITtfBPQwKxtQwRtQKQgFHGJVWHjPtSwiOFHztRMZqKZRPqOYJeGeIcfvvHhZVvqcclYNvSeCgmzLtnjIzwAJUtwnJXNIziSVdgJUGssZXurdBUwobVZNbQxNbkaOxYUHcTweGxupinOjRdRRocdslIWZWchnNjLRiuDYoPPBgHyqVoPDlHIxDrMAbnfCpCLhqReQzTd'
ACK 0 sent, duplicate data not written

Expecting seqNum: 1
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
data written, ACK 1 sent

Expecting seqNum: 0
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x01DrGdmGTCoToYOMpKidqkuTONFBuKgDozEoWdPXcAVKlRrqaOffSSOAhgSIzdRFODEhxMvnUaXmarJmoKsGTqlGELywryxtZKiWqxmeBiYNQcdzbDmCLnwCaDQrFaczkJJmlAoAptoTqdLWiaQjDlzLfGADQCVEMqciNYbeWJHVEJgVtapCUBUvzEvSRHKoHDXeUHobYDyYSQSGbpycNlPnOMxylCTChnmjOrnayBzBjUnWHcDzcpWPKyPzkxBpzUAqmnCpOWlyjhhUIulPfQMSOScFmzifhkjRSNOiwcjcfKGJcoXLgGULgGOyXxtLXGoSwZmRyqnQeKgJJbIiFlXzFwtJVVAqvsjKlDcpFNUwwbcFGrRLQXAyLxpIUAjmVPtXLUpWjZYFqnGxcKNiEVPRBFbOYwZoduKucGfCGLyGFRkDHVeGUIQhANboQXiFodrpDPPvYDVSmhIjCPkJvmxcQjUbyBKlv'
ACK 1 sent, duplicate data not written

Expecting seqNum: 0
Packet content: 
b'\x00PGtXynritKeWcWOuDUlWEPrEtIcLPSoanXMLfIQuwColAnoJOObbcZPSAhwVZbpYGguArYytuHdTkCfJDvOIfwYNLZTyHPVeooEKQYAeECVdMxzHTRDuhlWaZBsyzgkzLJSe'
------------------------------------

*****************
***Conclusions***
*****************
+We can confirm duplicate ACKs are handled correctly by the client
+We can confirm duplicate packets are handled correctly by the server
+We can confirm that maximum retransmission limit is working


-----------------------------------------
Test 4: 10% Loss, 100ms Delay, 512B file:
-----------------------------------------

**Note: We know that all the previous tests prove functionality, therefor output is as follows:
Client:
+final print statement
Server:
+"Lost packet or ACK" if loss is simulated
+delay
+ACK# sent

*******************
***Client Output***
*******************

------------------------------------
sFTP: file sent successfully to 127.0.0.1 in 1.222secs
------------------------------------

*******************
***Server Output***
*******************
------------------------------------
Lost packet or ACK
140
ACK 0 sent
74
ACK 1 sent
------------------------------------

*****************
***Conclusions***
*****************
+We know that any integral multiple of 512B file size will be transferred correctly