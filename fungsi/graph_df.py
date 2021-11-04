import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# Pastikan matplotlib tidak menampilkan data, tapi hanya membuat png yang diinginkan.
matplotlib.use('Agg')

# graph_df menerima input mata uang awal dan mata uang tujuan.
# matplotlib kemudian akan menggambarkan grafik yang bersesuaian dengan data.
# fungsi mereturn png grafik yang sesuai.
def graph_df(from_curr, to_curr):
    # Baca data perbandingan nilai 1 from_curr yang dikonversi menjadi to_curr tersebut.
    curr_df = pd.read_csv(
        f"fungsi/currency_dfs/{from_curr}/fx_daily_{from_curr}_{to_curr}.csv")

    # Buat list x (sumbu x) yang menyimpan tanggal data.
    # Buat list y (sumbu y) yang menyimpan rate nilai tukar.
    x = [curr_df["date"][i] for i in range(len(curr_df))]
    y = [curr_df["rate"][i] for i in range(len(curr_df))]

    # Jika nilai tukar akhir > nilai tukar awal, nilai tukar mengalami kenaikan.
    # Ubah plot menjadi warna hijau.
    # Jika turun = tidak berubah, maka ubah plot menjadi warna merah.
    if y[-1] > y[0]:
        plt.plot(x, y, color='green')
        plt.fill_between(x, y, color='green', alpha=0.2)
    else:
        plt.plot(x, y, color='red')
        plt.fill_between(x, y, color='red', alpha=0.2)

    # Pengaturan label, judul, skala, dan juga setup lain.
    plt.axis((x[0], x[-1], min(y)-(min(y)/1000), max(y)+(min(y)/1000)))
    plt.xticks(x[::5],  rotation='vertical')
    plt.xlabel('Date')
    plt.title(f"{from_curr} to {to_curr} exchange")
    plt.subplots_adjust(left=0.15,
                        bottom=0.25,
                        right=0.97,
                        top=0.94,
                        wspace=0.2,
                        hspace=0.2)

    # Jika folder penyimpanan belum dibuat, maka buat terlebih dahulu.
    if not os.path.isdir(f"static/img/graph_img/{from_curr}"):
        os.makedirs(f"static/img/graph_img/{from_curr}")

    # Simpan grafik ke dalam direktori ini.
    plt.savefig(f"static/img/graph_img/{from_curr}/{to_curr}.png")
