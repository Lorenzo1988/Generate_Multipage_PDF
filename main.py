from fpdf import FPDF
import pandas as pd

### PANDAS INPUT
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("input/topics.csv",sep=",",header=0,skipinitialspace=True)
for i, row in df.iterrows():
        num_pagine = int(row["Pages"])-1
        for j in (1,num_pagine):
                topic = row["Topic"]
                pdf.set_font(family="Times", style="B", size=24)
                pdf.set_text_color(100,100,100)

                if j == 1:
                    pdf.add_page()
                    pdf.cell(w=0, h=12, txt=f"Topic: {topic}. Pagina: {j}", align="L", ln=1, border=0)
                    pdf.line(10,22,200,22)
                else:
                    pdf.add_page()

pdf.output("output/output.pdf")
