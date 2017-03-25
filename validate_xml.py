# This Python file uses the following encoding: utf-8
"""
Usage: python validate_xml.py
"""
import lxml.etree as ET
import codecs, os, sys

# Function to validate without DTD file.
def validate_without_dtd():
	# Open and read input XML.
	fin = codecs.open('sk.xml','r','utf-8')
	out = fin.read()
	fin.close()
	# Try to parse. 
	# If there is error, it will be printed. Correct and retry.
	root = ET.fromstring(out.encode('utf-8'))
	# If there is no error, this line will be printed on screen.
	print "No error found in XML file."

# Function to vailidate with DTD.
def validate_with_dtd():
	parser = ET.XMLParser(dtd_validation=True)
	tree = ET.parse('sk.xml', parser)
	# If no error found, print this line.
	print "No error found in XML file."

# Function to validate with DTD, with printing of errors also on screen.
def validate_with_dtd1():
	dtd = ET.DTD('sk.dtd')
	tree = ET.parse('sk.xml')
	print dtd.validate(tree)
	# Print errors on screen for debug.
	print dtd.error_log.filter_from_errors()[0]

# Function to read XPATH from given XML.
def read_something(xpathexpression):
	parser = ET.XMLParser(dtd_validation=True)
	tree = ET.parse('sk.xml', parser)
	for member in tree.xpath(xpathexpression):
		children = member.getchildren()
		memtag = member.tag
		memtext = member.text
		if len(children) > 0:
			for child in children:
				# Print the data in given XPATH.
				print child.tag, child.text.encode('utf-8')
				print child.items()
		else:
			print memtag, memtext.encode('utf-8')
			print member.items()
			
if __name__=="__main__":
	if len(sys.argv) > 1:
		#read_something('//vArtika[@saMSayaH="1"]')
		read_something(sys.argv[1])
	else:
		validate_without_dtd()
		#validate_with_dtd()
		#validate_with_dtd1()
	
