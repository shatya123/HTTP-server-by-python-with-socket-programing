Hello Guys!

This is http server which is written on python language.
this htt server is written through scoket program.

What does this program do?

So first this program open socket on 127.0.0.1 (localhost) on ip and 989 on port, You can change it.
Now you should to open browser or other client network software
Enter URL localhost:989 or 127.0.0.1 
Now you will be able to see html code which return by my server


How its work, what i wrote on code

So first we need to import socket package 
now i created ip variable for assign ip address you can also get by input through user
now i created port variable for assign port number you can also get by input through user
call socket function which will you return an object of socket
blind the ip and port
listen port through object of socket which is return by socket function 
after connected successfully send http header and html by send.object_of_connected_client


What is http headers

http header is set of code and rules which pretend that you are actual server.
You can also modify it.
if this is not in correct way then browser will not display anything.

