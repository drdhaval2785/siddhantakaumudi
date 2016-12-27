rmdir output
rm -f log.txt
mkdir output
cd PADAMANJARI/PADAMANJARI
shopt -s nullglob
array=(*.*)
cd ../..

for FILENAME in "${array[@]}"
do
	# conversion
	python preprocess.py 'PADAMANJARI/PADAMANJARI/'$FILENAME
done
echo "preparing padamanjari.txt"
cat output/*[1234].txt > padamanjari.txt
echo "prepared padamanjari.txt"
