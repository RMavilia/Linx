
def getInfo(newServer,newChannel,newNickname,newSocket):
	ircsocket=newSocket
	channel=newChannel
	server=newServer
	nickname=newNickname
def sendMessage(ircsocket,newChannel,message):
	ircsocket.send("PRIVMSG "+newChannel+" :"+message+"\r\n")
def joinChannel(ircsocket,newChannel):
	ircsocket.send("JOIN " + newChannel+"\r\n")
def leaveChannel(ircsocket,newChannel,leaveMessage):
	ircsocket.send("PART "+newChannel+" "+leaveMessage+"\r\n")
def pluginStatements(ircsocket,incomingMsg):
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
		joinChannel(ircsocket,newChannel)
	if "#kill" in incomingMsg:
		loop=False
	if "#YOLO" in incomingMsg:
		sendMessage(ircsocket,incomingMsg.split()[2],"FUCK IT! IM OUTIE DOE")
		leaveChannel(ircsocket,incomingMsg.split()[2], "Said fuck it, yolo.")