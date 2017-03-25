# Where are the files ?

1. Online view - https://drdhaval2785.github.io/siddhantakaumudi/
2. XML file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk.xml
3. HTML file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/sk.html
4. epub file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/sk.epub
5. babylon file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/siddhAnta-kaumudI.babylon
6. Stardict files - https://github.com/sanskrit-coders/stardict-sanskrit/tree/master/sa-vyAkaraNa/siddhAnta-kaumudI
7. txt file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk1.txt
8. docx file - https://github.com/drdhaval2785/siddhantakaumudi/blob/master/Siddhanta%20Kaumudi%20-%20Text%20only.doc

# Download and extraction

1. Downloaded Siddhanta Kaumudi - Text only.zip file from mail of Dr. H. N. Bhat dated 26 Dec 2016.
2. Extracted and copy pasted in siddhantakaumudi.txt (This is base copy in which there will not be any change.)
3. Created a copy of it in sk0.txt.

# Step 0 - Manual corrections

1. There are misorders in this file. So created a list of misordered sUtra numbers by step0.py in step0_notes.txt and made corrections in sk0.txt.
2. Added missing 2139-2150 sUtras manually in sk0.txt. 
3. sarvasamAsazeSaprakaraNam is missing.  - Added manually.
4. prakaraNa headings were missing. - Added manually.
5. तिङन्तप्रत्ययमालाप्रकरणम्‌ is missing. - Added manually.
6. Last one portion of svaraprakaraNam page 775 is missing. Added manually.
8. Correct verb number errors. They should be in chronologic order. When not, it means it is wrong. e.g. 157 वगि -> 147 वगि
9. 1209 verb number are missing in original. Made adjustment in step1.py logic.
10. Some missing data for verbs was also incorporated. The diff file is logged in sk0_manual.txt file. (by `diff siddhantakaumudi.txt sk0.txt > sk0_manual.txt`).
11. sUtra 3158 is missing in original SK text also (uNAdi sUtras are there in its place.) Therefore only 3977 sUtras are present instead of 3978 as in printed text.
12. Some vArtika markups were fishy. Corrected them manually. See issue 1.


# Step 1 - Mechanical changes and add markup

1. Add space after the sUtra number. (2264)धात्वादेः षः सः -> (2264) धात्वादेः षः सः
2. Add space after the sentence हल्संज्ञायाम्।। -> हल्संज्ञायाम् ।।
3. Change ।। -> ॥
4. (अ) -> ॒ and (स्व) -> ॑
5. ।शकन्ध्वादिषु पररूपं वाच्यम् (वा)।। depicts a vArtika. Try to preserve this information while correcting the spaces after and before ॥ and ।.

	5.1. {%...%} for vArtika.
	
	5.2. {%?...?%} Questionable vArtikas. There is a small subset 251 items following regex `'।[^ ।]([^।]+)।।'` which also has vArtikas (without (वा) at the end). See ।पितुर्भ्रातरि व्यत्।।. They are marked with {%?...?%}. Question mark shows that it needs to be verified whether they actually are vArtikas or not.
	
	5.3. {%??...??%} Very doubtful vArtikas. 143 such cases `'।([^ ।][^।0-9]+)।'` regex.
	
	5b and 5c need manual examination and confirmation whether they are actually vArtikas or not.
	
	Ideal is to make them uniformly in format of 5a in sk0.txt itself manually, so that it is consistent throughout.

