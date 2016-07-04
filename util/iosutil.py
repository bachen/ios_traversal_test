# -*-coding:utf-8-*=

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
sys.path.append('/usr/local/lib/')
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


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


# settings and common actions


def remotedriver(bundle_id='com.gemd.iting', device_type=None, ios_version=None):
    desired_caps = {
        'bundleId': bundle_id,
        'deviceName': device_type,
        'platformName': 'iOS',
        'platformVersion': ios_version,
    }
    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
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


# test actions


def get_page_source(dr):
    res = dr.getPageSource()
    return res


def click(em, msg=None):
    try:
        em.click()
        sleep(5)
    except:
        if msg:
            print '%s.' % msg


def inputs(dr, s=None, w=None):
    try:
        em = dr.find_element_by_xpath(s)
        em.set_value(w)
    except:
        print 'failed to input words'


def inputu(dr, s=None, w=None):
    try:
        em = dr.find_element_by_ios_uiautomation(s)
        em.set_value(w)
    except:
        print 'failed to input words by ios uiautomation'


# inputw()函数用于webview页面的操作


def input(dr, s=None, w=None):
    try:
        em = dr.find_element_by_xpath(s)
        em.send_keys(w)
    except:
        print 'failed to input words in webview'


def hide_keyboard(dr, s=None):
    try:
        em = dr.find_element_by_class_name('keyboard')
        if em.is_displayed:
            # if keyboard has 'Done', then dr.hide_keyboard('Done')
            if s:
                dr.hide_keyboard(s)
            else:
                dr.hide_keyboard()
    except:
        print 'failed to hide keyboard'


def tap(dr, x, y):
    try:
        action = TouchAction()
        action.tap(em).perform()
    except:
        print 'failed to tap element'


def find(dr, s=None):
    # native app find element method
    # 判断当前元素存在时，请勿使用该方法
    try:
        em = dr.find_element_by_xpath(s)
        return em
    except:
        print 'failed to find element by xpath'


def finds(dr, s=None):
    # native app find elements method
    try:
        ems = dr.find_elements_by_xpath(s)
        return ems
    except:
        print 'failed to find elements by xpath'


def long_press(dr, s=None):
    try:
        em = dr.find_element_by_xpath(s)
        action = TouchAction(dr)
        action.long_press(em).release().perform()
    except:
        print 'failed to long press element'


def drag_drop(dr, s1, s2):
    try:
        em1 = dr.find_element_by_xpath(s1)
        em2 = dr.find_element_by_xpath(s2)
        dr.drag_and_drop(em1, em2)
    except:
        print 'failed to drag and drop element'


def switch(dr, cur):
    # cur为当前所在页面名臣
    # 在新页面操作完后，需要回到原页面
    cons = dr.contexts
    for con in cons:
        if con != cur:
            dr.switch_to.context(con)


def swipe(dr, x1, y1, x2, y2, t=1000):
    action = TouchAction(dr)
    action.press(x=x1, y=y1).wait(t).move_to(x=x2, y=y2).release().perform()


def back(dr):
    try:
        # cancel search
        cancel_btn = dr.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[@name="取消"]')
        cancel_btn.click()
        sleep(5)
    except:
        # back btn
        dr.tap([(25, 34)])
        sleep(5)
