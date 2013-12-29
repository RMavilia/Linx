import socket
from main import main

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
main()