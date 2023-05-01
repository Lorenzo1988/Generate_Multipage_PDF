from fpdf import FPDF
import pandas as pd

### PANDAS INPUT
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("input/topics.csv",sep=",",header=0,skipinitialspace=True)

# k serve per le note a piede (footer)
k= 0
for i, row in df.iterrows():
        num_pagine = int(row["Pages"])-1
        for j in (1,num_pagine):
                topic = row["Topic"]
                pdf.set_font(family="Times", style="B", size=24)
                pdf.set_text_color(100,100,100)
                k = k+1
                print(f"K:{k}")
                pdf.add_page()
                if j == 1:
                    pdf.cell(w=0, h=12, txt=f"Topic: {topic}. Pagina: {j}", align="L", ln=1, border=0)
                    pdf.line(10,22,200,22)
                   #Set Footer
                    pdf.ln(265)  # aggiunti 278 millimetri vuoti e arriva a pie pagina
                    pdf.set_font(family="Times", style="I", size=12)
                    pdf.set_text_color(180,180,180)
                    pdf.cell(w=0,h=10,txt=row["Topic"]+". Pagina:"+str(k),align="R")
                else:
                    # Set Footer
                    pdf.ln(int(265+12))  # aggiunti 278 millimetri vuoti e arriva a pie pagina
                    pdf.set_font(family="Times", style="I", size=12)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=row["Topic"]+". Pagina:"+str(k), align="R")

pdf.output("output/output.pdf")
