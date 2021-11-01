from flask import render_template, request
from app import *
from fungsi.get_csv import save_csv
from fungsi.print_result import getValue
from fungsi.graph_df import graph_df
from fungsi.create_today_csv import save_csv_today
import os
from datetime import datetime, timedelta
import time


def update():
    tanggalupdatekonverter = datetime.fromtimestamp(os.path.getmtime(
        'fungsi/today_dfs/AED_exchange.csv'))

    tanggalupdategraph = datetime.fromtimestamp(os.path.getmtime(
        'fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv'))

    if (datetime.now() - tanggalupdatekonverter > timedelta(days=1)):
        print("I am in!")
        save_csv_today()
    if (datetime.now() - tanggalupdategraph > timedelta(days=1)):
        print("I am in!")
        save_csv()


@app.route('/')
def home():
    return render_template('public/home.html')


@app.route("/konverter", methods=["GET", "POST"])
def konverter():
    tanggalupdatekonverter = os.path.getmtime(
        'fungsi/today_dfs/AED_exchange.csv')
    tanggalupdatekonverter = datetime.fromtimestamp(
        tanggalupdatekonverter).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        kuantitas = float(request.form.get('jumlah'))
        matauangasal = request.form.get('matauangasal')
        matauangtarget = request.form.get('matauangtarget')

        hasilkonversi = getValue(kuantitas, matauangasal, matauangtarget)
        return render_template("public/konverter.html", diperbarui=tanggalupdatekonverter, currencies=CURRENCIES, matauangasal=matauangasal, matauangtarget=matauangtarget, hasilkonversi=hasilkonversi, jumlahawal=kuantitas)
    else:
        return render_template("public/konverter.html", diperbarui=tanggalupdatekonverter, currencies=CURRENCIES)


@app.route("/graph", methods=["GET", "POST"])
def graph():
    tanggalupdategraph = os.path.getmtime(
        'fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv')
    tanggalupdategraph = datetime.fromtimestamp(
        tanggalupdategraph).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        matauangasal = request.form.get("matauangasal")
        matauangtarget = request.form.get("matauangtarget")
        graph_df(matauangasal, matauangtarget)
        time.sleep(2)
        return render_template("public/graph.html", diperbarui=tanggalupdategraph, currencies=CURRENCIES, matauangasal=matauangasal, matauangtarget=matauangtarget)
    else:
        return render_template("public/graph.html", diperbarui=tanggalupdategraph, currencies=CURRENCIES)


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
