# This Python file uses the following encoding: utf-8
"""
Usage:
python issue7.py
"""
import re,codecs

def issue7():
	fin = codecs.open('unadi.txt','r','utf-8')
	input = fin.readlines()
	fout = codecs.open('issue7.txt','w','utf-8')
	counter = 1
	for line in input:
		m = re.search(u'^([0-5][-][0-9]{,3}) ([^॥]+) ॥(.*)',line)
		if m:
			fout.write(u'(उ'+str(counter)+')'+m.group(2).strip()+'    10-'+m.group(1)+'\n'+m.group(3).strip()+'\n')
			print m.group(1)
			counter+=1 
	fout.close()

issue7()