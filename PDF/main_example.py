from fpdf import FPDF

#Create the basic object
pdf = FPDF(orientation="P", unit="mm", format="A4")

#Add page to the document
pdf.add_page()

#Modify the font of the text. For more explations see the .txt
pdf.set_font(family="Times", style="B", size=12)

#Add cells. For more explations see the .txt
pdf.cell(w=0, h=12, txt="Hello Marios",
         align="L", ln=1, border=1)

#Add one more cell with its one style
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hello Maria", align="R", ln=1)

#Vision of the objects thst we create
pdf.output("output.pdf")