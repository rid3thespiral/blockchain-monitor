import pandas as pd
import glob
import bar_chart_race as bcr
import warnings as ws

ws.filterwarnings("ignore")

ethblocks=pd.read_csv('cryptocurrencies_data/ethereum.csv', parse_dates=["Date(UTC)"], index_col="Date(UTC)").drop(labels="UnixTimeStamp",axis=1)

#scelgo periodo di osservazione: 01/01/20-01/8/20
ethblocks=ethblocks.loc["2016-10-28":"2018-08-12"]
ethblocks["blockCount"] = ethblocks["Value"]
zcashblocks = pd.read_csv('cryptocurrencies_data/zcash.csv', parse_dates=["date"], index_col="date")
moneroblocks = pd.read_csv('cryptocurrencies_data/monero.csv', parse_dates=["date"], index_col="date")
dogeblocks = pd.read_csv('cryptocurrencies_data/dogecoin.csv', parse_dates=["date"], index_col="date")
moneroblocks = moneroblocks.loc["2016-10-28":"2018-08-12"]
dogeblocks = dogeblocks.loc["2016-10-28":"2018-08-12"]

#create a location
ethblocks["agg"] = ethblocks["blockCount"]
zcashblocks["agg"] = zcashblocks["blockCount"]
moneroblocks["agg"] = moneroblocks["blockCount"]
dogeblocks["agg"] = dogeblocks["blockCount"]

def create_agg(df):
    for i in range(0, len(df["blockCount"])):

        if i == 0:
            df["agg"][i] = df["blockCount"][i]

        if i > 0:
            df["agg"][i] = df["agg"][i - 1] + df["blockCount"][i]

    return df

ethblocks = create_agg(ethblocks)
moneroblocks = create_agg(moneroblocks)
dogeblocks = create_agg(dogeblocks)
zcashblocks = create_agg(zcashblocks)

df = pd.DataFrame({"Ethereum": ethblocks["agg"], "Monero": moneroblocks["agg"],
                   "Dogecoin": dogeblocks["agg"], "ZCash":zcashblocks["agg"]})

bcr.bar_chart_race(df=df, filename='crypto.mp4',n_bars=4,title='daily blocks production PoW cryptocurrencies')