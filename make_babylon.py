# This Python file uses the following encoding: utf-8
"""
Usage:
python make_babylon.py
e.g.
python make_babylon.py
"""
import re,codecs,sys
import transcoder


def add_tags1(x):
	m = re.search(u'{#([0-9]+)#}(.*){@([0-9-]+)@}',x)
	sutra = m.group(2).strip()
	num = transcoder.transcoder_processString(m.group(3).strip(),'slp1','deva')
	result = '\n\n'+num+'|'+sutra+'|'+sutra+' '+num+'|'+num+' '+sutra+'\n'
	result = result.replace('-','.')
	result = result.replace(u'\n\n०.०.०',u'०.०.०')
	return result

fin = codecs.open('sk1.txt','r','utf-8')
input = fin.readlines()	
fin.close()
output = ''
fout = codecs.open('docs/sk.babylon','w','utf-8')
for line in input:
	if re.match(u'{#([0-9]+)#}(.*){@([0-9-]+)@}',line):
		output += add_tags1(line)
	elif re.match(u'[X।॥]',line):
		pass
	else:
		output += line.strip()+' '
fout.write(output+'\n')
fout.close()