6. Figures in bracket is SK rule number `(2264)`. Figures with two dashes are AS rule number `6-1-64`. Figures without bracktes are reference to SK rule.
There is a slight issue with the rule without bracket referring to only SK rules. They may also refer to verb number or something else too. e.g. `(2264)धात्वादेः षः सः    6-1-64 धातोरादेः षस्य सः स्यात्। सात्पदाद्योः 2123 इति षत्वनिषेधः। अनुस्वदते। सस्वदे। स्वर्दते। सस्वर्दे । 20 उर्द माने क्रीडायां च।।`
In the present example 2123 refers to SK rule, whereas 20 refers to the 20th verb under examination.
There is a possibility of identifying SK rule reference by regex `X इति` or `X इत्‍`or `X इती`.
Another check is - verb numbers will be in chronologic order. If there is some number which is not chronologic, it is highly probable that it is rule number.
Suggested approach - 

	6.1. {#...#} encoding for SK rule.

	6.2. {@...@} encoding for AS rule.

	6.3. {*...*} encoding for internal reference to SK rule.

	6.4. {$ {!verbnum verb!}+ verbmeaning$} encoding for verb number or other stuff (if they are found out). + sign depicts there can be more than one such occurrences. e.g. {$ {!31 युतृ!} {!32 जुदृ!} भासने$}
	

7. ःढ़द्य; -> ऊ

8. ञ्ञ is wrongly duplicated for most of the time. Have to find out a way to correct it mechanically. Pending. 1551 occurrences. Majority were errors. Converted to ञ. Should look out for errors.

9. श्र्व -> श्र

10. After all corrections, change >1 space to 1 space and remove trailing space.

# Step 2

Make XML (sk.xml) from sk1.txt file by make_xml.py. 

This step is purely mechanical. Wherever on parsing the XML was found to be ill-formed, its corrections were incorporated into make_xml.py.

The process was repeated till there were no errors in validate_xml.py (See step 3).

# Step 3

Validate XML

3a. Initially the validation was made using `etree.fromstring(out.encode('utf-8'))` without DTD file, with main intention to find out errors in XML file generated by make_xml.py. (See Step 2)

# Step 4: Generate HTML, EPUB and babylon files

4a. Run `./run_xslt.sh` to produce sk.html (requires libxslt to be installed)

4b. Run `./run_epub.sh` to produce sk.epub (requires Calibre to be installed)

4c. Run `python make_babylon.py` to produce siddhAnta-kaumudI.babylon file.

# Workflow

0. [redo.sh](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/redo.sh) - Runs all points mentioned below, except last.

1. [sk0.txt](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk0.txt) - basic file where all manual corrections are made. All others are derived from scripts.

2. [step1.py](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/step1.py) - Converts sk0.txt into tagged file sk1.txt.

3. [sk1.txt](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk1.txt) - File derived from sk0.txt which has tagged all important features.

4. [make_xml.py](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/make_xml.py) - Converts sk1.txt to sk.xml.

5. [sk.xml](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk.xml) - XML file

6. [validate_xml.py](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/validate_xml.py) - Checks whether the XML is well formed or not.

7. [sk_html.xslt](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/sk_html.xslt) - XSLT file which has information about how to generate sk.html file from sk.xml.

8. [run_xslt.sh](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/run_xslt.sh) - Converts sk.xml to sk.html file.

9. [sk.html](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/sk.html) - HTML file with appendices and changelog display etc.

10. [run_epub.sh](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/run_epub.sh) - Converts sk.html to sk.epub file.

11. [sk.epub](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/sk.epub) - EPUB file for viewing in epub readers.

10. [make_babylon.py](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/make_babylon.py) - Makes .babylon file from sk1.txt.

11. [siddhAnta-kaumudI.babylon](https://github.com/drdhaval2785/siddhantakaumudi/blob/master/docs/siddhAnta-kaumudI.babylon) - Babylon file which serves as input for generating stardict dictionary files.

12. [siddhAnta-kaumudI.babylon_final, siddhAnta-kaumudI.dict.dz, siddhAnta-kaumudI.idx, siddhAnta-kaumudI.ifo, siddhAnta-kaumudI.syn](https://github.com/sanskrit-coders/stardict-sanskrit/tree/master/sa-vyAkaraNa/siddhAnta-kaumudI) - Stardict files generated via processing in an [external repository](https://github.com/sanskrit-coders/stardict-sanskrit/).
