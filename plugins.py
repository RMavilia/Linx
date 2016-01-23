class Plugins:
	def __init__(self, new_server, new_channel, new_nickname, new_password, new_socket):
		self.channel = new_channel
		self.server = new_server
		self.nickname = new_nickname
		self.password = new_password
		self.irc_socket = new_socket
		
	def send_message(self, irc_socket, destination, message):
		irc_socket.send("PRIVMSG %s :%s\r\n" % (destination, message))
		
	def send_action(self, irc_socket, destination, message):
		irc_socket.send("ACTION %s :%s\r\n" % (destination, message))
		
	def join_channel(self, irc_socket, destination):
		irc_socket.send("JOIN %s\r\n" % destination)
		
	def leave_channel(self, irc_socket, destination, leave_message):
		irc_socket.send("PART %s %s\r\n" % (destination, leave_message))
		
	def plugin_statements(self, irc_socket, incoming_msg):
		if incoming_msg.startswith("PING") #If message is a PING message send a PONG in response
			irc_socket.send("PONG %s" % incoming_msg[5:])
			
		elif "001" in incoming_msg:
			self.send_message(irc_socket, "NickServ", "identify %s %s" % (self.nickname, self.password))
			irc_socket.send("JOIN %s\r\n" % self.channel)
			
		elif "|bio" in incoming_msg:
			self.send_message(irc_socket, current_channel, "created by NAME HERE; type |help for other commands.")
			
		elif "|help" in incoming_msg:
			self.send_message(irc_socket, current_channel, "Current commands: |bio |join |kill |slap")
			
		elif "|join" in incoming_msg:
			new_channel = incoming_msg[(incoming_msg.index("|join ")+6):]
			self.join_channel(irc_socket, new_channel)
		
		elif "|kill" in incoming_msg:
			loop = False
			
		elif "|slap" in incoming_msg:
			self.send_action(irc_socket, self.channel, "slaps %s with a large trout" % incoming_msg.split()[3])
