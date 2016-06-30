# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from util.iosutil import remotedriver
from util.iosutil import click
from util.iosutil import finds
from util.iosutil import input
from util.iosutil import back
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
	click_nodes_stack = {}
	input_nodes_stack = {}
	# initialize first page of app
	count = 0
	xml_res = dr.page_source
	current_window_id = create_current_window_id(xml_res)
	pages_stack.append(current_window_id)
	click_nodes, input_nodes = get_current_page_all_nodes(xml_res)
	click_nodes_stack[current_window_id] = click_nodes
	input_nodes_stack[current_window_id] = input_nodes
	# start traverse app
	try:
		while pages_stack is not []:
			pre_page = pages_stack[-1]
			if click_nodes_stack[pre_page] is not []:
				# xpath: /UIAApplication/UIAWindow/UIAButton[contains('name','search')]
				tmp_click_node = click_nodes_stack[pre_page].pop()
				ems = finds(dr, tmp_click_node)
				length_of_ems = len(ems)
				if length_of_ems == 1:
					click(ems[0])
					xml_res = dr.page_source
				else:
					click(ems[0])
					xml_res = dr.page_source
					for i in xrange(1, length_of_ems, 1):
						click_nodes_stack[pre_page].append(ems[i].xpath)
				current_window_id = create_current_window_id(xml_res)
				if current_window_id == pre_page:
					continue
			elif input_nodes_stack[pre_page] is not []:
				tmp_input_node = input_nodes_stack[pre_page].pop()
				ems = finds(dr, tmp_input_node)
				length_of_ems = len(ems)
				if length_of_ems == 1:
					input(ems[0])
					xml_res = dr.page_source
				else:
					input(ems[0])
					xml_res = dr.page_source
					for i in xrange(1, length_of_ems, 1):
						input_nodes_stack[pre_page].append(ems[i].xpath)
				current_window_id = create_current_window_id(xml_res)
				# after inout, still on the same page
				if current_window_id == pre_page:
					continue
			else:
				# no more nodes which not click or input on this page, this page can be pop to exist_pages.
				exist_pages.append(pages_stack.pop())
				back(dr)
			# after click or input, is on a different page
			while len(pages_stack) > depth:
				back(dr)
				pages_stack.pop()
			xml_res = dr.page_source
			current_window_id = create_current_window_id(xml_res)
			# make sure on a new page, if the same page, do not add to pages_stack.
			if pages_stack[-1] == current_window_id:
				continue
			# if new page has been traversed, do not add to pages_stack
			while current_window_id in exist_pages:
				back(dr)
				xml_res = dr.page_source
				current_window_id = create_current_window_id(xml_res)

			if current_window_id not in pages_stack and current_window_id not in exist_pages:
				pages_stack.append(current_window_id)
				click_nodes, input_nodes = get_current_page_all_nodes(xml_res)
				click_nodes_stack[current_window_id] = click_nodes
				input_nodes_stack[current_window_id] = input_nodes
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
