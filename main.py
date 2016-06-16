# -*-coding:utf-8-*=
from ios import remotedriver
from analysize_config_xml import get_config
from analysize_config_xml import get_device_number
from analysize_config_xml import get_udid
from analysize_config_xml import get_ipa_path
from analysize_config_xml import get_level
from controller import startup_appium
from controller import shutdown_appium
from controller import cleansession
from installer import install
from traversal import traversal
import multiprocessing
from time import sleep


# get device number
device_number = get_device_number(filename='./config.xml')
# get .ipa file path
path = get_ipa_path(filename='./config.xml')
# get traversal level
level = get_level(filename='./config.xml')

# start install and traversal test
for i in xrange(0, device_number, 1):
    # clean session before new test, make sure no old appium session occupied.
    cleansession()
    sleep(10)
    try:
        # according to device number, get device args from config.xml
        udid = get_udid(filename='./config.xml', device_number=i)
        device_name, ios_version, bundle_id, device_type = get_config(filename='./config.xml', device_number=i)

        # remove old version, and install new version app
        install(udid=udid, bundle_id=bundle_id, path=path)
        sleep(10)

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
        traversal(dr=driver, level=level)

        # quit driver
        driver.quit()
        sleep(20)

        # shutdown appium
        shutdown_appium(startup)
    except:
        # when exception happens, clean appium session
        cleansession()



