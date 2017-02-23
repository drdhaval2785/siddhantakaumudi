#diff sk0.txt siddhantakaumudi.txt > sk0_notes.txt
echo "Step 1 - Creating sk1.txt from sk0.txt by adding markup."
python step1.py sk0.txt sk1.txt step1_notes.txt
#diff sk1.txt sk0.txt > sk1_notes.txt
echo "Step 2 - Creating sk.xml from sk1.txt file."
python make_xml.py
echo "Step 3 - Validating sk.xml file for errors."
python validate_xml.py
echo "Step 4 - Creating HTML from XML. (Requires libxslt)"
./run_xslt.sh
#echo "Step 5 - Creating epub from HTML. (Requires Calibre)"
#./run_epub.sh
#echo "Step6 - Creating babylon file from sk1.txt"
#python make_babylon.py
