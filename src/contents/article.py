# -*- coding: utf-8 -*-

import os

from colorama import Fore
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


def create_pdf_article(content: dict):

    print(f"\n> {Fore.CYAN}[create-article]{Fore.RESET} Starting...")

    content_pdf = []
    search_term = content["search_term"].lower().replace(" ", "-")
    filename = f"data/{search_term}.pdf"

    pdf = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )

    print(f"> {Fore.CYAN}[create-article]{Fore.RESET} Adding title")
    content_pdf.append(
        Paragraph(content["source_content_title"], get_styles()["Title"])
    )
    content_pdf.append(Spacer(1, 12))

    print(f"> {Fore.CYAN}[create-article]{Fore.RESET} Adding sentences and images")
    content_pdf += add_sentences_and_images(content["sentences"])

    print(f"> {Fore.CYAN}[create-article]{Fore.RESET} Adding references")
    content_pdf += add_references(content["references"])

    pdf.build(content_pdf)
    print(
        f"> {Fore.CYAN}[create-article]{Fore.RESET} {Fore.GREEN}Article created{Fore.RESET}"
    )


def add_sentences_and_images(sentences: list) -> list:
    content = []
    for index, sentence in enumerate(sentences):
        content.append(Paragraph(sentence["text"], get_styles()["Justify"]))
        content.append(Spacer(1, 6))

        if len(sentence["images"]):
            filename = f"data/images/{index}.png"
            if index % 5 == 0 and os.path.exists(filename):
                image = Image(filename, 5 * inch, 4 * inch)
                content.append(image)
                content.append(Spacer(1, 6))

    return content


def add_references(references: list) -> list:
    content = []
    styles = get_styles()
    content.append(Spacer(1, 12))
    content.append(Paragraph("References", styles["Title"]))
    content.append(Spacer(1, 12))
    content += [Paragraph(r, styles["Justify"]) for r in references]
    return content


def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
    return styles
