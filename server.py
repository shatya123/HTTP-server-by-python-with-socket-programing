import socket
ip="127.0.0.1"
port=989
com=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
com.bind((ip,port))
com.listen(5)
print 'Server Started'
(client,(cip,cport))=com.accept()
print ' Connected ' + str(cip),str(cport)
t = "HTTPS/1.1 200 OK\r\nContent-Length: 1024\r\n Content-Type: text/html\r\n\r\n <html><h1>shatya<h6>shatya<marquee><h1>shatyab</marquee></html>";
client.send(bytes(t))


print 'through clinet =>   '+client.recv(99999)
com.close()

