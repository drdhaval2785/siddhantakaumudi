# This Python file uses the following encoding: utf-8
import lxml.etree as ET
import codecs
def validate_without_dtd():
	fin = codecs.open('sk.xml','r','utf-8')
	out = fin.read()
	fin.close()
	root = ET.fromstring(out.encode('utf-8'))
	print "No error found in XML file."
def validate_with_dtd():
	parser = ET.XMLParser(dtd_validation=True)
	tree = ET.parse('sk.xml', parser)
	print "No error found in XML file."

#validate_without_dtd()
validate_with_dtd()
