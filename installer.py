# -*-coding:utf-8-*=
from time import sleep
from os import system
from analysize_config_xml import get_ipa_path
from analysize_config_xml import get_config
from analysize_config_xml import get_device_number
from analysize_config_xml import get_udid


def install(udid, bundle_id, path):
	"""

	:type dr: appium - driver
	:type path: path of .ipa file
	"""
	try:
		cmd = 'ideviceinstaller --udid ' + udid + ' --uninstall ' + bundle_id
		system(cmd)
		sleep(10)
		cmd = 'ideviceinstaller --udid ' + udid + ' --install ' + path
		system(cmd)
		sleep(70)
		print 'complete install app.'
	except:
		print 'failed to install app'


if __name__ == '__main__':
	# get .ipa file path
	path = get_ipa_path(filename='./config.xml')

	# get device number
	device_number = get_device_number(filename='./config.xml')
	# according to device number, get device args from config.xml

	for i in xrange(0, device_number, 1):
		udid = get_udid(filename='./config.xml', device_number=i)
		device_name, ios_version, bundle_id, device_type = get_config(filename='./config.xml', device_number=i)

		# remove old version, and install new version app
		install(udid=udid, bundle_id=bundle_id, path=path)
