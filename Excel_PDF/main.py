import pandas
import glob
from fpdf import FPDF

print("Hello")

filepaths = glob.glob("*.xlsx")
print(filepaths)

for filepath in filepaths :
    df = pandas.read_excel(filepath)
    print(df)
    print()
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    invoice_nb = filepath[:5]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=16, txt="Invoice nb: {}".format(invoice_nb),
             align="L", ln=1)
    pdf.output("Excel_PDF_{}.pdf".format(invoice_nb))