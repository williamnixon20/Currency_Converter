from flask import render_template, request
from app import *
from fungsi.get_csv import save_csv
from fungsi.print_result import getValue
from fungsi.graph_df import graph_df
from fungsi.create_today_csv import save_csv_today
import os
from datetime import datetime, timedelta

# Fungsi untuk mengupdate database jika waktu update terakhir > 1 hari
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

# Router jika web diakses melalui jalur /


@app.route('/')
def home():
    return render_template('public/home.html')

# Router jika web diakses melalui jalur /konverter
@app.route("/konverter", methods=["GET", "POST"])
def konverter():
    # Tanggal terakhir data di update
    tanggal_update_konverter = os.path.getmtime(
        'fungsi/today_dfs/AED_exchange.csv')
    tanggal_update_konverter = datetime.fromtimestamp(
        tanggal_update_konverter).strftime('%Y-%m-%d %H:%M:%S')
    # Jika user telah mengsubmit data ("POST"), olah data tersebut dengan mengoper data ke fungsi getValue!
    if request.method == "POST":
        kuantitas = float(request.form.get('jumlah'))
        mata_uang_asal = request.form.get('matauangasal')
        mata_uang_target = request.form.get('matauangtarget')

        hasil_konversi = getValue(kuantitas, mata_uang_asal, mata_uang_target)
        return render_template("public/konverter.html", diperbarui=tanggal_update_konverter, currencies=currencies, matauangasal=mata_uang_asal, matauangtarget=mata_uang_target, hasilkonversi=hasil_konversi, jumlahawal=kuantitas)
    # Jika user meminta halaman ("GET"), maka berikan halaman HTML yang sesuai.
    else:
        return render_template("public/konverter.html", diperbarui=tanggal_update_konverter, currencies=currencies)

# Router jika web diakses melalui jalur /graph
@app.route("/graph", methods=["GET", "POST"])
def graph():
    # Tanggal terakhir data graph diupdate
    tanggal_update_graph = os.path.getmtime(
        'fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv')
    tanggal_update_graph = datetime.fromtimestamp(
        tanggal_update_graph).strftime('%Y-%m-%d %H:%M:%S')
    # Jika user telah mengsubmit data ("POST"), buat grafik yang sesuai dengan mengoper ke fungsi graph_df
    if request.method == "POST":
        mata_uang_asal = request.form.get("matauangasal")
        mata_uang_target = request.form.get("matauangtarget")
        graph_df(mata_uang_asal, mata_uang_target)
        return render_template("public/graph.html", diperbarui=tanggal_update_graph, currencies=currencies, matauangasal=mata_uang_asal, matauangtarget=mata_uang_target)
    else:
        # Jika user meminta halaman ("GET"), maka berikan halaman HTML yang sesuai.
        return render_template("public/graph.html", diperbarui=tanggal_update_graph, currencies=currencies)

# Router jika web diakses melalui jalur /about
@app.route("/about")
def about():
    # Kembalikan halaman yang sesuai
    return render_template("public/about.html")


# Matriks Nx2 tempat menyimpan data singkatan mata uang dan nama panjangnya.
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
