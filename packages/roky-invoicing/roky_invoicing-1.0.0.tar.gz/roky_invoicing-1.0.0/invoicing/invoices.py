import pandas
import glob
import os
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, product_id, product_name,
             amount_purchased, price_per_unit, total_price):
    """
    This function converts excel files into PDF invoices
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")
    print(filepaths)

    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4") #define pdf document
        pdf.add_page()  #add first page
        #stem gives you the filename without the extension in a string
        filename = Path(filepath).stem
        #extract first item in filename string (which is the invoice number)
        #invoice_nbr = filename.split("-")[0]  #first item in the list
        #invoice_date = filename.split("-")[1]  #2nd item in the list
        #or
        invoice_nbr, invoice_date = filename.split("-") #does the work of the two lines above

        pdf.set_font("Times", size=16, style="B")
        # use cell method to add text to a .pdf page
        # get the number dynamically from the name of the invoice
        pdf.cell(w=50, h=8, txt=f"Invoice Nbr: {invoice_nbr}", ln=1) #ln=1 spaces 1 line

        pdf.set_font("Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice Date: {invoice_date}", ln=1)

        #add table with data
        #"Sheet 1" is the tab name of the first (and i'm assuming) subsequent files
        df = pandas.read_excel(filepath, sheet_name="Sheet 1")
        print(df)
        #add the headerd
        columns = list(df.columns)
        #list comprehension to remove the underscores and capitalize all words
        #works through the entire list.  was rusty on that topic.  seems like a while ago
        columns = [item.replace("_", " ").title() for item in columns]
        pdf.set_font("Times", size=10, style="B")
        #pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=70, h=8, txt=columns[1], border=1)
        pdf.cell(w=30, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

        #create the data values in the spreadsheet
        #pdf.cell expects a string.  if you are sending numeric, you need to convert it
        for i, row in df.iterrows():
            pdf.set_font("Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border =1, ln=1)

        #create the total sum row
        total_sum = df[total_price].sum() #sums the value in the total column
        pdf.set_font("Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        #write the sum of the totals here after the emtpy rows
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

        #add total amount due row
        pdf.set_font("Times", size=10, style="B")
        pdf.cell(w=30, h=8, txt=f"The total price is: {total_sum} USD", ln=1)

        #add company name and logo
        pdf.set_font("Times", size=14, style="B")
        pdf.cell(w=25, h=8, txt=f"PythonHow")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path, exist_ok=True)
        pdf.output(f"{pdfs_path}/{filename}.pdf")

