# -*-coding:utf-8-*=
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
from xml.dom.minidom import parse


def get_device_number(filename):
    """

    :type filename: xml
    """
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    nodes = root.getElementsByTagName('device')
    device_number = len(nodes)
    return device_number


def get_udid(filename, device_number=None):
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    udids = root.getElementsByTagName('udid')
    udid = udids[device_number].firstChild.data
    return udid


def get_config(filename='../config/config.xml', device_number=None):
    """

    :type filename: xml
    :type device_number: int
    """
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    # get device name
    names = root.getElementsByTagName('name')
    device_name = names[device_number].firstChild.data
    # get version
    versions = root.getElementsByTagName('version')
    version = versions[device_number]
    ios_version = version.firstChild.data
    # get bundle_id
    bundleids = root.getElementsByTagName('bundleid')
    bundleid = bundleids[device_number]
    bundle_id = bundleid.firstChild.data
    # get device type
    devicetypes = root.getElementsByTagName('type')
    devicetype = devicetypes[device_number]
    device_type = devicetype.firstChild.data
    return device_name, ios_version, bundle_id, device_type


def get_ipa_path(filename):
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    ipas = root.getElementsByTagName('ipa')
    paths = ipas[0].getElementsByTagName('path')
    path = paths[0].firstChild.data
    return path


def get_level(filename):
    # get level
    xml_doc = parse(filename)
    root = xml_doc.documentElement
    traversals = root.getElementsByTagName('dfs')
    levels = traversals[0].getElementsByTagName('depth')
    level = int(levels[0].firstChild.data)
    return level


if __name__ == '__main__':
    res1 = get_device_number('config.xml')
    print res1
    res2 = get_config('config.xml', 1)
    print res2
    res3 = get_udid('config.xml', 0)
    print res3
    res4 = get_ipa_path('config.xml')
    print res4