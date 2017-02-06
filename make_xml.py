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
endtext = '</vivaraRam></sUtra></sidDAntakOmudI>'

# Tuples have the following information (version, date, changelog, person, email)
def revhistory():
	historydata = [
		('1.0.0','2016-12-27','First version. 1. There are misorders in this file. So created a list of misordered sUtra numbers by step0.py in step0_notes.txt and made corrections in sk0.txt. 2. Added missing 2139-2150 sUtras manually in sk0.txt. 3. sarvasamAsazeSaprakaraNam is missing.  - Added manually. 4. prakaraNa headings were missing. - Added manually. 5. तिङन्तप्रत्ययमालाप्रकरणम्‌ is missing. - Added manually. 6. Last one portion of svaraprakaraNam page 775 is missing. Added manually. 8. Correct verb number errors. They should be in chronologic order. When not, it means it is wrong. e.g. 157 वगि -> 147 वगि 9. 1209 verb number are missing in original. Made adjustment in step1.py logic. 10. Some missing data for verbs was also incorporated. The diff file is logged in sk0_manual.txt file.','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
		('1.1.0','2017-01-06','Added missing vArtika markup manually. See https://github.com/drdhaval2785/siddhantakaumudi/issues/4','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
	]
	headertext = '<header>\n'
	for (version, date, changelog, person, email) in historydata:
		headertext += '<revHistory>\n'
		headertext += '<version>'+version+'</version>\n'
		headertext += '<date>'+date+'</date>\n'
		headertext += '<changelog>'+changelog+'</changelog>\n'
		headertext += '<person>'+person+'</person>\n'
		headertext += '<email>'+email+'</email>\n'
		headertext += '</revHistory>\n'
	headertext += '</header>'
	return headertext.decode('utf-8')

def add_tags(x):
	x = re.sub(r'{#','</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>',x)
	x = re.sub(r'#}','</SK><sUtramUlam>',x)
	x = re.sub(r'{@','</sUtramUlam><AS>',x)
	x = re.sub(r'@}','</AS>\n<vivaraRam>',x)
	x = re.sub(r'{[*]','<SKsandarBaH>',x)
	x = re.sub(r'[*]}','</SKsandarBaH>',x)
	x = re.sub(r'{[$]','<DAtukramaH>',x)
	x = re.sub(r'[$]}','</DAtukramaH>',x)
	#x = re.sub(r'{[%][?][?]([^?]*)[?][?][%]}','<vArtika saMSayaH="2">\g<1></vArtika>',x)
	#x = re.sub(r'{[%][?]([^?]*)[?][%]}','<vArtika saMSayaH="1">\g<1></vArtika>',x)
	x = re.sub(r'{[%]([^%]*)[%]}','<vArtika>\g<1></vArtika>',x)
	x = re.sub(u'।<vArtika>','<vArtika>',x)
	x = re.sub(u'\n॥ अथ ([^॥]+) ॥','\n<prakaraRa prakaraRanAman="\g<1>">',x)
	x = re.sub(u'प्रकरणम्‌">\W+</vivaraRam>\W+</sUtra>\W+<sUtra>',u'प्रकरणम्‌">\n<sUtra>',x)
	x = re.sub(u'प्रकरणम्">\W+</vivaraRam>\W+</sUtra>\W+<sUtra>',u'प्रकरणम्‌">\n<sUtra>',x)
	x = x.replace('XXXXXXXXXXXXXXXXXXXX','</prakaraRa>')
	x = x.replace('====================================','</prakaraRa>')
	x = x.replace('</vivaraRam></sUtra></sidDAntakOmudI>','</sidDAntakOmudI>')
	x = re.sub(u'। इति (.*प्रकरणम्‌) ।',u'</vivaraRam>\n</sUtra>\n<prakaraRAnta>\g<1></prakaraRAnta>',x)
	x = re.sub(u'। इति (.*प्रकरणम्) ।',u'</vivaraRam>\n</sUtra>\n<prakaraRAnta>\g<1></prakaraRAnta>',x)
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>150</SK>','<sUtra>\n<SK>150</SK>') # Some odd entries handled now onwards
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>162</SK>','<sUtra>\n<SK>162</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2423</SK>','<sUtra>\n<SK>2423</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2489</SK>','<sUtra>\n<SK>2489</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2505</SK>','<sUtra>\n<SK>2505</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2523</SK>','<sUtra>\n<SK>2523</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2534</SK>','<sUtra>\n<SK>2534</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2543</SK>','<sUtra>\n<SK>2543</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2547</SK>','<sUtra>\n<SK>2547</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2554</SK>','<sUtra>\n<SK>2554</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2563</SK>','<sUtra>\n<SK>2563</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<sUtra>\n<SK>2679</SK>','<sUtra>\n<SK>2679</SK>')
	x = x.replace(u'</vivaraRam>\n</sUtra>\n<prakaraRAnta>सवसमासशेषप्रकरणम्‌</prakaraRAnta>',u'<prakaraRAnta>सवसमासशेषप्रकरणम्‌</prakaraRAnta>')
	x = x.replace(u'<SKsandarBaH>21<DAtukramaH>7</DAtukramaH>9</SKsandarBaH>',u'<SKsandarBaH>2179</SKsandarBaH>')
	x = re.sub(u'<prakaraRa prakaraRanAman="तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः">\W+</vivaraRam>\n</sUtra>\n<sUtra>',u'<prakaraRa prakaraRanAman="तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः">\n<sUtra>',x)
	x = re.sub(u'। इति तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः ।',u'</vivaraRam>\n</sUtra>\n<prakaraRAnta>तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः</prakaraRAnta>',x)
	x = x.replace('<DAtukramaH>226</DAtukramaH>5</SKsandarBaH>','<SKsandarBaH>2265</SKsandarBaH>')
	x = re.sub(u'</vivaraRam>\n</sUtra>\n<prakaraRAnta>तिङन्तप्रत्ययमालाप्रकरणम्‌</prakaraRAnta>',u'\n<prakaraRAnta>तिङन्तप्रत्ययमालाप्रकरणम्‌</prakaraRAnta>',x)
	return x

fin = codecs.open('sk1.txt','r','utf-8')
input = fin.read()	
fout = codecs.open('sk.xml','w','utf-8')
input = starttext + '\n' + revhistory() + '\n' + input + '\n' + endtext + '\n'
output = add_tags(input)
fout.write(output+'\n')
#print output.encode('utf-8')
