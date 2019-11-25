## WHAT IS THE PDF? 
	-> Portable Document Format; over 2.5 trillion PDFS... 
	-> 1993-Adobe Open format under ISO 2008; 
	-> PostScript; fonts, text, vector, raster
	-> ISSUES: ubiquitious as a data formatopen format, logs of writers, and encodings
	-> dark data - data not "packaged" in data format
	-> data aggregation / secondary data
	
## PyPDF2  (can't read Open-Office PDFs)
https://github.com/mstamy2/PyPDF2
filepath = "./pdfs/python_pdf.pdf"
from p... import P...
with open(filepath, 'rb") as f:
   reader = PdfFileReader(f)
   page_count = reader.getNumPages()
   for i in range(page_count):
       page = reader.getPage(i)
	   text = page.extractText()
	   
## pdfminer(.six)   (better with Open-Office PDFs; better support for CMaps)
https://github.com/pdfminer/pdfminer.six

## Common Gotchas
--> text needing O. Character pytesseract is Python program to do OCR on the PDF. 
--> dependent on OS/Program where PDF was created
--> CMaps maps text to glyphs ... CJK language support (important for Jap., Kor., Ch.)

## IMR Scrape
3.7 use @dataclass  ## no need to use __init__ 
	number: int = 0 
	give attributes
-->Uses generator function to go page by page
--> APD Forward
https://github.com/apdforward/imr-scrape

GUIs -> Python
->PyQT
->KIVY
->QT.io
->wxpython (legacy)
  wxpython Phoenix

#######################################################################################
# imrscrape

This Python module allows scraping of [IMR (Independent Monitoring Report)](https://www.abqmonitor.org/documents) PDFs to extract [CASA (Court Approved Settlement Agreement)](https://www.cabq.gov/police/documents/first-amended-restates-cour-approved-settlement-agreement.pdf) paragraph compliance and page information into a tabular format.

imrscrape is available as an importable Python module and as a CLI tool. 


## Installation

clone this repo:
```
git clone https://github.com/apd-forward/imr-scrape
```

run setup.py 
```
python setup.py
```

### CLI usage

#### Example

```
imrscrape -i ./imr-8-final.pdf -o ./imr-8-data.csv
```

#### Available Commands

+ _-i --input [filepath]_ (required)

    Takes the filepath to the PDF of the IMR to be scraped

+ _-o --output [filepath]_ (required)

    Take the filepath to a csv for the results

+ _-qa_

    returns a QA/QC report of possible missing paragraphs to stdout


## Development

This module is written using Python >3.7.0 syntax. Dependencies for development are managed with pipenv. Code is formatted with [black](https://github.com/ambv/black).
