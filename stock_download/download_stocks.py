import pandas as pd
import numpy as np
import yfinance as yf

def DownloadStockInformation(stocks, start, end):
    if not isinstance(stocks, list) and not isinstance(stocks, str): raise Exception('"stocks" should be a list or a string')
    if not isinstance(start, str): raise Exception('"start" should be a string')
    if not isinstance(end, str): raise Exception('"end" should be a string')
    data = yf.download(stocks, start=start, end=end)
    return data
