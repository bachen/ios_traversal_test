#-*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from xml.dom.minidom import parse
import xml.dom.minidom


def get_config(filename='./config.xml'):
	DOMTree = parse(filename)
	Data = DOMTree.documentElement
	device_number = 1
	ios_version = 1
	bundle_id = 1
	device_type = 1
	level = 1
	return device_number, ios_version, bundle_id, device_type, level
