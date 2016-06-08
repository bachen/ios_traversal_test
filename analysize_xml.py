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
	# get level
	traversals = root.getElementsByTagName('traversal')
	levels = traversals[0].getElementsByTagName('level')
	level = int(levels[0].firstChild.nodeValue)
	return ios_version, bundle_id, device_type, level


if __name__ == '__main__':
	res1 = get_device_number('config.xml')
	print res1
	res2 = get_config('config.xml', 1)
	print res2
