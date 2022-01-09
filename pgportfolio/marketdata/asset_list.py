import pandas as pd
import time
from datetime import datetime

colnames = ["date", "pre_close", "open", "high", "low", "close", "volume", "amt"]

def parse_time(time_string):
    return time.mktime(datetime.strptime(time_string, "%Y-%m-%d").timetuple())

def get_data(asset, start, end):
    chart = {}
    df = pd.read_csv(f"WindIndexData/MarketData/{asset}.WI.csv", header=None, names=colnames, skiprows=1)
    df["date"] = df["date"].apply(parse_time)
    df_out = df[df["date"] >= start]
    df_out = df_out[df_out["date"] <= end]
    #df_out["date"] = df_out["date"].astype(int)
    #print("Start: ", start, end)
    return df_out