#!/usr/bin/python

from mod_pywebsocket import msgutil
import time

def web_socket_do_extra_handshake(request):
	pass  # Always accept.

def web_socket_transfer_data(request):
	time.sleep(3)
	msgutil.send_message(request, "line")
