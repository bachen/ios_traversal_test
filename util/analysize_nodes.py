# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from xml.dom.minidom import parseString
from xml.dom.minidom import parse


def find_nodes(xml_res, click_config, input_config, black_config):
	xml_doc = parseString(xml_res)
	root = xml_doc.documentElement
	click_nodes = []
	# get click enable elements:
	for config in click_config:
		click_nodes = click_nodes + xml_2_xpath(root, config, black_config)
	# get input enable elements:
	input_nodes = []
	for config in input_config:
		input_nodes = input_nodes + xml_2_xpath(root, config, black_config)
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
	black_configs = root.getElementsByTagName('blacklist')
	blacks = black_configs[0].getElementsByTagName('class')
	black_config = []
	for black in blacks:
		black_config.append(black.firstChild.data)
	return click_config, input_config, black_config


def xml_2_xpath(root, element_type, black_config):
	uia_elements = root.getElementsByTagName(element_type)
	# elements collect all nodes' xpath which enabled = true and visible = true
	elements = []
	for element in uia_elements:
		if element.getAttribute('enabled') == "true" and element.getAttribute('name'):
			# element_path is raw path get from xml object, such as '/0/0/1/2'
			element_path = element.getAttribute('path').split('/')
			element_xpath = '/' + element.nodeName + '[@name="' + element.getAttribute('name') + '"]'
			element = element.parentNode
			element_path.pop()
			while element_path[-1] != '':
				element_xpath = '/' + element.nodeName + element_xpath
				element = element.parentNode
				element_path.pop()
			# //UIAAplication/...
			element_xpath = '/' + element_xpath
			flag = True
			for black in black_config:
				if black in element_xpath:
					flag = False
					break
			if flag:
				# do not add duplicate xpath
				if element_xpath not in elements:
					elements.append(element_xpath)
	return elements


def get_window_8_elements(xml_res):
	xml_doc = parseString(xml_res)
	root = xml_doc.documentElement
	button_elements = root.getElementsByTagName('UIAButton')
	collection_elements = root.getElementsByTagName('UIACollectionCell')
	window_string = ''
	if len(collection_elements) > 0:
		for count in xrange(0,1,1):
			window_string += collection_elements[count].getAttribute('name')
	if len(button_elements) > 9:
		for count in xrange(1, 9, 1):
			window_string += button_elements[count].getAttribute('name')
	else:
		for element in button_elements:
			window_string = window_string + element.getAttribute('name')
	return window_string


if __name__ == '__main__':
	pass
