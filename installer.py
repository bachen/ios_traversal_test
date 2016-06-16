# -*-coding:utf-8-*=
from time import sleep
from os import system


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
		sleep(60)
		print 'complete install app.'
	except:
		print 'failed to install app'


if __name__=='__main__':
	install('2e58ffd37a53a8a3920f51b4ab73fe5e6a363d22', 'com.gemd.iting', '/Users/jenkins/.jenkins/jobs/ios_build_master/workspace/build/ting-*.ipa')
