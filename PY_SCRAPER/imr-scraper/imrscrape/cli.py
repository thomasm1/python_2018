import argparse
import csv
import os
from typing import List

from .main import scrape, Paragraph

from halo import Halo


def write_csv(out_file: str, paragraphs: List[Paragraph]):
    p = Paragraph()
    fieldnames = list(p.__dict__().keys())
    with open(out_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for paragraph in paragraphs:
            writer.writerow(paragraph.__dict__())


def qaqc(paragraphs: List[Paragraph]) -> str:
    text = ""
    all_paragraphs = range(14, 320, 1)
    current_paragraphs = [int(paragraph.number) for paragraph in paragraphs]
    diff = set(all_paragraphs) - set(current_paragraphs)
    for paragraph in sorted(diff):
        missing = f"Paragraph {paragraph} - missing\n"
        text += missing
    return text


def check_pdf_path(filepath) -> str:
    _, file_extension = os.path.splitext(filepath)
    if file_extension != ".pdf":
        raise argparse.ArgumentTypeError("input file must have .pdf extension" % value)
    return filepath


def check_csv_path(filepath) -> str:
    _, file_extension = os.path.splitext(filepath)
    if file_extension != ".csv":
        raise argparse.ArgumentTypeError("output file must have .csv extension" % value)
    return filepath


def main_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        type=check_pdf_path,
        required=True,
        help="path to input pdf file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=check_csv_path,
        required=True,
        help="path to output csv file",
    )
    parser.add_argument(
        "-qa",
        action="store_true",
        help="run QA/QC on input data for missing paragraphs",
    )
    args = parser.parse_args()
    spinner = Halo(text="Processing", spinner="dots")
    spinner.start()
    paragraphs = scrape(args.input)
    write_csv(args.output, paragraphs)
    spinner.succeed()
    if args.qa:
        print(qaqc(paragraphs))


if __name__ == "__main__":
    main_cli()
