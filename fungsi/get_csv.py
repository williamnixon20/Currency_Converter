import os
import csv
import requests
import bs4 as bs
import pandas as pd
from datetime import datetime, timedelta


def save_csv():
    # Ambil data referensi semua list mata uang.
    curr_df = pd.read_csv("fungsi/currency_dfs/physical_currency_list.csv")
    # Buat list yang berisikan singkatan mata uang dan juga nama panjangnya.
    curr_list = [[curr_df["abbv"][i], curr_df["currency"][i]]
                 for i in range(len(curr_df))]

    # Buka salah satu data rujukan, ambil tanggalnya dan simpan ke last_date.
    with open("fungsi/currency_dfs/AED/fx_daily_AED_ARS.csv", 'r') as f:
        last_line = f.readlines()[-1]
    last_date = last_line.split(',')[0]

    # Jika last_date bukan hari ini, maka lanjutkan proses update.
    # Jika tidak, print data hari ini telah terupdate.
    if last_date != datetime.today():
        # Buat date_list yang berisikan list tanggal dari hari terakhir diupdate+1, sampai hari ini.
        date_list = pd.date_range(datetime.strptime(
            last_date, '%Y-%m-%d')+timedelta(days=1), datetime.today())

        # Untuk setiap hari ini date_list dan setiap mata uang di curr_list, webscrape datanya di www.xrates.com!
        for day in date_list:
            for curr in curr_list:
                # Lakukan request, ubah ke lxml, dan cari tabel yang bersesuaian.
                src = requests.get(
                    f"https://www.x-rates.com/historical/?from={curr[0]}&amount=1&date={day.strftime('%Y-%m-%d')}")
                soup = bs.BeautifulSoup(src.text, "lxml")
                table = soup.find("table", {"class": "tablesorter ratesTable"})
                # List kosong tempat menyimpan data.
                currs = []

                # Jika folder mata uang kita belum dibuat, buat terlebih dahulu.
                if not os.path.exists(f"fungsi/currency_dfs/{curr[0]}"):
                    os.makedirs(f"fungsi/currency_dfs/{curr[0]}")

                # Untuk setiap kolom yang bukan judul
                for row in table.findAll("tr")[1:]:
                    # Simpan nama mata uang kolom.
                    # Ubah nama mata uang kolom menjadi singkatannya (xxx).
                    currency = row.findAll("td")[0].text
                    for abbv in curr_list:
                        if currency == abbv[1]:
                            currency = abbv[0]
                    # Cari nilai tukarnya. Append tanggal, nilai tukar, serta simbol tukar ke dalam list currs.
                    exchange = row.findAll("td")[1].find('a').contents[0]
                    currs.append(
                        [day.strftime('%Y-%m-%d'), exchange, currency])

                # Untuk setiap data yang telah kita dapat di dalam currs, simpan ke dalam file.
                for row in currs:
                    if not os.path.exists(f"fungsi/currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[2]}.csv"):
                        with open(f"fungsi/currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[2]}.csv", "w", encoding="UTF8", newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(["date", "rate"])
                            writer.writerow([row[0], row[1]])
                        print(f"W: {day} {curr[0]} {row[1]}")
                    else:
                        with open(f"fungsi/currency_dfs/{curr[0]}/fx_daily_{curr[0]}_{row[2]}.csv", "a", encoding="UTF8", newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([row[0], row[1]])
                            f.close()
                        print(f"A: {day} {curr[0]} {row[1]}")
    else:
        print("Today's rate has been extracted")
