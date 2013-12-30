class PluginsClass:
	def __init__(self,newServer,newChannel,newNickname,newPassword,newSocket):
		self.channel=newChannel
		self.server=newServer
		self.nickname=newNickname
		self.password=newPassword
		self.ircsocket=newSocket
	def sendMessage(self,ircsocket,newChannel,message):
		ircsocket.send("PRIVMSG "+newChannel+" :"+message+"\r\n")
	def joinChannel(self,ircsocket,newChannel):
		ircsocket.send("JOIN " + newChannel+"\r\n")
	def leaveChannel(self,ircsocket,newChannel,leaveMessage):
		ircsocket.send("PART "+newChannel+" "+leaveMessage+"\r\n")
	def pluginStatements(self,ircsocket,incomingMsg):
		if incomingMsg.find('PING') != -1: #If PING is Found in the Data
			ircsocket.send('PONG '+incomingMsg.strip("PING "))
		if "376" in incomingMsg:
			ircsocket.send("JOIN " + self.channel+"\r\n")
		if "366" in incomingMsg:
			ircsocket.send("PRIVMSG NickServ :identify "+self.nickname+" "+self.password+"\r\n")
		if "licks" in incomingMsg:
			ircsocket.send("PRIVMSG "+self.channel+" :STOP LICKING THE NICE KITTY!\r\n")
		if "#bio" in incomingMsg:
			self.sendMessage("the lick bot.")
		if "#join" in incomingMsg:
			newChannel=incomingMsg[(incomingMsg.index("#join ")+6):]
			self.joinChannel(ircsocket,newChannel)
		if "#kill" in incomingMsg:
			loop=False
		if "#YOLO" in incomingMsg:
			self.sendMessage(ircsocket,incomingMsg.split()[2],"FUCK IT! IM OUTIE DOE")
			self.leaveChannel(ircsocket,incomingMsg.split()[2], "Said fuck it, yolo.")