# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import xml.dom.minidom


def get_device_number(filename='./config.xml'):
    """

    :type filename: xml
    """
    xml_doc = xml.dom.minidom.parse(filename)
    root = xml_doc.documentElement
    nodes = root.getElementsByTagName('device')
    device_number = len(nodes)
    return device_number


def get_config(filename='./config.xml', device_number=None):
    """

    :type filename: xml
    :type device_number: int
    """
    xml_doc = xml.dom.minidom.parse(filename)
    root = xml_doc.documentElement
    nodes = root.getElementsByTagName('device')
    for node in nodes:
        if node.getAttribute('number') == str(device_number):
            ios_version = node.childNodes[2].data
            bundle_id = node.childNodes[3].data
            device_type = node.childNodes[4].data
    nodes = root.getElementsByTagName('level')
    level = int(nodes[0].data)
    return ios_version, bundle_id, device_type, level
