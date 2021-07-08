class Strategy: 
  def __init__(self,Strategy_Name,show_plots=False):
    self.MACD_RSI()



    def MACD_RSI(): 
      """
      Implements a simple RSI (Relative Strength Index) and MACD (Moving Average Convergence Divergence) Strategy.
      1. Buy signal if longer MACD is under #check shorter MACD and RSI is overbought
      2. Sell signal if longer MACD is over shorter MACD and RSI is underbought. 
      """
      pass