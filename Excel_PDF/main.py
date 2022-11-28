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

    date = filepath[6:-5]
    pdf.cell(w=50, h=16, txt="Date : {}".format(date), ln=1)

    #Add header
    columns_name = [item.replace("_"," ").title() for item in df.columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=10, txt=columns_name[0], border=1)
    pdf.cell(w=70, h=10, txt=columns_name[1], border=1)
    pdf.cell(w=30, h=10, txt=columns_name[2], border=1)
    pdf.cell(w=30, h=10, txt=columns_name[3], border=1)
    pdf.cell(w=30, h=10, txt=columns_name[4], border=1, ln=1)

    #Add rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1) #We dont put ln=1 because we want to be at the same line all the cells above
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output("Excel_PDF_{}.pdf".format(invoice_nb))