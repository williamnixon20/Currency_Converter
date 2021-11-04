import pandas as pd

# Fungsi menerima kuantitas uang (val), mata uang awal (awal), dan target (target).


def getValue(val, awal, target):
    # Baca data dari CSV yang sesuai
    df = pd.read_csv(f"fungsi/today_dfs/{awal}_exchange.csv")

    # Cari kolom yang bersesuaian dengan target. Jika sudah ditemukan,
    # maka kalikan kuantitas dengan rate nilai tukar hari itu.
    for i in range(len(df)):
        if target == df["currency"][i]:
            return (val*df["rate"][i])
