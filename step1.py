# This Python file uses the following encoding: utf-8
"""
Usage:
python step1.py inputfile outputfile logfile
e.g.
python step1.py sk0.txt sk1.txt step1_notes.txt
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

# Tag the verb, meaning etc.
def tryverb(filein,fileout,logfile):
	# open input file, output file, log file.
	fin = codecs.open(filein,'r','utf-8')
	fout = codecs.open(fileout,'w','utf-8')
	fillog = codecs.open(logfile,'w','utf-8')
	# Initialize lastverb with 0. Whenever a verb is encountered, it will be increased by 1.
	lastverb = 0
	# Initialize output list.
	output = []
	# For every line in file,
	for line in fin:
		# Line has pattern match e.g. `। 6 नाथृ 7 नाधृ याच्ञोपतापैस्वर्याशीःषु।`
		if re.search(u'। [0-9]{1,4} [^ ]+ [^।]+।',line):
			# Separate sentences in line.
			lin = line.split(u'।')
			# For each sentence,
			for mem in lin:
				# Find all matches e.g. ` 6 नाथृ 7 नाधृ याच्ञोपतापैस्वर्याशीःषु`
				out = re.findall(u' [0-9]{1,4} [^ ]+ [^।]+',mem)
				# For each such match,
				for member in out:
					# ['6','7']
					verbnums = re.findall('[0-9]{1,4}',member)
					# If the first member of list == last verb number + 1
					# e.g. in present case, first member is 6 and last stored verb number is 5. So it matches.
					if int(verbnums[0]) == lastverb + 1:
						# Convert to `{$ {!6 नाथृ!} {!7 नाधृ!} याच्ञोपतापैस्वर्याशीःषु$}`
						tagged = '{$' + re.sub(' ([0-9]{1,4} [^ ]+)',' {!\g<1>!}',member) + '$}'
						# Write to log file
						fillog.write(member+'\n')
						fillog.write(tagged+'\n')
						# Append to output list a tupple of (input,tagged)
						output.append((member,tagged))
						# After processing everything, change lastverb to the last treated verb e.g. 7 in our case.
						lastverb = int(verbnums[-1])
					# 1209 is missing in data. Jump it.
					if int(verbnums[-1]) == 1208:
						lastverb = int(verbnums[0]) + 1
	# Return the output list
	return output

# Run step1.py main algorithm.
def step1(filein,fileout,logfile):
	# Open input, output, log files.
	fin = codecs.open(filein,'r','utf-8')
	fout = codecs.open(fileout,'w','utf-8')
	fillog = codecs.open(logfile,'w','utf-8')
	# Write explanation item as first line in log file.
	fillog.write('; denotes unchanged item. $ denotes verb number. * denotes internal SK reference\n')
	# Initialize blank list of sUtra number of SK.
	sksutranum = []
	# verb number is initialized to 0.
	rootnum = 0
	# Write the lines containing verbs and their tagged version in verbdata.txt. This can be manually examined to identified if any verb is missing chronologically.
	replistforverbs = tryverb(filein,fileout,'verbdata.txt')
	# For each line in input file,
	for line in fin:
		# Point 5.1 - Tag vArtikas.
		if re.search(u'।([^।{]+)([(]वा[)][ ]*।)',line):
			line = re.sub(u'।([^।{]+)([(]वा[)][ ]*।)',u'।{%\g<1>%} (वा)।',line)
		# Point 5.2 - Tag questionable vArtikas. 
		# Questionable vArtikas. Noted in sk1_notes.txt. Needs manual examination. If they are not vArtikas, their preceding and ending | need correction in sk0.txt for future automated generation of sk1.txt from sk0.txt.
		# N.B. - As on 25/03/2017, there is no questionable vArtikas pending. They have all been examined and corrected.
		if re.search(u'।[^ ।{]([^।]+)।।',line):
			line = re.sub(u'।([^ ।{][^।0-9]+)।।',u'।{%?\g<1>?%} ।।',line)
		# Point 5.3 - As above.
		if re.search(u'।[^ ।{]([^।{]+)।',line):
			line = re.sub(u'।([^ ।{][^।0-9]+)।',u'।{%??\g<1>??%} ।',line)
		# sUtra references
		if re.match('[(]([0-9]+)[)]',line):
			# Points 1, 6.1, 6.2
			sksutranum = re.findall(u'^[(]([0-9]+)[)]',line)
			# (1)हलन्त्यम्    1-3-3 -> {#1#} हलन्त्यम्    {@1-3-3@}
			line = re.sub(u'^[(]([0-9]+)[)]([^0-9]+)([\-0-9]+)','{#\g<1>#} \g<2>{@\g<3>@}',line)
		# Tag phiTsUtras. # (फि1)फिषोऽन्त उदात्तः    10-1-1 -> {#फि1#} फिषोऽन्त उदात्तः {@10-1-1@}
		elif re.match(u'[(]फि([0-9]+)[)]',line):
			sksutranum = re.findall(u'^[(]फि([0-9]+)[)]',line)
			line = re.sub(u'^[(]फि([0-9]+)[)]([^0-9]+)([\-0-9]+)',u'{#फि\g<1>#} \g<2>{@\g<3>@}',line) 
		# Tag uNAdisUtras.  # (उ1)कृवापाजिमिस्वदिसाध्यशूभ्य उण्    9-1-1 -> {#उ1#} कृवापाजिमिस्वदिसाध्यशूभ्य उण् {@9-1-1@}
		elif re.match(u'[(]उ([0-9]+)[)]',line):
			sksutranum = re.findall(u'^[(]उ([0-9]+)[)]',line)
			line = re.sub(u'^[(]उ([0-9]+)[)]([^0-9]+)([\-0-9]+)',u'{#उ\g<1>#} \g<2>{@\g<3>@}',line)
		# Other than these
		else:
			# Internal references of SK / verb numbers in tiGanta prakaraNa.
			if re.search(u' [0-9]{1,4} ',line):
				# Find internal SK references or verb numbers.
				m = re.findall(u' ([0-9]{1,4}) ',line)
				# For all matches,
				for member in m:
					# Verbs start from sUtra 2164 to 2829. And the verb number == previous verb number + 1
					if int(sksutranum[0]) > 2164 and int(sksutranum[0]) < 2829 and int(member) == rootnum+1: # Ignore roots having the same markup as internal references to SK.
						rootnum = int(member)
						# Write to log file.
						fillog.write('$ '+sksutranum[0]+' '+member+'\n')
						if member == '1208': # 1209 is missing in original too.
							rootnum = int(member)+1
					# Usually verses / shlokavArtikas etc have numbers < 5, so separating them.
					elif int(member) <= 5:
						# Write to log file.
						fillog.write('; '+sksutranum[0]+' '+member+'\n')
					# Else, they are SK internal references.
					else:
						# Tag for SK internal references.
						line = line.replace(member,'{*'+member+'*}')
						# Write to log file.
						fillog.write('* '+sksutranum[0]+' '+member+'\n')
			# Catching the SK internal references which do not have space before or space after the number.
			if re.search(u'[^*]([0-9]{2,4})([^0-9\-@#$%^*])',line):
				m = re.findall(u'[^*]([0-9]{2,4})[^ 0-9\-@#$%^*]',line)
				# Tag them as internal SK references.
				line = re.sub(u'([^*])([0-9]{2,4})([^ 0-9\-@#$%^*])',u'\g<1>{*\g<2>*}\g<3>',line)
				# For each match,
				for member in m:
					# Write to log file.
					fillog.write('* '+sksutranum[0]+' '+member+'\n')
			# Add internal references to phiTsUtras
			if re.search(u' फि[0-9]{1,4} ',line):
				# Find matches
				m = re.findall(u' (फि[0-9]{1,4}) ',line)
				# Tag them
				line = re.sub(u' (फि[0-9]{1,4}) ',u' {*\g<1>*} ',line)
				# Write to log file
				for member in m:
					fillog.write('* '+sksutranum[0]+' '+member+'\n')
			# Add internal references to uNAdisUtras
			if re.search(u' उ[0-9]{1,4} ',line):
				# Find matches
				m = re.findall(u' (उ[0-9]{1,4}) ',line)
				# Tag them
				line = re.sub(u' (उ[0-9]{1,4}) ',u' {*\g<1>*} ',line)
				# Write to log file.
				for member in m:
					fillog.write('* '+sksutranum[0]+' '+member+'\n')
		# Point 4. Convert accent marks [ (अ) -> ॒ and (स्व) -> ॑ ]
		line = line.replace(u'(अ)',u'॒')
		line = line.replace(u'(स्व)',u'॑')
		# Point 2. Add space after the sentence हल्संज्ञायाम्।। -> हल्संज्ञायाम् ।।
		line = re.sub(u'([^ ])।',u'\g<1> ।',line)
		# Point 3. Change ।। -> ॥
		line = line.replace(u'।।',u'॥')
		line = line.replace(u'। ।',u'॥')
		# Club multiple spaces into one.
		line = re.sub('[ ]+',' ',line)
		# Issue 29.  Add space after double danda.
		line = re.sub(u'॥([0-9])',u'॥ \g<1>',line)
		# Catch some missed SK internal reference tags.
		line = re.sub('[\-]([0-9]{2,4}) ','-{*\g<1>*} ',line)
		# Typical entry corrections. Mostly caused by a string in one SK reference forming part of another reference e.g. 12 and 1512.
		# They need to be manually corrected.
		line = line.replace(u'2528 इत्यादिसूत्रद्वये',u'{*2528*} इत्यादिसूत्रद्वये') # Only single item where there are two consecutive numbers.
		line = line.replace(u'{*1509*} बन्ध बन्धने',u'{$ {!1509 बन्ध!} बन्धने$}') # Some sUtras and dhAtu numbers overlap 1509 rule occurs in the same line as the verb number. 
		line = line.replace(u'{*15*}{*12*} मन्थ विलोडने',u'{$ {!1509 मन्थ!} विलोडने$}') # Some sUtras and dhAtu numbers overlap 12 rule occurs in the same line as the verb number. 
		line = line.replace(u'{#99#} ई{@3@} चाऽक्रवर्मणस्य 6-1-{*130*}',u'{#99#} ई3 चाऽक्रवर्मणस्य {@6-1-130@}') # See https://github.com/drdhaval2785/siddhantakaumudi/issues/58.
		
		# When there are two same numbers in a line, they are double qouted. Removing the outer one (wrong one).
		line = re.sub(u'[{][@#$%*][{]','{',line)
		line = re.sub(u'[}][@#$%*][}]','}',line)
		for (base,rep) in replistforverbs:
			line = line.replace(base,rep)
		# Making corrections for some convertor issues which corrupted the input file. See steps 7, 8, 9.
		line = line.replace(u'ञ्ञ',u'ञ')
		line = line.replace(u'ःढ़द्य;',u'ऊ')
		line = line.replace(u'श्र्व',u'श्व')
		# [^#@*$%\?\-][0-9]+[^0-9#@*$%\?\-] is the regex which gave missed out internal references. Smaller than 10 can be ignored (accent/verse number etc). Now completed incorporating it in code.
		# Write the modified text to the output file.
		fout.write(line)
	# Close the files.
	fin.close()
	fout.close()
	fillog.close()
			
if __name__=="__main__":
	# sk0.txt
	filein = sys.argv[1]
	# sk1.txt
	fileout = sys.argv[2]
	# step1_notes.txt
	logfile = sys.argv[3]
	# Run step1 module.
	step1(filein,fileout,logfile)

	#tryverb(filein,fileout,'verbdata.txt')
	