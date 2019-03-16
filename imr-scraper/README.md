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
