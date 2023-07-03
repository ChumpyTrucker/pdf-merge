import PyPDF2
# import sys



template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfWriter()

for i in range (template.pages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

