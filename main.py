def getSocket(newSocket):
	ircsocket=newSocket
def sendMessage(newChannel,message):
	ircsocket.send("PRIVMSG "+newChannel+" :"+message+"\r\n")
def joinChannel(newChannel):
	ircsocket.send("JOIN " + newChannel+"\r\n")
def leaveChannel(newChannel,leaveMessage):
	ircsocket.send("PART "+newChannel+" "+leaveMessage+"\r\n")
