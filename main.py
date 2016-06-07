#-*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from appium import webdriver
from time import sleep
from ios import remotedriver
from analysize_xml import get_config
from traversal import

# according to device number, get device args from config.xml
ios_version, bundle_id, device_number, device_type, level = get_config(filename='./config.xml')

for i in xrange(0, device_number, 1):
	# according to device args, create driver object
	driver = remotedriver(bundle_id=bundle_id, device_type=device_type, ios_version=ios_version)
	# start to traversal app
	# traversal: step 1 get current page source as xml
	# traversal: step 2 discover node which could be clicked
	# traversal: step 3 decide the sort to traversal all node


