import socket


server = "irc.awfulnet.org" #Server
channel = "#fitness" #Channel
nickname = "Linx" #Bot nickname
password = raw_input("What is your password? ")
port = 6667
ircsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsocket.connect((server,port))
ircsocket.send("NICK "+ nickname+"\r\n")
ircsocket.send("USER "+nickname+" 0 * "+ ":RYAN"+"\r\n")
archiveFile = open("archive.txt", 'a+')
def sendMessage(newChannel,message):
	ircsocket.send("PRIVMSG "+newChannel+" :"+message+"\r\n")
def joinChannel(newChannel):
	ircsocket.send("JOIN " + newChannel+"\r\n")
def leaveChannel(newChannel,leaveMessage):
	ircsocket.send("PART "+newChannel+" "+leaveMessage+"\r\n")
loop=True
while loop:
	incomingMsg = ircsocket.recv (4096) #Make Data the Receive Buffer
	print incomingMsg #Print the Data to the console(For debug purposes)
	archiveFile.write(incomingMsg)#log it in the archive txt doc
	if incomingMsg.find('PING') != -1: #If PING is Found in the Data
		ircsocket.send('PONG '+incomingMsg.strip("PING "))
	if "376" in incomingMsg:
		ircsocket.send("JOIN " + channel+"\r\n")
	if "366" in incomingMsg:
		ircsocket.send("PRIVMSG NickServ :identify "+nickname+" "+password+"\r\n")
	if "licks" in incomingMsg:
		ircsocket.send("PRIVMSG "+channel+" :STOP LICKING EACH OTHER!\r\n")
	if "#bio" in incomingMsg:
		sendMessage("the lick bot.")
	if "#join" in incomingMsg:
		newChannel=incomingMsg[(incomingMsg.index("#join ")+6):]
		joinChannel(newChannel)
	if "#kill" in incomingMsg:
		loop=False
	if "#YOLO" in incomingMsg:
		print(incomingMsg.split()[2])
		sendMessage(incomingMsg.split()[2],"FUCK IT! IM OUTIE DOE")
		leaveChannel(incomingMsg.split()[2], "Said fuck it, yolo.")