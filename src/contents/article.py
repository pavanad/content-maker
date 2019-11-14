# -*- coding: utf-8 -*-

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def create_pdf_article(content: dict):

    content_pdf = []
    filename = "data/article.pdf"

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
    for sentence in sentences:
        content_pdf.append(Paragraph(sentence['text'], styles["Justify"]))
        content_pdf.append(Spacer(1, 6))

    pdf.build(content_pdf)


def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
    return styles
