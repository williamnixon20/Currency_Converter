import pandas as pd


def getValue(val, awal, target):
    df = pd.read_csv(f"fungsi/today_dfs/{awal}_exchange.csv")

    for i in range(len(df)):
        if target == df["currency"][i]:
            return (val*df["rate"][i])
