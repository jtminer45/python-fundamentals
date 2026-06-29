import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Pull 1 year of real stock data for 5 companies: Apple, Google, Microsoft, Amazon, Tesla using yfinance
apple = yf.download("AAPL", period="1y", auto_adjust=True)
google = yf.download("GOOGL", period="1y", auto_adjust=True)
microsoft = yf.download("MSFT", period="1y", auto_adjust=True)
amazon = yf.download("AMZN", period="1y", auto_adjust=True)
tesla = yf.download("TSLA", period="1y", auto_adjust=True)

# Flatten columns for all dataframes
apple.columns = apple.columns.get_level_values(0)
google.columns = google.columns.get_level_values(0)
microsoft.columns = microsoft.columns.get_level_values(0)
amazon.columns = amazon.columns.get_level_values(0)
tesla.columns = tesla.columns.get_level_values(0)

# Line plot — closing prices for all 5 companies on one chart, each a different colour, with a legend
plt.figure(figsize=(12, 6))
plt.plot(apple.index, apple["Close"], label="Apple", color="blue")
plt.plot(google.index, google["Close"], label="Google", color="red")
plt.plot(microsoft.index, microsoft["Close"], label="Microsoft", color="green")
plt.plot(amazon.index, amazon["Close"], label="Amazon", color="orange")
plt.plot(tesla.index, tesla["Close"], label="Tesla", color="purple")
plt.title("Stock Closing Prices - Last 12 Months")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("closing_prices.png")
plt.show()

# Bar chart — average closing price per company over the year
plt.figure(figsize=(8, 6))
plt.bar(["Apple", "Google", "Microsoft", "Amazon", "Tesla"],
        [apple["Close"].mean(), google["Close"].mean(), microsoft["Close"].mean(),
 amazon["Close"].mean(), tesla["Close"].mean()],
        color=["blue", "red", "green", "orange", "purple"])
plt.title("Average Closing Price per Company - Last 12 Months")
plt.xlabel("Company")
plt.ylabel("Average Closing Price (USD)")
plt.tight_layout()
plt.savefig("average_closing_prices.png")
plt.show()

# Scatter plot — Apple's volume vs closing price
plt.figure(figsize=(8, 6))
plt.scatter(apple["Volume"], apple["Close"], alpha=0.7, s=100)
plt.title("Apple's Volume vs Closing Price")
plt.xlabel("Volume")
plt.ylabel("Closing Price (USD)")
plt.tight_layout()
plt.savefig("apple_volume_vs_closing_price.png")
plt.show()

# Correlation heatmap — closing prices between all 5 companies
correlation = pd.DataFrame({
    "Apple": apple["Close"],
    "Google": google["Close"],
    "Microsoft": microsoft["Close"],
    "Amazon": amazon["Close"],
    "Tesla": tesla["Close"]
}).corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()


# Save every chart as a PNG file
#All charts must have titles, axis labels, and legends where appropriate


