# This example is using Python 3
import socket
import struct
import _thread
# Get host name, IP address, and port number.
#
# API: gethostname()
#   returns a string containing the hostname of the
#   machine where the Python interpreter is currently
#   executing.
# API: getfqdn()
#   returns a fully qualified domain name for name.
host_name = socket.gethostname()
print('host_name:', host_name)
host_ip = socket.gethostbyname(host_name)
host_port = 8181
print(host_ip, ':', host_port)

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

def cal(s):
       
        def update(operation, num):
            if operation == '+':
                stack.append(num)
            elif operation == '-':
                stack.append(-num)
            elif operation == '*':
                stack.append(stack.pop() * num)
            elif operation == '/':
                stack.append(stack.pop() / num)
        
        stack = []
        num, operation = 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ['+', '-', '*', '/', ')']:
                update(operation, num)
                if s[i] == ')':
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop() 
                    operation = stack.pop()
                    update(operation, num)
                num, operation = 0, s[i]
            elif s[i] == '(':
                stack.append(operation)
                num, operation = 0, '+'
        update(operation, num)
        res = int (sum(stack))
        return (str) (res)

def helper(message):
    res = b''
    i = 2;
    two = message[0:i]
    res += two
    follow = struct.unpack('>h', two)[0];
    
    while(follow > 0):
        size = struct.unpack('>h',message[i : i + 2])[0]
        express = message[i+2 : i + 2 + size]
        s = express.decode('utf-8');
        
        temp = cal(s)
        parse = temp.encode('utf-8');
        length = struct.pack('>h', len(parse))
        res += length + parse
        i += 2 + size
        follow -= 1

    print(res)
    return res;
    

# Bind to server IP and port number.
#
# API: bind(address)
#   Bind the socke to address.
s.bind((host_ip, host_port))

# Listen allow 5 pending connects.
#
# API: listen(backlog)
#   Listen for connections made to the socket. The
#   backlog argument specifies the maximum number
#   of queued connections
s.listen(5)

print('\nServer started. Waiting for connection...\n')

# Listen until process is killed.
#
# API: accept()
#   Accept an incoming connection. The return value
#   is a pair (conn, address) where conn is a new socket
#   object usable to send and receive data on the
#   connection, and address is the address bound to the
#   socket on the other end of the connection.
bufsize = 16


def handler(conn):
    message = b''
    while True:
        data = conn.recv(bufsize)
        
        print('Server received:', data)
        #conn.sendall(data)
        message += data
        if len(data) < 16:
            print("break")
            break
    print(message)
    res = helper(message);
    conn.sendall(res)
    conn.close()

while True:
    # Wait for next client connect.
    conn, addr = s.accept()
    print('Server connected by', addr)
    _thread.start_new(handler, (conn, ))
    # Read next line on client socket. Send a reply line to the client
    # until EOF when socket closed.
    
        
    # Close TCP connection.
    




