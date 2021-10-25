from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from functions.get_csv import save_csv
from functions.print_result import getValue


# Configure application
app = Flask(__name__)
run_with_ngrok(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        kuantitas = int(request.form.get('jumlah'))
        matauangasal = request.form.get('matauangasal')
        matauangtarget = request.form.get('matauangtarget')

        hasilkonversi = getValue(kuantitas, matauangasal, matauangtarget)

        return render_template("index.html", currencies=CURRENCIES, matauangasal=matauangasal, matauangtarget=matauangtarget, hasilkonversi=hasilkonversi, jumlahawal=kuantitas)
    else:
        save_csv()
        return render_template("index.html", currencies=CURRENCIES)


# Tuple dari semua currency yang ada, sumber: https://gist.github.com/mjallday/1141751
CURRENCIES = curr_list = [["AED", "Emirati Dirham"],
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


if __name__ == '__main__':
    app.run()
