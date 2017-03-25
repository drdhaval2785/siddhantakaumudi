# This Python file uses the following encoding: utf-8
"""
This file was used in initial phase of program to find out errors in numbering of sUtras.
Now no longer used. Legacy purpose.
So not documenting it in detail.

Usage:
python step0.py sk0.txt step0_notes.txt
"""

"""
LICENCE

MIT License

Copyright (c) 2017 Dr. Dhaval Patel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
