from fpdf import FPDF
import pandas as pd

### PANDAS INPUT
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("input/topics.csv",sep=",",header=0,skipinitialspace=True)
for i, row in df.iterrows():
        pdf.add_page()

        topic = row["Topic"]
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=f"Topic: {topic}", align="L", ln=1, border=1)
pdf.output("output/output.pdf")
