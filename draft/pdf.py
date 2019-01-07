#open pdf with adobe reader with python
#import webbrowser as wb
#wb.open_new(r'C:\test.pdf')

import PyPDF2


def printpdf():
    pdf = input("file name: ")
    pdfobj = open(pdf, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdfobj)
    print(pdfreader.numPages)
    pageobj = pdfreader.getPage(0)
    print(pageobj.extractText())
    pdfobj.close()
    return


printpdf()
