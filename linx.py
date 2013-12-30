import socket
import plugins
server = "squid.awfulnet.org" #Server
channel = "#fitness" #Channel
nickname = "Linx" #Bot nickname
password = raw_input("What is your password? ")
port = 6667
ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myPlugins=plugins.PluginsClass(server,channel,nickname,ircsocket)
ircsocket.connect((server,port))
ircsocket.send("NICK "+ nickname+"\r\n")
ircsocket.send("USER "+nickname+" 0 * "+ ":RYAN"+"\r\n")
archiveFile = open("archive.txt", 'a+')
loop=True
while loop:
	incomingMsg = ircsocket.recv (4096) #Make Data the Receive Buffer
	print incomingMsg #Print the Data to the console(For debug purposes)
	archiveFile.write(incomingMsg)#log it in the archive txt doc
	myPlugins.pluginStatements(ircsocket,incomingMsg)