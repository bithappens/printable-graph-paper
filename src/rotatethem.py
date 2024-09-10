#!/bin/python

from pathlib import Path

for portraitpath in sorted(Path(__file__).parent.glob('*-portrait.tex')):
    linkname = portraitpath.name.replace(".tex", "")
    landscapepath = portraitpath.parent / portraitpath.name.replace("portrait", "landscape")

    with open(landscapepath, 'w') as newfile:
        newfile.write("\\providecommand{\\geometryorientation}{landscape}\n")
        newfile.write(f"\\input{{{linkname}}}\n")
