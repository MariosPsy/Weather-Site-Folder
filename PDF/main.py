from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pandas.read_csv("topics.csv")

#print(df)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) #Color of text in RGB
    pdf.cell(w=0, h=12, txt=row["Topic"],
         align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21) #Add an underline

    for i in range(row["Pages"] - 1) :
        pdf.add_page()


pdf.output("csv_to_pdf.pdf")



