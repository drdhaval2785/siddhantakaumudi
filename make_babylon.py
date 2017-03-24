# This Python file uses the following encoding: utf-8
"""
Usage:
python make_babylon.py
e.g.
python make_babylon.py
"""
import re,codecs,sys
import transcoder


# Function to add | separated headwords and the first part of output. e.g.
"""
१.१.६९|अणुदित्सवर्णस्य चाप्रत्ययः|अणुदित्सवर्णस्य चाप्रत्ययः १.१.६९|१.१.६९ अणुदित्सवर्णस्य चाप्रत्ययः
अणुदित्सवर्णस्य चाप्रत्ययः १.१.६९ <BR>
"""
def add_tags1(x):
	# 1 = SK number, 2 = sUtra, 3 = AS number
	m = re.search(u'{#([फि।उ]*[0-9]+)#}(.*){@([0-9-]+)@}',x)
	# sUtra (in Devanagari)
	sutra = m.group(2).strip()
	# Number (in Devanagari)
	num = transcoder.transcoder_processString(m.group(3).strip(),'slp1','deva')
	"""
	१.१.६९|अणुदित्सवर्णस्य चाप्रत्ययः|अणुदित्सवर्णस्य चाप्रत्ययः १.१.६९|१.१.६९ अणुदित्सवर्णस्य चाप्रत्ययः
	अणुदित्सवर्णस्य चाप्रत्ययः १.१.६९ <BR>
	"""
	result = '\n\n'+num+'|'+sutra+'|'+sutra+' '+num+'|'+num+' '+sutra+'\n'+sutra+' '+num+' <BR> '
	# Change dash to period.
	result = result.replace('-','.')
	# Remove unnecessary two line breaks before the first entry.
	result = result.replace(u'\n\n०.०.०',u'०.०.०')
	return result

if __name__=="__main__":
	# open file and read linewise
	fin = codecs.open('sk1.txt','r','utf-8')
	input = fin.readlines()	
	fin.close()
	# Initiallize the output string
	output = ''
	# Open output file
	fout = codecs.open('docs/siddhAnta-kaumudI.babylon','w','utf-8')
	# For each line in input file
	for line in input:
		# If the line has sUtra, process it and add the modified string to output.
		if re.match(u'{#([फि।उ]*[0-9]+)#}(.*){@([0-9-]+)@}',line):
			output += add_tags1(line)
		# If line is prakaraNa separator, ignore it.
		elif re.match(u'[X।॥]',line):
			pass
		# If line is the sUtra explanation text, write it without any change.
		else:
			output += line.strip()+' '
	# Write output to file.
	fout.write(output+'\n\n')
	# Close file.
	fout.close()
