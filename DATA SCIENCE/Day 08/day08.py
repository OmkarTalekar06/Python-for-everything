import yfinance as yf
import matplotlib.pyplot as plt

stock_name = "TCS.NS"
stock_date = "2022-01-01"

data = yf.download(stock_name, start=stock_date)
print(data.head())

plt.plot(data["Close"])
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Close Price")
plt.show()

