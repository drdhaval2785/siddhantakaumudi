# This Python file uses the following encoding: utf-8
"""
Usage:
python make_xml.py inputfile outputfile logfile
e.g.
python make_xml.py sk1.txt xml/sk.xml xmlnotes.txt
"""
import re,codecs,sys
import transcoder

starttext = '<?xml version="1.0" encoding="UTF-8"?>\n<TEI xml:id="Dhaval__SK" xmlns="http://www.tei-c.org/ns/1.0">\n'
endtext = '</body>\n</text>\n</div></div></div>'

# Tuples have the following information (version, date, changelog, person, email)
def revhistory():
	historydata = [
		('1.0.0','2016-12-27','First version. 1. There are misorders in this file. So created a list of misordered sUtra numbers by step0.py in step0_notes.txt and made corrections in sk0.txt. \n2. Added missing 2139-2150 sUtras manually in sk0.txt. \n3. sarvasamAsazeSaprakaraNam is missing.  - Added manually. \n4. prakaraNa headings were missing. - Added manually. \n5. तिङन्तप्रत्ययमालाप्रकरणम्‌ is missing. - Added manually. \n6. Last one portion of svaraprakaraNam page 775 is missing. Added manually. \n8. Correct verb number errors. They should be in chronologic order. When not, it means it is wrong. e.g. 157 वगि -> 147 वगि \n9. 1209 verb number are missing in original. Made adjustment in step1.py logic. \n10. Some missing data for verbs was also incorporated. The diff file is logged in sk0_manual.txt file.','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
		('1.1.0','2017-02-06','Added missing vArtika markup manually. See https://github.com/drdhaval2785/siddhantakaumudi/issues/4','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
		('1.1.1','2017-02-12','1. Added sUtra detail on mouse hover. \n2. External links open in new tab. \n3. Latest HTML file is hosted on https://drdhaval2785.github.io/siddhantakaumudi for online viewing.','Karthikeyan Madathil','kmadathil@gmail.com'),
		('1.2.0','2017-02-12','1. Captured all verbs with meaning and number in XML itself. See https://github.com/drdhaval2785/siddhantakaumudi/issues/6 for details. \n2. Added pratyAhAra section and maGgalAcaraNam. See issue 12.','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
		('1.3.0','2017-02-15','1. Added paribhāṣās. See issue 11.','Dr. Dhaval Patel','drdhaval2785@gmail.com'),
		('1.3.1','2017-02-15','1. Added minimal stylesheet in HTML. See issue 25.','Karthikeyan Madathil','kmadathil@gmail.com'),
	]
	headertext = '<teiHeader xml:lang="en">\n<fileDesc>\n<titleStmt>\n<title>Siddhāntakaumudī</title>\n<respStmt>\n<persName>Dr. Dhaval Patel</persName>\n<resp>Creation and updation of XML</resp>\n</respStmt>\n<respStmt>\n<persName>Dr. H. N. Bhat</persName>\n<resp>Supply of base docx file.</resp>\n</respStmt>\n</titleStmt>\n<publicationStmt>\n<publisher>https://github.com/drdhaval2785/siddhantakaumudi/</publisher>\n<authority>Dr. Dhaval Patel</authority>\n<availability status="free">\n<p>Copyright Notice</p>\n<p>Copyright 2017 https://github.com/drdhaval2785/</p>\n<p><ref target="http://creativecommons.org/licenses/by-sa/4.0/" type="licence">Distributed by <ref target="https://github.com/drdhaval2785/siddhantakaumudi/" type="url">https://github.com/drdhaval2785/</ref> under a Creative Commons Attribution-ShareAlike 4.0 International License. </ref></p>\n<p>Under this licence, you are free <list>\n<item>to Share — to copy, distribute and transmit the work</item>\n<item>to Remix — to adapt the work </item></list></p>\n<p>Under the following conditions:</p>\n<p><list>\n<item>Attribution — You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).</item>\n<item>Share Alike — If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.</item></list></p>\n<p>More information and fuller details of this license are given on the Creative Commons website.</p>\n<p>https://github.com/drdhaval2785/ assumes no responsibility for unauthorised use that infringes the rights of any copyright owners, known or unknown.</p>\n</availability>\n<date>2017-02-06</date>\n</publicationStmt>\n<notesStmt>\n<note>Dr. H. N. Bhat posted a docx file on a google group on 2016-12-26 at https://groups.google.com/forum/#!searchin/bvparishat/siddhantakaumudi$20unicode|sort:relevance/bvparishat/iYYVe5sFaFM/tPBIEFvcDAAJ. The digital file has no description of source from where it was encoded nor who encoded it.</note>\n</notesStmt>\n<sourceDesc>\n<bibl>\n<title>Siddhāntakaumudī</title>\n<publisher>Unknown</publisher>\n<date>Unknown</date>\n</bibl>\n</sourceDesc>\n</fileDesc>\n<encodingDes>\n<editorialDecl>\n<p>The e-text is in Devanagari script</p>\n</editorialDecl>\n</encodingDes>\n<revisionDesc>\n'
	for (version, date, changelog, person, email) in historydata:
		headertext += '<change who="'+person+'" when="'+date+'">'+version+' - '+changelog+' '+'</change>\n'
	headertext += '</revisionDesc>\n</teiHeader>\n<text xml:id="__SK" xml:lang="sa-Deva">\n<body>'
	return headertext.decode('utf-8')

def add_tags1(x):
	x = re.sub(u'(। इति .*प्रकरणम्‌ ।)',u'</p>\n</div>\n<trailer>\g<0></trailer>',x)
	x = re.sub(u'{#([0-9]+)#}(.*){@([0-9-]+)@}',u'</p>\n</div>\n<div type="sūtra_with_explanation" n="\g<1>">\n<ab type="sūtra" n="\g<1>"><label type="SK">\g<1></label><label type="AS">\g<3></label>\g<2></ab>\n<p>',x)
	x = re.sub(u'{#फि([0-9]+)#}(.*){@([0-9-]+)@}',u'</p>\n</div>\n<div type="sūtra_with_explanation" n="फि\g<1>">\n<ab type="sūtra" n="फि\g<1>"><label type="SK">फि\g<1></label><label type="AS">\g<3></label>\g<2></ab>\n<p>',x)
	#x = re.sub(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="1">',u'<div type="sūtra_with_explanation" n="1">',x)
	x = re.sub(u'\n(॥ अथ [^॥]+ ॥)',u'\n<div type="prakaraṇa">\n<head>\g<1></head>',x)
	x = re.sub(u'</head>\W+</p>\W+</div>',u'</head>\n',x)
	x = re.sub(u'{[*]',u'<div type="SKsandarbhaḥ">',x)
	x = re.sub(u'[*]}',u'</div>',x)
	x = re.sub(u'{[$]',u'<div type="dhātvarthaḥ">',x)
	x = re.sub(u'[$]}',u'</div>',x)
	x = re.sub(u'{[!]',u'<div type="dhātuḥ">',x)
	x = re.sub(u'[!]}',u'</div>',x)
	x = re.sub(u'[[]\(प\)([^]]*)[]]',u'<div type="paribhāṣā">\g<1></div>',x)
	x = re.sub(u'{[%]([^%]*)[%]}',u'<div type="vārtika">\g<1></div>',x)
	x = re.sub(u'।<div type="vārtika">',u'<div type="vārtika">',x)
	x = x.replace(u'XXXXXXXXXXXXXXXXXXXX',u'</div>')
	x = x.replace(u'====================================',u'</div>')
	x = x.replace(u'</div></div></div>',u'</div>')
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="150">',u'<div type="sūtra_with_explanation" n="150">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="162">',u'<div type="sūtra_with_explanation" n="162">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2423">',u'<div type="sūtra_with_explanation" n="2423">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2489">',u'<div type="sūtra_with_explanation" n="2489">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2505">',u'<div type="sūtra_with_explanation" n="2505">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2523">',u'<div type="sūtra_with_explanation" n="2523">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2534">',u'<div type="sūtra_with_explanation" n="2534">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2543">',u'<div type="sūtra_with_explanation" n="2543">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2547">',u'<div type="sūtra_with_explanation" n="2547">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2554">',u'<div type="sūtra_with_explanation" n="2554">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2563">',u'<div type="sūtra_with_explanation" n="2563">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<div type="sūtra_with_explanation" n="2679">',u'<div type="sūtra_with_explanation" n="2679">') # Some odd entries handled now onwards
	x = x.replace(u'</p>\n</div>\n<trailer>। इति सवसमासशेषप्रकरणम्‌ ।</trailer>',u'<trailer>। इति सवसमासशेषप्रकरणम्‌ ।</trailer>')
	x = x.replace(u'<div type="SKsandarbhaḥ">21<div type="dhātukramaḥ">7</div>9</div>',u'<div type="SKsandarbhaḥ">2179</div>')
	x = re.sub(u'<div type="prakaraṇanāman">तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः</div>\W+</div>\n</div>\n<div type="sūtra">',u'<div type="prakaraṇanāman">तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः</div>\n<div type="sūtra">',x)
	x = re.sub(u'। इति तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः ।',u'</p>\n</div>\n<trailer>। इति तद्धिकाधिकारप्रकरणे अपत्यादिविकारान्तार्थसाधारणप्रत्ययाः ।</trailer>',x)
	x = x.replace(u'<div type="dhātukramaḥ">226</div>5</div>',u'<div type="SKsandarbhaḥ">2265</div>')
	x = re.sub(u'<head>॥ अथ तिङन्तप्रत्ययमालाप्रकरणम्‌ ॥</head>',u'<head>॥ अथ तिङन्तप्रत्ययमालाप्रकरणम्‌ ॥</head>\n<p>',x)
	x = re.sub(u'</p>\W+</div>\W+<trailer>। इति तिङन्तप्रत्ययमालाप्रकरणम्‌ ।</trailer>',u'</p>\W+<trailer>। इति तिङन्तप्रत्ययमालाप्रकरणम्‌ ।</trailer>',x)
	x = re.sub(u'इत्थं वैदिकशब्दानां दिङ्मात्रमिह दर्शितम्‌ ।(\W+)तदस्तु प्रीतये श्रीमद्भवानीविश्वनाथयोः ॥\W+</div>\W+</body>',u'<div type="colophon">इत्थं वैदिकशब्दानां दिङ्मात्रमिह दर्शितम्‌ ।\g<1>तदस्तु प्रीतये श्रीमद्भवानीविश्वनाथयोः ॥</div>\n</div>\n</body>',x)
	x = x.replace(u'</body>\n</text>\n</div>',u'</body>\n</text>\n</TEI>')
	x = x.replace(u'बुध्यती ॥<div type="dhātukramaḥ">3</div> ॥ बन्धि',u'बुध्यती ॥3 ॥ बन्धि')
	return x

fin = codecs.open('sk1.txt','r','utf-8')
input = fin.read()	
fout = codecs.open('sk.xml','w','utf-8')
input = starttext + '\n' + revhistory() + '\n' + input + '\n' + endtext + '\n'
output = add_tags1(input)
fout.write(output+'\n')
#print output.encode('utf-8')
