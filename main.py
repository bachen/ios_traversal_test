# -*-coding:utf-8-*=
from time import sleep
from ios import remotedriver
from analysize_config_xml import get_config
from analysize_config_xml import get_device_number
from analysize_config_xml import get_udid

# get device number
device_number = get_device_number(filename='./config.xml')

for i in xrange(0, device_number, 1):
	# according to device number, get device args from config.xml
	udid = get_udid(filename='./config.xml', device_number=i)
	ios_version, bundle_id, device_type, level = get_config(filename='./config.xml', device_number=i)
	# start up appium program
	# according to device args, create driver object

	driver = remotedriver(bundle_id=bundle_id, device_type=device_type, ios_version=ios_version)

	# start to traversal app
	# traversal: step 1 get current page source as xml
	# traversal: step 2 discover node which could be clicked
	# traversal: step 3 decide the sort to traversal all node
	driver.quit()

