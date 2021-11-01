from flask import render_template, request
from app import *
from functions.get_csv import save_csv
from functions.print_result import getValue
import os
from datetime import datetime


@app.route('/')
def home():
    return render_template('public/home.html')


@app.route("/konverter", methods=["GET", "POST"])
def konverter():
    tanggalupdate = os.path.getmtime(
        'functions/currency_dfs/AED_exchange.csv')
    tanggalupdate = datetime.fromtimestamp(
        tanggalupdate).strftime('%Y-%m-%d %H:%M:%S')

    if request.method == "POST":
        kuantitas = float(request.form.get('jumlah'))
        matauangasal = request.form.get('matauangasal')
        matauangtarget = request.form.get('matauangtarget')

        hasilkonversi = getValue(kuantitas, matauangasal, matauangtarget)
        return render_template("public/konverter.html", diperbarui=tanggalupdate, currencies=CURRENCIES, matauangasal=matauangasal, matauangtarget=matauangtarget, hasilkonversi=hasilkonversi, jumlahawal=kuantitas)
    else:
        return render_template("public/konverter.html", diperbarui=tanggalupdate, currencies=CURRENCIES)


@app.route("/graph", methods=["GET", "POST"])
def graph():
    # todo
    return render_template("public/graph.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


CURRENCIES = [["AED", "Emirati Dirham"],
              ["ARS", "Argentine Peso"],
              ["AUD", "Australian Dollar"],
              ["BGN", "Bulgarian Lev"],
              ["BHD", "Bahraini Dinar"],
              ["BND", "Bruneian Dollar"],
              ["BRL", "Brazilian Real"],
              ["BWP", "Botswana Pula"],
              ["CAD", "Canadian Dollar"],
              ["CHF", "Swiss Franc"],
              ["CLP", "Chilean Peso"],
              ["CNY", "Chinese Yuan Renminbi"],
              ["COP", "Colombian Peso"],
              ["CZK", "Czech Koruna"],
              ["DKK", "Danish Krone"],
              ["EUR", "Euro"],
              ["GBP", "British Pound"],
              ["HKD", "Hong Kong Dollar"],
              ["HRK", "Croatian Kuna"],
              ["HUF", "Hungarian Forint"],
              ["IDR", "Indonesian Rupiah"],
              ["ILS", "Israeli Shekel"],
              ["INR", "Indian Rupee"],
              ["IRR", "Iranian Rial"],
              ["ISK", "Icelandic Krona"],
              ["JPY", "Japanese Yen"],
              ["KRW", "South Korean Won"],
              ["KWD", "Kuwaiti Dinar"],
              ["KZT", "Kazakhstani Tenge"],
              ["LKR", "Sri Lankan Rupee"],
              ["LYD", "Libyan Dinar"],
              ["MUR", "Mauritian Rupee"],
              ["MXN", "Mexican Peso"],
              ["MYR", "Malaysian Ringgit"],
              ["NOK", "Norwegian Krone"],
              ["NPR", "Nepalese Rupee"],
              ["NZD", "New Zealand Dollar"],
              ["OMR", "Omani Rial"],
              ["PHP", "Philippine Peso"],
              ["PKR", "Pakistani Rupee"],
              ["PLN", "Polish Zloty"],
              ["QAR", "Qatari Riyal"],
              ["RON", "Romanian New Leu"],
              ["RUB", "Russian Ruble"],
              ["SAR", "Saudi Arabian Riyal"],
              ["SEK", "Swedish Krona"],
              ["SGD", "Singapore Dollar"],
              ["THB", "Thai Baht"],
              ["TRY", "Turkish Lira"],
              ["TTD", "Trinidadian Dollar"],
              ["TWD", "Taiwan New Dollar"],
              ["USD", "US Dollar"],
              ["VEF", "Venezuelan Bolivar"],
              ["ZAR", "South African Rand"]]
