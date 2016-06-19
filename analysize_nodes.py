# -*-coding:utf-8-*=
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from xml.dom.minidom import parse


def find_nodes(xml_doc, filter, click_config, input_config):
    root = xml_doc.documentElement
    # get click enable elements:
    if 'UIAImage' in click_config:
        UIAImages = root.getElementsByTagName('UIAImage')
    if 'UIAButton' in click_config:
        UIAButtons = root.getElementsByTagName('UIAButton')
    if 'UIASwitch' in click_config:
        UIASwitchs = root.getElementsByTagName('UIASwitch')
    if 'UIATableCell' in click_config:
        UIATableCells = root.getElementsByTagName('UIATableCell')
    if 'UIAPickerWheel' in click_config:
        UIAPickerWheels = root.getElementsByTagName('UIAPickerWheel')
    if 'UIACollectionCell' in click_config:
        UIACollectionCells = root.getElementsByTagName('UIACollectionCell')
    if 'UIAStaticText' in click_config:
        UIAStaticTexts = root.getElementsByTagName('UIAStaticText')
    # get input enable elements:
    if 'UIATextField' in input_config:
        UIATextFields = root.getElementsByTagName('UIATextField')
    if 'UIASearchBar' in input_config:
        UIASearchBars = root.getElementsByTagName('UIASearchBar')
    if 'UIASecureTextField' in input_config:
        UIASecureTextFields = root.getElementsByTagName('UIASecureTextField')
    return nodes


def get_nodes_config(filename='./node.xml'):
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    # get nodes filter strategy
    filters = root.getElementsByTagName('filter')
    filter = filters[0].firstChild.data
    # get click controllers
    click_configs = root.getElementsByTagName('click')
    clicks = click_configs.getElementsByTagName('class')
    click_config = []
    for click in clicks:
        click_config.append(click.firstChild.data)
    # get input controllers
    input_configs = root.getElementsByTagName('input')
    inputs = input_configs.getElementsByTagName('class')
    input_config = []
    for input_i in inputs:
        input_config.append(input_i.firstChild.data)
    return filter, click_config, input_config


