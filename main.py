from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm", format= "A4")

#aggiungo pagina vuota
pdf.add_page()

#aggiugno una font
pdf.set_font(family="Times",style="B",size=12)
    #il size non è in mm ma in point. I millimetro impostati sopra sono usati dopo
#aggiugno cell

pdf.cell(w=0,h=12,txt="Ciao a tutti", align="L",ln= 1,border=1)
    #w = largezza della cella
    # border = largenzza dei bordi (0 --> senza bordi)
    # ln = è una sorta di separatore di celle. ln = 1 vuol dire cella a capo)
    # ln = 0 vuol dire che la cella successiva è aggiunta dopo la largenzza della cella w
    # h = altezza cella. si consiglia uguale a sie character
pdf.set_font(family="Times",style="B",size=10)
pdf.cell(w=0,h=12,txt="Ancora", align="L",ln= 1,border=1)

pdf.output("output/output.pdf")


#VOGLIO CREARE UNA PRIMA PAGINA DI UN CV PARTENDO DA UN FILE .CSV (info.txt)