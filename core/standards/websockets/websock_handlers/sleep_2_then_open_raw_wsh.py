#!/usr/bin/python

from mod_pywebsocket import msgutil
import time
import urllib


def web_socket_do_extra_handshake(request):
	msgutil._write(request, 'x')
	time.sleep(2)

def web_socket_transfer_data(request):
	msgutil._write(request, urllib.unquote(request.ws_location.split('?', 1)[1]).decode("string-escape"))
	time.sleep(2)
