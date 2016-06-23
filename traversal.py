# -*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from ios import remotedriver
from time import sleep
from analysize_nodes import find_nodes
from analysize_nodes import get_nodes_config
from analysize_nodes import get_window_first_8_elements
from hashlib import md5


def traversal(dr, level):
    res = 0
    return res


def create_current_window_id(dr):
    xml_res = dr.page_source
    window_string = get_window_first_8_elements(xml_res)
    window_id = md5(window_string)
    return window_id


def md5(window):
    m = md5()
    m.update(window)
    return m.hexdegist()


def get_current_page_all_nodes(dr):
    # get all nodes in current page
    xml_res = dr.page_source
    click_config, input_config = get_nodes_config(filename='./node.xml')
    click_nodes, input_nodes = find_nodes(xml_res=xml_res.encode('utf8'), click_config=click_config, input_config=input_config)
    return click_nodes, input_nodes


if __name__ == '__main__':
    driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
    sleep(10)
    res = get_current_page_all_nodes(driver)
    sleep(10)
    driver.quit()
    print res
