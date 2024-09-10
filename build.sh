#!/bin/sh

mkdir -p pdf
cd src

if ! command -v parallel &> /dev/null
then
    find . -name "*.tex" -exec pdflatex -output-directory=../pdf {} \;
else
    find . -name "*.tex" | parallel --bar 'pdflatex -output-directory=../pdf >/dev/null {}'
fi

cd ../pdf
rm *.log *.aux *.nav *.out *.toc *.snm
