# This Python file uses the following encoding: utf-8
"""
Usage:
python issue35.py
"""
import re,codecs

def dupSutras():
	fin = codecs.open('../sk1.txt','r','utf-8')
	input = fin.readlines()
	fout = codecs.open('issue35.txt','w','utf-8')
	sUtralist = set()
	for line in input:
		ASsUtra = re.sub(u'{#([0-9]+)#}(.*){@([0-9-]+)@}','\g<3>',line)
		if not ASsUtra == line:
			if ASsUtra not in sUtralist:
				sUtralist.add(ASsUtra)
			else:
				fout.write(ASsUtra)
				print ASsUtra.encode('utf-8')
	fout.close()

dupSutras()