# -*-coding:utf-8-*=
from time import sleep
from os import system
import multiprocessing


'''
example:

import multiprocessing
import time

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"


if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))

    p1.start()
    p2.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
'''


def startup_appium(udid=None, version=None, bundle_id=None, device_name=None):
	cmd = '/usr/local/bin/node /usr/local/bin/appium --command-timeout "15000" --session-override --debug-log-spacing --log-timestamp --platform-version "' + version + '" --platform-name "iOS" --app "' + bundle_id + '" -U "' + udid + '" --device-name "' + device_name + '"'
	print cmd
	system(cmd)
	sleep(10)


def shutdown_appium(process):
	if process.is_alive():
		process.terminate()


def cleansession():
	cmd = 'pkill -9 node'
	system(cmd)
	sleep(5)


if __name__ == "__main__":
	startup = multiprocessing.Process(target=startup_appium, args=(
		'2e58ffd37a53a8a3920f51b4ab73fe5e6a363d22', 'iPhone 5', 'com.gemd.iting', '9.3.2'))
	startup.start()
	sleep(120)
	print 'start up appium for 10s.'
	sleep(20)
	shutdown_appium(startup)
	sleep(10)
