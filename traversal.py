# -*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from ios import remotedriver
from time import sleep
from analysize_nodes import find_nodes
from analysize_nodes import get_nodes_config


def traversal(dr, level):
    res = 0
    return res


def get_current_page_all_nodes(dr):
    # get all nodes in current page
    xml_res = dr.page_source
    print xml_res
    click_config, input_config = get_nodes_config(filename='./node.xml')
    enable_nodes = find_nodes(xml_res=unicode(xml_res), click_config=click_config, input_config=input_config)
    return enable_nodes


if __name__ == '__main__':
    driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
    sleep(10)
    res = get_current_page_all_nodes(driver)
    sleep(10)
    driver.quit()
    print res
