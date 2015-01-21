import socket
import plugins
import imp
from datetime import datetime

server = "irc.subluminal.net" #Server
channel = "#bots" #Channel
nickname = "Linx" #Bot nickname
password = raw_input("What is your password? ")
port = 6667

irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_plugins = plugins.Plugins(server, channel, nickname, password, irc_socket)
irc_socket.connect((server, port))
irc_socket.send("NICK %s\r\n" % nickname)
irc_socket.send("USER %s 0 * :RYAN\r\n" % nickname)
archiveFile = open("archive.txt", 'a+')
loop = True

while loop:
	incoming_msg = irc_socket.recv(4096) #Make Data the Receive Buffer
	print incoming_msg #Print the Data to the console(For debug purposes)
	archiveFile.write("%s %s" % (str(datetime.now().strftime('%Y/%m/%d %H:%M:%S')), incoming_msg)) #Log it in the archive txt doc
	if "|reload" in incoming_msg:
		imp.reload(plugins)
		my_plugins = plugins.Plugins(server, channel, nickname, password, irc_socket)
		my_plugins.send_message(irc_socket, channel, "Plugins Reloaded")
	my_plugins.plugin_statements(irc_socket, incoming_msg)
