# This example is using Python 3
import socket
import struct

# Make a TCP socket object.
#
# API: socket(address_family, socket_type)
#
# Address family
#   AF_INET: IPv4
#   AF_INET6: IPv6
#
# Socket type
#   SOCK_STREAM: TCP socket
#   SOCK_DGRAM: UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server machine and port.
#
# API: connect(address)
#   connect to a remote socket at the given address.
server_ip = '10.15.71.104'
server_port = 8181
s.connect((server_ip, server_port))
print('Connected to server ', server_ip, ':', server_port)

# messages to send to server.


def read(message):
	i = 2
	res = '';
	two = message[0:i]
	#print(two)
	follow = struct.unpack('>h', two)[0];
	#print(follow)
	res += (str) (follow)
	#print(res)
	while(follow > 0):
		size = struct.unpack('>h',message[i : i + 2])[0]
		res += (str) (size)
		express = message[i+2 : i + 2 + size]
		s = express.decode('utf-8');
		res += s;
		follow -= 1
		i += 2 + size

	print(res)
	return res;



val = [2,4, "3+12",6, "1+12/3"]
#print(pack('hhs', 2, 4, "3+12"))
bval = []
#print(bytes([3]));
i = 0;
while(i < len(val)):
	if(type(val[i]) == str):
		my_str_as_bytes = val[i].encode('utf-8');
		bval.append(my_str_as_bytes);
		#print(type(my_str_as_bytes))
		#print(my_str_as_bytes);
	
	else:
		#print(type(val[i]))
		my_int_as_bytes = struct.pack('>h', val[i]);
		#print(val[i]);
		#print(struct.pack('>h', val[i]));
		bval.append(my_int_as_bytes);
		#print(type(my_int_as_bytes))
		#print(my_int_as_bytes);
#my_str = "hello world"
	i += 1
#print(bytearray(val));
#data = "1+2"
bval.append(('\n').encode('utf-8'))

# Send messages to server over socket.
#
# API: send(bytes)
#   Sends data to the connected remote socket.
#   Returns the number of bytes sent. Applications
#   are responsible for checking that all data
#   has been sent
#
# API: recv(bufsize)
#   Receive data from the socket. The return value is
#   a string representing the data received. The
#   maximum amount of data to be received at once is
#   specified by bufsize
#
# API: sendall(bytes)
#   Sends data to the connected remote socket.
#   This method continues to send data from string
#   until either all data has been sent or an error
#   occurs.
bufsize = 16
size = 0
i = 0;
data = b'';

while i < len(bval):
	while size < 16:
		if i == len(bval):
			break
		data += bval[i]
		size += len(bval[i])
		i += 1

	cur = data[0:16]
	s.sendall(cur)
	data = data[16:]
	size -= 16
	print('Client sent:', cur)



  
  #data = s.recv(bufsize)
  #print('Client received:', data)

  #i += 1;
#s.sendall(b'');
data = s.recv(bufsize)
print(data)
read(data)
s.close()
  

# Close socket to send EOF to server.
