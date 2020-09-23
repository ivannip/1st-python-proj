import PyPDF2

try:
    output = PyPDF2.PdfFileWriter()
    wtr_reader = PyPDF2.PdfFileReader(open("./pdf/wtr.pdf", "rb"))
    i_reader = PyPDF2.PdfFileReader(open("./pdf/00. Cover v0.2.pdf", "rb"))
    i = 0
    for i in range(i_reader.getNumPages()):
        page = i_reader.getPage(i)
        page.mergePage(wtr_reader.getPage(0))
        output.addPage(page)

    with open("./pdf/newfile.pdf", "wb") as f:
        output.write(f)


except FileNotFoundError:
    print("File not existed")

