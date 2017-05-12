class Plugins:
        # Initialize variables
        def __init__(self, new_server, new_channel, new_nickname, new_password, new_socket):
                self.channel = new_channel
                self.server = new_server
                self.nickname = new_nickname
                self.password = new_password
                self.irc_socket = new_socket
        
        # Sends message to specified channel with given socket
        def send_message(self, irc_socket, destination, message):
                irc_socket.send("PRIVMSG %s :%s\r\n" % (destination, message))
        
        # Sends an action e.g. "bot raises his hand"
        def send_action(self, irc_socket, destination, message):
                irc_socket.send("PRIVMSG %s :\x01ACTION%s\x01\r\n" % (destination, message))
        
        # Joins new channel
        def join_channel(self, irc_socket, destination):
                irc_socket.send("JOIN %s\r\n" % destination)
        
        # Leaves given channel
        def leave_channel(self, irc_socket, destination, leave_message):
                irc_socket.send("PART %s %s\r\n" % (destination, leave_message))
        
        # If statements for determining how to respond
        # pongs when pinged and other commands are explained below
        def plugin_statements(self, irc_socket, incoming_msg):
                # Sends pong when pinged by server
                if incoming_msg.startswith("PING"):
                        irc_socket.send("PONG %s" % incoming_msg[5:])
                
                # Joins the first channel after getting correct permissions from server
                elif "001" in incoming_msg:
                        self.send_message(irc_socket, "NickServ", "identify %s %s" % (self.nickname, self.password))
                        irc_socket.send("JOIN %s\r\n" % self.channel)
                
                # Gives the bot's bio
                elif "|bio" in incoming_msg:
                        self.send_message(irc_socket, self.channel, "created by Ryan; type |help for other commands.")
                
                # Lists all bot commands
                elif "|help" in incoming_msg:
                        self.send_message(irc_socket, self.channel, "Current commands: |bio |join |kill |slap")

                # Slaps the user which calls the command (old irc joke)
                elif "|slap" in incoming_msg:
                        self.send_message(irc_socket, self.channel, "slaps %s with a large trout" % incoming_msg.split("!")[0][1:])

                # Handles user telling bot to join another channel
                elif "|join" in incoming_msg:
                        new_channel = incoming_msg[(incoming_msg.index("|join ")+6):]
                        self.join_channel(irc_socket, new_channel)

                # this kills the bot :(
                # Closes the socket which is supposedly the proper way of finishing off a socket
                elif "|kill" in incoming_msg:
                        self.irc_socket.shutdown()
                        self.irc_socket.close()
