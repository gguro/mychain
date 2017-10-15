import netifaces
import socket

import os
from configparser import ConfigParser

config = ConfigParser()


def get_ip_address(ifname):
	import platform
	plf = platform.system()
	if plf == 'Windows':
		return ([l for l in (
			[ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [
				[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
				 [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
	else:
		netifaces.ifaddresses(ifname)
		return netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']


def load_config_file(conf_file):
	global config

	if os.path.exists(conf_file) == False:
		raise Exception("%s file does not exist\n") % conf_file

	config.read(conf_file)


def get_config_item(section, item):
	global config

	return config.get(section, item)
