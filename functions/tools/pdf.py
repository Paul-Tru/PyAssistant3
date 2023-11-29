from PyPDF2 import PdfReader, PdfWriter, PdfMerger


def get_meta(path, struc):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        info = pdf.metadata
        nop = len(pdf.pages)
    if struc == "info":
        return info
    if struc == "nop":
        return nop


def extract_text(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        page_one = pdf.pages[0]
        text = page_one.extract_text()
        return text


def split_pdf(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        for page in range(pdf.numPages):
            writer = PdfWriter()
            writer.addPage(pdf.pages[page])
            with open(f"{page}.pdf", "wb") as f_out:
                writer.write(f_out)


def merge_pdf(input_paths, output_path):
    writer = PdfWriter()
    for i in input_paths:
        pdf_reader = PdfReader(i)
        for page in range(pdf_reader.numPages):
            writer.addPage(pdf_reader.pages[page])
    with open(output_path, "wb") as f_out:
        writer.write(f_out)


def lazy_merge(input_paths, output_path):
    pdf_merger = PdfMerger()
    for i in input_paths:
        pdf_merger.append(i)
    with open(output_path, "wb") as f_out:
        pdf_merger.write(f_out)
