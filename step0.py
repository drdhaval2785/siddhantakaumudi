# This Python file uses the following encoding: utf-8
"""
This file was used in initial phase of program to find out errors in numbering of sUtras.
Now no longer used. Legacy purpose.

Usage:
python step0.py sk0.txt step0_notes.txt
"""
import re,codecs,sys
import transcoder
def numberingerrors(filein,logfile):
	counter = 0
	fin = codecs.open(filein,'r','utf-8')
	fillog = codecs.open(logfile,'w','utf-8')
	for line in fin:
		if line.startswith('('):
			m = re.match('[(]([0-9]+)[)]',line)
			if m:
				rulenum = int(m.group(1))
				if rulenum == 0:
					pass
				elif not rulenum == counter + 1:
					fillog.write(str(counter)+','+m.group(1)+'\n')
				counter = rulenum
	fin.close()
	fillog.close()
if __name__=="__main__":
	filein = sys.argv[1]
	logfile1 = sys.argv[2]
	numberingerrors(filein,logfile1)
