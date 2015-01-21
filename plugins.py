class Plugins:
	def __init__(self, new_server, new_channel, new_nickname, new_password, new_socket):
		self.channel = new_channel
		self.server = new_server
		self.nickname = new_nickname
		self.password = new_password
		self.irc_socket = new_socket
		
	def send_message(self, irc_socket, new_channel, message):
		irc_socket.send("PRIVMSG "+new_channel+" :"+message+"\r\n")
		
	def send_action(self, irc_socket, new_channel, message):
		irc_socket.send("ACTION "+new_channel+" :"+message+"\r\n")
		
	def join_channel(self, irc_socket, new_channel):
		irc_socket.send("JOIN "+new_channel+"\r\ning")
		
	def leave_channel(self, irc_socket, new_channel, leaveMessage):
		irc_socket.send("PART "+new_channel+" "+leaveMessage+"\r\n")
		
	def plugin_statements(self, irc_socket,incoming_msg):
		if incoming_msg.startswith("PING") #If message is a PING message send a PONG in response
			irc_socket.send("PONG"+incoming_msg[4:])
			
		if "001" in incoming_msg:
			self.send_message(irc_socket, "NickServ", "identify "+self.nickname+" "+self.password)
			irc_socket.send("JOIN "+self.channel+"\r\n")
			
		if "licks" in incoming_msg:
			self.send_message(irc_socket, current_channel, "that was hot.")
			
		if "|bio" in incoming_msg:
			self.send_message(irc_socket, current_channel, "created by Mav; type |help for other commands.")
			
		if "|help" in incoming_msg:
			self.send_message(irc_socket, current_channel, "Current commands: |help DICKS (fuck you im working on it)")
			
		if "|join" in incoming_msg:
			new_channel=incoming_msg[(incoming_msg.index("|join ")+6):]
			self.join_channel(irc_socket, new_channel)
		
		if "|kill" in incoming_msg:
			loop=False
			
		if "|slap" in incoming_msg:
			self.send_action(irc_socket, self.channel, "slaps "+incoming_msg.split()[3]+" with a large trout")
			
		if "|YOLO" in incoming_msg:
			self.send_message(irc_socket, incoming_msg.split()[2], "FUCK IT! IM OUTIE DOE")
			self.leave_channel(irc_socket, incoming_msg.split()[2], "Said fuck it, yolo.")
