# -*- coding: utf-8 -*-

import os

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


def create_pdf_article(content: dict):

    print("> [create-article] Starting...")

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

    styles = get_styles()
    content_pdf.append(Paragraph(content["source_content_title"], styles["Title"]))
    content_pdf.append(Spacer(1, 12))

    sentences = content["sentences"]
    for index, sentence in enumerate(sentences):
        content_pdf.append(Paragraph(sentence["text"], styles["Justify"]))
        content_pdf.append(Spacer(1, 6))

        filename = f"data/images/{index}.png"
        if index % 5 == 0 and os.path.exists(filename):
            image = Image(filename, 5 * inch, 4 * inch)
            content_pdf.append(image)
            content_pdf.append(Spacer(1, 6))

    pdf.build(content_pdf)
    print("> [create-article] Article created")


def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
    return styles
