import pymupdf4llm
import fitz
import PyPDF2
import io

def parse_pdf(pdf_file, start_page, end_page):

    pdf_file = extract_relevant_pages(pdf_file, start_page, end_page)

    doc = fitz.open(stream=pdf_file, filetype="pdf")

    md_text = pymupdf4llm.to_markdown(doc)

    return(md_text)

def extract_relevant_pages(pdf_file, start_page, end_page):
    """Extracts a range of pages from a PDF file.

    Args:
        pdf_file: The PDF file object.
        start_page: The starting page number (inclusive, 1-based indexing).
        end_page: The ending page number (inclusive, 1-based indexing).

    Returns:
        A new PDF file (as bytes) containing the extracted pages.
    """

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    extracted_pdf_io = io.BytesIO()
    pdf_writer.write(extracted_pdf_io)
    return extracted_pdf_io.getvalue()