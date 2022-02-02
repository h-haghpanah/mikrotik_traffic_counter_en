#!/usr/bin/env python

LOG_FILE = 'youlogfile.log'
HOST, PORT = "0.0.0.0", 514


import logging
import socketserver
import time

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

class SyslogUDPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		data = bytes.decode(self.request[0].strip())
		socket = self.request[1]
		files = open('/python/mikrotik/weblog.txt', 'a')
		files.write(str(data) + "\n")
		files.close()
		print(str(data))
		#logging.info(str(data))

if __name__ == "__main__":
	try:
		server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
		server.serve_forever(poll_interval=0.5)
	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
