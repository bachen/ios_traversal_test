# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from ios import remotedriver
from time import sleep
from analysize_nodes import find_nodes
from analysize_nodes import get_nodes_config
from xml.dom.minidom import parseString
import hashlib


def traversal(dr, level):
	res = 0
	return res


def get_current_page_all_nodes(dr):
	# get all nodes in current page
	xml_res = dr.page_source
	click_config, input_config = get_nodes_config(filename='./node.xml')
	click_nodes, input_nodes = find_nodes(
		xml_res=xml_res.encode("utf8"),
		click_config=click_config,
		input_config=input_config
	)
	return click_nodes, input_nodes


def get_current_window_id(dr):
	xml_doc = dr.page_source.encode("utf8")
	root = parseString(xml_doc)


def md5(window_mark):
	m = hashlib.md5()
	m.update(window_mark)
	return m.hexdigest()



def find_nodes(xml_res, click_config, input_config):
	xml_doc = parseString(xml_res)
	root = xml_doc.documentElement
	nodes = []
	# get click enable elements:
	if 'UIAImage' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIAImage')
	if 'UIAButton' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIAButton')
	if 'UIASwitch' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIASwitch')
	if 'UIATableCell' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIATableCell')
	if 'UIAPickerWheel' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIAPickerWheel')
	if 'UIACollectionCell' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIACollectionCell')
	if 'UIAStaticText' in click_config:
		click_nodes = nodes + xml_2_xpath(root, 'UIAStaticText')

	# get input enable elements:
	input_nodes = []
	if 'UIATextField' in input_config:
		input_nodes = input_nodes + xml_2_xpath(root, 'UIATextField')
	if 'UIASearchBar' in input_config:
		input_nodes = input_nodes + xml_2_xpath(root, 'UIASearchBar')
	if 'UIASecureTextField' in input_config:
		input_nodes = input_nodes + xml_2_xpath(root, 'UIASecureTextField')

	return click_nodes, input_nodes


def get_nodes_config(filename='./node.xml'):
	xml_doc = parse(filename)
	root = xml_doc.documentElement
	# get click controllers
	click_configs = root.getElementsByTagName('click')
	clicks = click_configs[0].getElementsByTagName('class')
	click_config = []
	for click in clicks:
		click_config.append(click.firstChild.data)
	# get input controllers
	input_configs = root.getElementsByTagName('input')
	inputs = input_configs[0].getElementsByTagName('class')
	input_config = []
	for input_i in inputs:
		input_config.append(input_i.firstChild.data)
	return click_config, input_config


def xml_2_xpath(root):
	uia_windows = root.getElementsByTagName('UIAWindow')
	# elements collect all nodes' xpath which enabled = true and visible = true
	elements = []
	uia_windows[0]
	return elements


if __name__ == '__main__':
	driver = remotedriver(bundle_id='com.gemd.iting', device_type='iPhone 5', ios_version='9.3.2')
	sleep(10)
	res = get_current_page_all_nodes(driver)
	sleep(10)
	driver.quit()
	print res
