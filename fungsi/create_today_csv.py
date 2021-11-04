import csv
import requests
import bs4 as bs
import pandas as pd


def save_csv_today():
    # Ambil data referensi semua list mata uang.
    curr_df = pd.read_csv("fungsi/currency_dfs/physical_currency_list.csv")
    # Buat list yang berisikan singkatan mata uang dan juga nama panjangnya.
    curr_list = [[curr_df["abbv"][i], curr_df["currency"][i]]
                 for i in range(len(curr_df))]

    # Untuk setiap mata uang di curr list,
    for curr in curr_list:
        # Lakukan request, ubah ke lxml, dan cari tabel yang bersesuaian.
        src = requests.get(
            f"https://www.x-rates.com/table/?from={curr[0]}&amount=1")
        soup = bs.BeautifulSoup(src.text, "lxml")
        table = soup.find("table", {"class": "tablesorter ratesTable"})
        # Buat list curr kosong tempat menyimpan data.
        currs = []

        # Untuk setiap kolom yang bukan judul
        for row in table.findAll("tr")[1:]:
            # Simpan nama mata uang kolom. Ubah nama mata uang menjadi singkatannya (xxx).
            currency = row.findAll("td")[0].text
            for abbv in curr_list:
                if currency == abbv[1]:
                    currency = abbv[0]
            # Cari nilai tukarnya. Append tanggal, nilai tukar, serta simbol tukar ke dalam list currs.
            exchange = row.findAll("td")[1].find('a').contents[0]
            currs.append([currency, exchange])

        # Simpan data di dalam curr ke dalam file csv.
        with open(f"fungsi/today_dfs/{curr[0]}_exchange.csv", "w", encoding="UTF8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["currency", "rate"])
            for exc in currs:
                writer.writerow(exc)
