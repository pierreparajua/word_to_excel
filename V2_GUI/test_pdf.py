from docx2pdf import convert
from function import PATH_RESULT

list = 'Appendix 3.01 - PV modules.docx'
pdf = list[:-5] + ".pdf"
print(pdf)

convert(PATH_RESULT / list, PATH_RESULT / pdf)