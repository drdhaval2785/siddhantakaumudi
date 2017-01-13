# This Python file uses the following encoding: utf-8
"""
Usage:
python make_xml.py inputfile outputfile logfile
e.g.
python make_xml.py sk1.txt xml/sk.xml xmlnotes.txt
"""
import re,codecs,sys
import transcoder

starttext = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE sidDAntakOmudI SYSTEM "sk.dtd">\n<sidDAntakOmudI>'
endtext = '</explanation></sUtra></sidDAntakOmudI>'

def add_tags(x):
	x = re.sub(r'{#','</explanation>\n</sUtra>\n<sUtra>\n<SK>',x)
	x = re.sub(r'#}','</SK><sUtraText>',x)
	x = re.sub(r'{@','</sUtraText><AS>',x)
	x = re.sub(r'@}','</AS>\n<explanation>',x)
	x = re.sub(r'{[*]','<refSK>',x)
	x = re.sub(r'[*]}','</refSK>',x)
	x = re.sub(r'{[$]','<rootNum>',x)
	x = re.sub(r'[$]}','</rootNum>',x)
	x = re.sub(r'{[%][?][?]([^?]*)[?][?][%]}','<vArtika doubt="2">\g<1></vArtika>',x)
	x = re.sub(r'{[%][?]([^?]*)[?][%]}','<vArtika doubt="1">\g<1></vArtika>',x)
	x = re.sub(r'{[%]([^%]*)[%]}','<vArtika doubt="0">\g<1></vArtika>',x)
	x = re.sub(u'॥ अथ ([^॥]+) ॥','<prakaraRa prakaraRanAman="\g<1>">',x)
	x = re.sub(u'प्रकरणम्‌">\W+</explanation>\W+</sUtra>\W+<sUtra>',u'प्रकरणम्‌">\n<sUtra>',x)
	x = re.sub(u'प्रकरणम्">\W+</explanation>\W+</sUtra>\W+<sUtra>',u'प्रकरणम्‌">\n<sUtra>',x)
	x = x.replace('XXXXXXXXXXXXXXXXXXXX','</prakaraRa>')
	x = x.replace('====================================','</prakaraRa>')
	x = x.replace('</explanation></sUtra></sidDAntakOmudI>','</sidDAntakOmudI>')
	x = re.sub(u'। इति (.*प्रकरणम्‌) ।',u'</explanation>\n</sUtra>\n<prakaraRAnta>\g<1></prakaraRAnta>',x)
	return x

fin = codecs.open('sk1.txt','r','utf-8')
input = fin.read()	
fout = codecs.open('trial.xml','w','utf-8')
input = starttext + '\n' + input + '\n' + endtext + '\n'
output = add_tags(input)
fout.write(output+'\n')
#print output.encode('utf-8')
