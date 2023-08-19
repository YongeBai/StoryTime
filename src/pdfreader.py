from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

out = StringIO()

with open('src/Einstein_Walter_Isaacson_Z-Library.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    device = TextConverter(rsrcmgr, out, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

    with open('output.txt', 'a', encoding=codec) as f:
        f.writelines(out.getvalue())