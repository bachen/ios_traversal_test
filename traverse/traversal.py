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
from util.analysize_nodes import get_window_8_elements
from hashlib import md5
from appium.webdriver import WebElement


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
	xml_res = dr.page_source
	current_window_id = create_current_window_id(xml_res)
	pages_stack.append(current_window_id)
	click_nodes, input_nodes = get_current_page_all_nodes(xml_res)
	first_page_plus = [
		'//UIAApplication/UIAWindow/UIATabBar/UIAElement[@name="我"]',
		'//UIAApplication/UIAWindow/UIATabBar/UIAElement[@name="下载听"]',
		'//UIAApplication/UIAWindow/UIATabBar/UIAElement[@name="定制听"]',
		'//UIAApplication/UIAWindow/UIATabBar/UIAElement[@name="全局播放器"]'
		]
	click_nodes_stack[current_window_id] = first_page_plus + click_nodes
	input_nodes_stack[current_window_id] = input_nodes
	# start traverse app
	while pages_stack is not []:
		pre_page = pages_stack[-1]
		print pre_page
		if click_nodes_stack[pre_page]:
			# xpath: //UIAApplication/UIAWindow/UIAButton[contains('name','search')]
			tmp_click_node = click_nodes_stack[pre_page].pop()
			print tmp_click_node
			# next node
			# print click_nodes_stack[pre_page][-1]
			if isinstance(tmp_click_node, WebElement):
				click(tmp_click_node)
				xml_res = dr.page_source
			else:
				ems = finds(dr, tmp_click_node)
				length_of_ems = len(ems)
				if length_of_ems == 1:
					# print ems[0]
					click(ems[0])
					xml_res = dr.page_source
				elif length_of_ems > 1:
					# print ems[0]
					click(ems[0])
					xml_res = dr.page_source
					for i in xrange(1, length_of_ems, 1):
						click_nodes_stack[pre_page].append(ems[i])
			current_window_id = create_current_window_id(xml_res)
			if current_window_id == pre_page:
				continue
		elif input_nodes_stack[pre_page]:
			tmp_input_node = input_nodes_stack[pre_page].pop()
			if isinstance(tmp_input_node, WebElement):
				input(tmp_input_node, 'test')
				xml_res = dr.page_source
			else:
				ems = finds(dr, tmp_input_node)
				length_of_ems = len(ems)
				if length_of_ems == 1:
					input(ems[0], 'test')
					xml_res = dr.page_source
				else:
					input(ems[0])
					xml_res = dr.page_source
					for i in xrange(1, length_of_ems, 1):
						input_nodes_stack[pre_page].append(ems[i])
			current_window_id = create_current_window_id(xml_res)
			# after input and click, still on the same page
			if current_window_id == pre_page:
				continue
		else:
			# no more nodes which not click or input on this page, this page can be pop to exist_pages.
			exist_pages.append(pages_stack.pop())
			back(dr)
		# -----start to judge new page, and decide whether add it to pages_stack----- #
		# after click or input, is on a different page
		while len(pages_stack) > depth:
			back(dr)
			pages_stack.pop()
			print 'reach the depth'
		xml_res = dr.page_source
		current_window_id = create_current_window_id(xml_res)
		# print current_window_id
		# make sure on a new page, if the same page, do not add to pages_stack, and continue to traverse this page.
		if pages_stack[-1] == current_window_id:
			continue
		# if nodes of this page has been all traversed, do not add to pages_stack
		while current_window_id in exist_pages:
			back(dr)
			xml_res = dr.page_source
			current_window_id = create_current_window_id(xml_res)
		if current_window_id not in pages_stack and current_window_id not in exist_pages:
			pages_stack.append(current_window_id)
			click_nodes, input_nodes = get_current_page_all_nodes(xml_res)
			click_nodes_stack[current_window_id] = click_nodes
			input_nodes_stack[current_window_id] = input_nodes
		if current_window_id in pages_stack and current_window_id not in exist_pages:
			pages_stack.append(current_window_id)


def create_current_window_id(xml_res):
	window_string = get_window_8_elements(xml_res.encode('utf8'))
	window_id = create_md5(window_string.encode('utf8'))
	return window_id


def create_md5(window):
	m = md5()
	m.update(window)
	return m.hexdigest()


def get_current_page_all_nodes(xml_res):
	# get all nodes in current page
	click_config, input_config, black_config = get_nodes_config(filename='../config/node.xml')
	click_nodes, input_nodes = find_nodes(
		xml_res=xml_res.encode('utf8'),
		click_config=click_config,
		input_config=input_config,
		black_config=black_config
	)
	return click_nodes, input_nodes


if __name__ == '__main__':
	driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
	sleep(30)
	dfs_search(driver, 10)
	sleep(10)
	driver.quit()
