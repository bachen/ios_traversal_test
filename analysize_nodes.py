# -*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from xml.dom.minidom import parseString
from xml.dom.minidom import parse


def find_nodes(xml_res, click_config, input_config):
    xml_doc= parseString(xml_res)
    root = xml_doc.documentElement
    nodes = []
    # get click enable elements:
    if 'UIAImage' in click_config:
        nodes = xml_2_xpath(root, 'UIAImage')
    '''
    if 'UIAButton' in click_config:
        UIAButtons = xml_2_xpath(root, 'UIAButton')
    if 'UIASwitch' in click_config:
        UIASwitchs = xml_2_xpath(root, 'UIASwitch')
    if 'UIATableCell' in click_config:
        UIATableCells = xml_2_xpath(root, 'UIATableCell')
    if 'UIAPickerWheel' in click_config:
        UIAPickerWheels = xml_2_xpath(root, 'UIAPickerWheel')
    if 'UIACollectionCell' in click_config:
        UIACollectionCells = xml_2_xpath(root, 'UIACollectionCell')
    if 'UIAStaticText' in click_config:
        UIAStaticTexts = xml_2_xpath(root, 'UIAStaticText')
    # get input enable elements:
    if 'UIATextField' in input_config:
        UIATextFields = xml_2_xpath(root, 'UIATextField')
    if 'UIASearchBar' in input_config:
        UIASearchBars = xml_2_xpath(root, 'UIASearchBar')
    if 'UIASecureTextField' in input_config:
        UIASecureTextFields = xml_2_xpath(root, 'UIASecureTextField')
    '''
    return nodes


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


def xml_2_xpath(root, element_type):
    uia_elements = root.getElementsByTagName(element_type)
    # elements collect all nodes' xpath which enabled = true and visible = true
    elements = []
    for element in uia_elements:
        if element.getAttribute('enabled') == "true" and element.getAttribute('visible') == "true":
            element_xpath = ''
            # element_path is raw path get from xml object, such as '/0/0/1/2'
            element_path = element.getAttribute('path').split('/')
            while element_path[-1] != '':
                element_xpath = '/' + element.nodeName + '[' + element_path[-1] + ']' + element_xpath
                element = element.parentNode
                element_path.pop()
            elements.append(element_xpath)
    return elements


if __name__ == '__main__':
    print get_nodes_config()
