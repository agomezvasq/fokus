import io

from urllib import request
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage, PDFParser, PDFDocument, PDFTextExtractionNotAllowed


def convert_pdf_to_txt(url):
    remoteFile = request.urlopen(url).read()
    memoryFile = io.BytesIO(remoteFile)
    parser = PDFParser(memoryFile)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    codec = 'utf-8'
    device = TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)

    text = retstr.getvalue()

    device.close()
    retstr.close()
    return text


#print(convert_pdf_to_txt('https://arxiv.org/pdf/1804.09579.pdf'))



