from dataclasses import dataclass, field
import itertools
import re
import sys
from typing import Dict, Generator, List

from PyPDF2 import PdfFileReader


def clean_text(text: str) -> str:
    text = re.sub(
        r"Case\s1\:14\-cv\-\d+\-[A-Z]+\-[A-Z]+\s+Document\s\d+\s+Filed\s\d{2}/\d{2}/\d{2}\s+Page\d\d+\sof\s\d+",
        "",
        text,
    )
    return text


@dataclass
class Paragraph:
    number: int = 0
    pages: List[int] = field(default_factory=list)
    text: str = ""

    @property
    def primary_compliance(self) -> str:
        compliance = {}
        match = re.search(
            r"Primary:\s+([a-zA-Z]+\s+[a-zA-Z]+\s{0,1}[a-zA-Z]*\s{0,1}\w*)\s\s*",
            self.text,
        )
        if match:
            return match.group(1)
        else:
            return "None"

    @property
    def secondary_compliance(self) -> str:
        match = re.search(
            r"Secondary:\s+([a-zA-Z]+\s+[a-zA-Z]+\s{0,1}[a-zA-Z]*\s{0,1}\w*)\s\s*",
            self.text,
        )
        if match:
            return match.group(1)
        else:
            return "None"

    @property
    def operational_compliance(self) -> str:
        match = re.search(
            r"Operational:\s+([a-zA-Z]+\s+[a-zA-Z]+\s{0,1}[a-zA-Z]*\s{0,1}[a-zA-Z]*)\b(?<!Recommendation)",
            self.text,
        )
        if match:
            return match.group(1)
        else:
            return "None"

    def __bool__(self):
        if self.number:
            return True
        else:
            return False

    def __dict__(self):
        data = {}
        data["paragraph_number"] = self.number
        data["pages"] = self.pages
        data["text"] = self.text
        data["primary_compliance"] = self.primary_compliance
        data["secondary_compliance"] = self.secondary_compliance
        data["operational_compliance"] = self.operational_compliance
        return data


def get_page_num(page: str) -> int:
    match = re.search(r"^\s*(\d{1,3})\s+", page.replace("\n", ""))
    if match:
        return int(match.group(1))
    else:
        return 0


def operational_section(pages: Generator) -> Generator:
    front_matter = True
    next(itertools.islice(pages, 3, None))  # skip TOC
    while front_matter:
        page = next(pages)
        match = re.search(r"\s4\.7\s+\w+", page)
        if match:
            front_matter = False
    chained = itertools.chain((i for i in [page]), pages)
    return (item for item in chained)


def scrape_data(pages: Generator, page_count: int) -> List:
    paragraphs = []
    _pages = []
    p = Paragraph()
    for i, page in enumerate(pages):
        page_num = get_page_num(page)
        _pages.append(page_num)
        page = page.replace("\n", "")
        page = re.sub(r"^\s*(\d{1,3})\s+", "", page)
        page_split = re.split(
            r"4\.7\.\d+\sAssessing\sCompliance\s[with\s]*Paragraph\s(\d{2,3})\:*", page
        )
        if len(page_split) > 1:
            for x in page_split:
                match = re.search(r"^(\d+)$", x)
                if match:
                    if p:
                        p.text = clean_text(text)
                        p.pages = _pages
                        paragraphs.append(p)
                        p = Paragraph()
                        _pages = []
                        _pages.append(page_num)
                    text = ""
                    paragraph_num = match.group(1)
                    p.number = paragraph_num
                elif p and not match:
                    text += x
        else:
            text += "\n\n"
            text += page
        if i + 1 == page_count:
            p.text = text
            p.pages = _pages
            paragraphs.append(p)
    return paragraphs


def scrape(input_file: str) -> List[Paragraph]:
    with open(input_file, "rb") as f:
        reader = PdfFileReader(f)
        page_count = reader.getNumPages()
        pages = (reader.getPage(i).extractText() for i in range(page_count))
        pages = operational_section(pages)
        ps = scrape_data(pages, page_count - 3)
        return ps
