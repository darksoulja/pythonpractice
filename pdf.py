#mergering file together (coming files together)
import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('Rohail_Butt_Resume_Cover.pdf')

pdf_combiner(inputs)

