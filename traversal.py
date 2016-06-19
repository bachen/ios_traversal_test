# -*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from ios import remotedriver
from time import sleep
from analysize_nodes import find_nodes


def traversal(dr, level):
    res = 0
    return res


def get_current_page_all_nodes(dr):
    # get all nodes in current page
    xml_res = dr.page_source
    enable_nodes = find_nodes(xml_res)
    return enable_nodes


if __name__ == '__main__':
    driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
    sleep(10)
    res = get_current_page_all_nodes(driver)
    driver.quit()
    print res
