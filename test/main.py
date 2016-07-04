# -*-coding:utf-8-*=
import multiprocessing
from time import sleep

from device.controller import cleansession
from device.controller import shutdown_appium
from device.controller import startup_appium
from util.iosutil import remotedriver
from traverse.traversal import dfs_search

from config.analysize_config_xml import get_config
from config.analysize_config_xml import get_device_number
from config.analysize_config_xml import get_level
from config.analysize_config_xml import get_udid

# get device number
config_file_path = '../config/config.xml'

device_number = get_device_number(filename=config_file_path)

# get traversal level
level = get_level(filename=config_file_path)
print level,device_number
# start traversal test
for i in xrange(0, device_number, 1):
    # clean session before new test, make sure no old appium session occupied.
    cleansession()
    sleep(10)
    try:
        # according to device number, get device args from config.xml
        udid = get_udid(filename=config_file_path, device_number=i)
        device_name, ios_version, bundle_id, device_type = get_config(filename=config_file_path, device_number=i)

        # start up appium
        startup = multiprocessing.Process(target=startup_appium, args=(
            udid, device_name, bundle_id, ios_version))
        startup.start()
        sleep(60)

        # according to device args, create driver object
        driver = remotedriver(bundle_id=bundle_id, device_type=device_type, ios_version=ios_version)
        print "good job %s" % (i,)
        sleep(10)

        # start to traversal app
        # traversal: step 1 get current page source as xml
        # traversal: step 2 discover node which could be clicked
        # traversal: step 3 decide the sort to traversal all node
        res = dfs_search(dr=driver, depth=level)
        print res
        # quit driver
        print 'ready to quit...'
        driver.quit()
        sleep(20)

        # shutdown appium
        shutdown_appium(startup)
    except:
        # when exception happens, clean appium session
        cleansession()



