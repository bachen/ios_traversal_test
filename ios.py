#-*-coding:utf-8-*=
import os
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.append('/usr/local/lib/')
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction
import time,threading
from multiprocessing import Process
'''
--------------------
Appium API 二次封装
--------------------

remotedriver():创建driver
launch():      登录app
close():	   关闭app
install():	   安装app
remove():	   卸载app

click():		点击元素
input():		输入
hide_keyboard():隐藏键盘
tap():			轻点
find():			定位一个元素
finds():		定位一组元素
find_id():		定位一个元素
finds_id():		定位一组元素
long_press():	长按
'''
class runserver(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		os.system('/usr/local/bin/node /usr/local/bin/appium --command-timeout "7200" --debug-log-spacing --platform-version "7.1.2" --platform-name "iOS" --app "com.gemd.iting" --udid "4394a67923a9f3b8a89ae424b461f8901258fe70" --device-name "iPhone 4"')

#start appium server
def start_server():
	t1 = runserver()
	p = Process(target=t1.run)
	p.start()
	print 'start server successfully...'

def stop_server():
	os.system('pkill -9 node')
	time.sleep(10)	
	print 'stop server...'

#settings and common actions
def remotedriver(type=None,bid='com.gemd.iting'):
	if type == u'ios7.1.1':
 		desired_caps = {
			'bundleId': bid,
			'deviceName': 'iPhone',
			'platformName': 'iOS',
			'platformVersion': '7.1.1',
		}
	elif type == u'ios9.3.2':
		desired_caps = {
			'bundleId': bid,
			'deviceName': 'iPhone',
			'platformName': 'iOS',
			'platformVersion': '9.3.2',  #this para must be the same as the version set in Appium
		}
	elif type == u'ios8.4':
		desired_caps = {
			'bundleId': bid,
			'deviceName': 'iPhone',
			'platformName': 'iOS',
			'platformVersion': '8.4',
		}
	else:
		print 'Please input correct version of iOS, iOS 7.1, 8.0, 8.1 are available here'
	dr= webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
	return dr

def launch(dr):
	try:
		dr.launch_app()
	except:
		print 'failed to launch app'

def close(dr):
	try:
		dr.close_app()
	except:
		print 'failed to close app'

def install(dr,path=None):
	try:
		if dr.is_app_installed('com.xily.baijiajiangtandaquan') == False:
			dr.install_app(path)
		time.sleep(20)
	except:
		print 'failed to install app'

def remove(dr):
	try:
		if dr.is_app_installed('com.xily.baijiajiangtandaquan') == True:
			dr.remove_app('com.xily.baijiajiangtandaquan')
		time.sleep(20)
	except:
		print 'failed to remove app'	

#test actions
def click(dr,s=None,msg=None):
	try:
		em = dr.find_element_by_xpath(s)
		em.click()
	except:
		if msg:
			print '%s.' % msg

def clicku(dr,s=None):
	try:
		em = dr.find_element_by_ios_uiautomation(s)
		em.click()
	except:
		print 'failed to click element by ios uiautomation'

def input(dr,s=None,w=None):
	try:
		em = dr.find_element_by_xpath(s)
		em.set_value(w)
	except:
		print 'failed to input words'

def inputu(dr,s=None,w=None):
	try:
		em = dr.find_element_by_ios_uiautomation(s)
		em.set_value(w)
	except:
		print 'failed to input words by ios uiautomation'

#inputw()函数用于webview页面的操作
def inputw(dr,s=None,w=None):
	try:
		em = dr.find_element_by_xpath(s)
		em.send_keys(w)
	except:
		print 'failed to input words in webview'

def hide_keyboard(dr,s=None):
	try:
		em = dr.find_element_by_class_name('keyboard')
		if em.is_displayed:
			#if keyboard has 'Done', then dr.hide_keyboard('Done')
			if s:
				dr.hide_keyboard(s)
			else:
				dr.hide_keyboard()
	except:
		print 'failed to hide keyboard'

def tap(dr,x,y):
	try:
		action = TouchAction()
		action.tap(em).perform()
	except:
		print 'failed to tap element'

def find(dr,s=None):
	#native app find element method
	#判断当前元素存在时，请勿使用该方法
	try:
		em = dr.find_element_by_xpath(s)
		return em
	except:
		print 'failed to find element by xpath'

def finds(dr,s=None):
	#native app find elements method
	try:
		ems = dr.find_elements_by_xpath(s)
		return ems
	except:
		print 'failed to find elements by xpath'

def long_press(dr,s=None):
    try:
        em = dr.find_element_by_xpath(s)
        action = TouchAction(self)
        action.long_press(em).release().perform()
    except:
        print 'failed to long press element'

def drag_drop(dr,s1,s2):
	try:
		em1 = dr.find_element_by_xpath(s1)
		em2 = dr.find_element_by_xpath(s2)
		dr.drag_and_drop(em1,em2)
	except:
		print 'failed to drag and drop element'

def switch(dr,cur):
	#cur为当前所在页面名臣
	#在新页面操作完后，需要回到原页面
	cons = dr.contexts
	for con in cons:
		if con != cur:
			dr.switch_to.context(con)

def swipe(dr,x1,y1,x2,y2,t=1000):
	action=TouchAction(dr)
	action.press(x=x1,y=y1).wait(t).move_to(x=x2,y=y2).release().perform()