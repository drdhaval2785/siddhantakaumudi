#!/bin/bash

# Copyright 2017 Karthikeyan Madathil
# Released under MIT licence. See LICENCE.txt.

INFILE=docs/sk.html
OUTFILE=docs/sk.epub
ebook-convert $INFILE $OUTFILE --insert-blank-line --chapter "//h:h2" --chapter-mark "both" --level1-toc "//h:h2" --use-auto-toc --authors "Bhattoji Dikshita" --author-sort "Bhattoji Dikshita" --comments "Automatically generated from XML file: https://github.com/drdhaval2785/siddhantakaumudi" --language Sanskrit --title "Siddhanta Kaumudi" --max-toc-links 100
