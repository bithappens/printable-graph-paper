#!/bin/python

from pathlib import Path

previous = ''

for pdfpath in sorted(Path(__file__).parent.parent.glob('pdf/*.pdf')):
    cleanname = pdfpath.name.replace("paper-", " Format ").replace(".pdf", "").title()
    linkoutput = f"[{cleanname}](https://github.com/bithappens/printable-graph-paper/releases/latest/download/{pdfpath.name})"

    if "landscape" in linkoutput:
        previous = linkoutput
    else:
        if previous:
            print('*', linkoutput, "/", previous)
            previous = ''
        else:
            print('*', linkoutput)
