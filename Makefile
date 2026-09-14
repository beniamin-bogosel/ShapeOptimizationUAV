DOCUMENTS = course-notes lab-sheets instructor-notes
PDFS = $(addprefix pdf/,$(addsuffix .pdf,$(DOCUMENTS)))
SOURCES = $(wildcard *.tex sessions/*.tex labs/*.tex instructor/*.tex)

.PHONY: all
all: $(PDFS)

pdf/%.pdf: %.tex $(SOURCES)
	mkdir -p build pdf
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $< > build/$*.build.log
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $< >> build/$*.build.log
	cp build/$*.pdf $@
