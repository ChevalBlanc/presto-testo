#!/usr/bin/python

from mod_pywebsocket import msgutil
import urllib

import time

def web_socket_do_extra_handshake(request):
	pass

def web_socket_transfer_data(request):
	time.sleep(2)
	msgutil._write(request, urllib.unquote(request.ws_location.split('?', 1)[1]).decode("string-escape"))
