# This Python file uses the following encoding: utf-8
import lxml.etree as ET
import codecs, os, sys
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
def read_something(xpathexpression):
	parser = ET.XMLParser(dtd_validation=True)
	tree = ET.parse('sk.xml', parser)
	for member in tree.xpath(xpathexpression):
		children = member.getchildren()
		memtag = member.tag
		memtext = member.text
		if len(children) > 0:
			for child in children:
				print child.tag, child.text.encode('utf-8')
		else:
			print memtag, memtext.encode('utf-8')
			
if __name__=="__main__":
	if len(sys.argv) > 1:
		#read_something('//vArtika[@saMSayaH="1"]')
		print sys.argv[1]
		read_something(sys.argv[1])
	elif not os.path.isfile('sk.dtd'):
			validate_without_dtd()
	else:
		validate_with_dtd()
