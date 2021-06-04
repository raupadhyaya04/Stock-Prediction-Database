import pandas as pd
import yfinance as yf

class AnalyzeStock:
  def __init__(self):
    Ticker_data = _getTickers
    Name_data = _getNames 

  def Analyze(self,ticker_list,corporation_list=None):
    "Does analaysis of stocks based on list of names or ticker id's"
    "Part 1: Take only ticker or corporation lists"
    "Part 2: Efficiently run analysis for all tickers in list (Pandas and lambda fucntions)"
    "Part 3: Return conclusions of analysis"
    pass

  def _getTickers(self):
      
    
  
  def _getNames(self):
    pass 


# On Balance Volume calculator more functions coming
# Need to arrange it into class format

# def OnBalanceVolume(ticker):
#   volumeYesterday, volumeToday = ticker.history('2d')['Volume'][0], ticker.history('2d')['Volume'][1]
#   if volumeYesterday >= volumeToday:
#     obv = volumeYesterday
#   else:
#     obv = volumeToday
#   return obv 