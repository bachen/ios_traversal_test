# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from util.iosutil import remotedriver
from time import sleep
from util.analysize_nodes import find_nodes
from util.analysize_nodes import get_nodes_config
from util.analysize_nodes import get_window_first_8_elements
from hashlib import md5


def dfs_search(dr, depth):
	# type of object is list: store window ids, each of them, their nodes had totally been traversed.
	exist_pages = []
	# type of object is list: store window ids which wait to traverse, and length <= depth.
	pages_stack = []
	# type of object is dict: key is window id, and type of value is list, which store the node on this page
	# that not yet click or input.
	nodes_stack = {}
	# initialize first page of app
	xml_res = dr.page_source
	current_window_id = create_current_window_id(xml_res)
	pages_stack.append(current_window_id)
	nodes = get_current_page_all_nodes(xml_res)
	nodes_stack[current_window_id] = nodes
	# start traverse app
	try:
		while pages_stack is not []:
			xml_res = dr.page_source
			current_window_id = create_current_window_id(xml_res)
			if current_window_id not in pages_stack
		test_result = True
	except:
		test_result = False
	finally:
		return test_result


def create_current_window_id(xml_res):
	window_string = get_window_first_8_elements(xml_res.encode('utf8'))
	window_id = create_md5(window_string.encode('utf8'))
	return window_id


def create_md5(window):
	m = md5()
	m.update(window)
	return m.hexdigest()


def get_current_page_all_nodes(xml_res):
	# get all nodes in current page
	click_config, input_config = get_nodes_config(filename='./node.xml')
	click_nodes, input_nodes = find_nodes(
		xml_res=xml_res.encode('utf8'),
		click_config=click_config,
		input_config=input_config
	)
	return click_nodes, input_nodes


if __name__ == '__main__':
	driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
	sleep(10)
	w_id = create_current_window_id(driver)
	sleep(10)
	driver.quit()
	print w_id
