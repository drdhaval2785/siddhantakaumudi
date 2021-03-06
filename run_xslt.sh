#!/bin/bash

# Copyright 2017 Karthikeyan Madathil
# Released under MIT licence. See LICENCE.txt.

function run_xslt {
    xsltproc --debug --output $OUTFILE --encoding $ENCODING $XSLT $INFILE
}

OUTFILE="docs/sk.html"
INFILE="sk.xml"
XSLT="sk_html.xslt"
ENCODING="utf-8"

run_xslt


