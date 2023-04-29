from fpdf import FPDF

pdf = FPDF(orientation="P",unit="mm", format= "A4")

#aggiungo pagina vuota
pdf.add_page()

#aggiugno una font
pdf.set_font(family="Times",style="B",size=12)
#aggiugno cell
pdf.cell(w=0,h=12,txt="Ciao a tutti", align="L",border=1)

pdf.cell(w=0,h=12,txt="Ciao di nuovo", align="L",border=1)
pdf.output("output/output.pdf")