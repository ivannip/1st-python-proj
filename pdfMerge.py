import PyPDF2
import os

filenames = os.listdir("./pdf")
merge = PyPDF2.PdfFileMerger()

for file in filenames:
    merge.append(f"./pdf/{file}")

merge.write("./pdf/combined.pdf")



