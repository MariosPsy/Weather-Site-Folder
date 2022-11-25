from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #Manipulate break lines

df = pandas.read_csv("topics.csv")

#print(df)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) #Color of text in RGB
    pdf.cell(w=0, h=12, txt=row["Topic"],
         align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21) #Add an underline
    #Add lines like notebbok
    for i in range(31,301,10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    # Add the footer under here
    pdf.ln(265) #Add break lines
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1) :
        pdf.add_page()
        # Add the footer under here
        pdf.ln(277) #Add break lines
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        # Add lines like notebbok
        for i in range(31, 301, 10):
            pdf.line(x1=10, y1=i, x2=200, y2=i)

pdf.output("csv_to_pdf.pdf")



