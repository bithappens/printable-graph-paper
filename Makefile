################################################################################
# Small makefile to simplify the pdf building process
################################################################################

.PHONY: clean


# Build all the pdfs
all: $(patsubst %.tex,%.pdf,$(wildcard *.tex))


clean:
	# remove build-directory and all its content
	rm -rf build


%.pdf: %.tex initbuilddirs
	# compile the pdf
	pdflatex -output-directory build $<
	# copy the final pdf to pdf-directory
	cp build/$@ pdf/$@


initbuilddirs:
	# Create directory for temporary build files
	mkdir -p build
	# Create directory for final pdfs
	mkdir -p pdf
