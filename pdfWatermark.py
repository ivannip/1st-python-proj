import os
import PyPDF2


try:
    with open("./pdf/combined.pdf", "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
except FileNotFoundError:
    print("File not existed")

