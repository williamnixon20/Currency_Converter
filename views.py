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
    tanggal_update_konverter = datetime.fromtimestamp(os.path.getmtime(
        'fungsi/today_dfs/AED_exchange.csv'))

    tanggal_update_graph = datetime.fromtimestamp(os.path.getmtime(
        'fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv'))

    if (datetime.now() - tanggal_update_konverter > timedelta(days=1)):
        print("Akan mengupdate data konverter")
        save_csv_today()
    if (datetime.now() - tanggal_update_graph > timedelta(days=1)):
        print("Akan mengupdate data graph")
        save_csv()


@app.route('/')
def home():
    return render_template('public/home.html')


@app.route("/konverter", methods=["GET", "POST"])
def konverter():
    tanggal_update_konverter = os.path.getmtime(
        'fungsi/today_dfs/AED_exchange.csv')
    tanggal_update_konverter = datetime.fromtimestamp(
        tanggal_update_konverter).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        kuantitas = float(request.form.get('jumlah'))
        mata_uang_asal = request.form.get('matauangasal')
        mata_uang_target = request.form.get('matauangtarget')

        hasil_konversi = getValue(kuantitas, mata_uang_asal, mata_uang_target)
        return render_template("public/konverter.html", diperbarui=tanggal_update_konverter, currencies=currencies, matauangasal=mata_uang_asal, matauangtarget=mata_uang_target, hasilkonversi=hasil_konversi, jumlahawal=kuantitas)
    else:
        return render_template("public/konverter.html", diperbarui=tanggal_update_konverter, currencies=currencies)


@app.route("/graph", methods=["GET", "POST"])
def graph():
    tanggal_update_graph = os.path.getmtime(
        'fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv')
    tanggal_update_graph = datetime.fromtimestamp(
        tanggal_update_graph).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        mata_uang_asal = request.form.get("matauangasal")
        mata_uang_target = request.form.get("matauangtarget")
        graph_df(mata_uang_asal, mata_uang_target)
        time.sleep(2)
        return render_template("public/graph.html", diperbarui=tanggal_update_graph, currencies=currencies, matauangasal=mata_uang_asal, matauangtarget=mata_uang_target)
    else:
        return render_template("public/graph.html", diperbarui=tanggal_update_graph, currencies=currencies)


@app.route("/about")
def about():
    return render_template("public/about.html")


currencies = [["AED", "Emirati Dirham"],
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
