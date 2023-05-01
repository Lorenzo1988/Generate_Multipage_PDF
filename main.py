from fpdf import FPDF
import pandas as pd

### PANDAS INPUT
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("input/topics.csv",sep=",",header=0,skipinitialspace=True)
k= 0
soglia_footer = 265

def inserimento_righe(posizione_riga=22, altezza_riga_mm = 10):
    global soglia_footer
    while posizione_riga <= soglia_footer:
        pdf.line(10, posizione_riga, 200, posizione_riga)
        posizione_riga = posizione_riga + altezza_riga_mm


for i, row in df.iterrows():
        num_pagine = int(row["Pages"])
        print(f"num_pagine: {num_pagine}")
        j=0
        while j < num_pagine:
                topic = row["Topic"]
                pdf.set_font(family="Times", style="B", size=24)
                pdf.set_text_color(100,100,100)
                j=j+1
                if j == 1:
                    k=k+1
                    print(f"K:{k}")
                    pdf.add_page()
                    pdf.cell(w=0, h=12, txt=f"Topic: {topic}. Pagina: {j}", align="L", ln=1, border=0)

                    inserimento_righe()
                    #Set Footer
                    pdf.ln(soglia_footer)  # aggiunti 278 millimetri vuoti e arriva a pie pagina
                    pdf.set_font(family="Times", style="I", size=12)
                    pdf.set_text_color(180,180,180)
                    pdf.cell(w=0,h=10,txt=row["Topic"]+". Pagina:"+str(k),align="R")
                else:
                    k=k+1
                    print(f"K:{k}")
                    pdf.add_page()
                    inserimento_righe()

                    # Set Footer
                    pdf.ln(int(265+12))  # aggiunti 278 millimetri vuoti e arriva a pie pagina
                    pdf.set_font(family="Times", style="I", size=12)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=row["Topic"]+". Pagina:"+str(k), align="R")

pdf.output("output/output.pdf")
