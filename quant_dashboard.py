# Save as quant_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Quant Portfolio Risk Dashboard")

# ------------------ User Inputs ------------------
st.sidebar.header("Portfolio Inputs")
tickers_input = st.sidebar.text_input("Tickers (comma-separated, e.g., HSBA.L,BARC.L,BP.L)", "HSBA.L,BARC.L,BP.L")
tickers = [t.strip() for t in tickers_input.split(",")]

# Initialize default equal weights if not provided
weights_default = [round(1/len(tickers), 2)]*len(tickers)
weights_input = st.sidebar.text_input(f"Weights (sum=1, comma-separated)", ",".join(map(str, weights_default)))
weights = np.array([float(w.strip()) for w in weights_input.split(",")])

portfolio_value = st.sidebar.number_input("Portfolio Value (£)", value=1_000_000, step=10_000)
risk_limit = st.sidebar.number_input("Risk Limit (£)", value=100_000, step=10_000)
confidence_level = st.sidebar.slider("Confidence Level (%)", 90, 99, 95)/100
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2025-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2025-09-19"))
simulations = st.sidebar.number_input("Monte Carlo Simulations", value=10000, step=1000)

# ------------------ Download Data ------------------
data_load_state = st.text("Downloading historical data...")
data = yf.download(tickers, start=start_date, end=end_date, progress=False)
data_load_state.text("✅ Data downloaded!")

# Handle Adj Close / Close
if isinstance(data.columns, pd.MultiIndex):
    if 'Adj Close' in data.columns.levels[0]:
        adj_close = data['Adj Close']
    else:
        adj_close = data['Close']
else:
    adj_close = data

returns = adj_close.pct_change(fill_method=None).dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()

# ------------------ Interactive Sliders for Weights ------------------
st.sidebar.subheader("Adjust Weights")
for i, ticker in enumerate(tickers):
    w = st.sidebar.slider(f"{ticker} weight", 0.0, 1.0, float(weights[i]), 0.01)
    weights[i] = w
weights = weights / weights.sum()  # normalize to sum=1

# ------------------ Portfolio Calculations ------------------
# Portfolio historical returns
portfolio_returns = returns.dot(weights)

# Historical VaR & CVaR
hist_var = abs(np.percentile(portfolio_returns, 100*(1-confidence_level))*portfolio_value)
hist_cvar = abs(portfolio_returns[portfolio_returns <= np.percentile(portfolio_returns, 100*(1-confidence_level))].mean()*portfolio_value)

# Monte Carlo simulation using GBM
np.random.seed(42)
T = 1/252  # 1-day
simulated_returns = np.zeros(simulations)
S0 = adj_close.iloc[-1].values  # latest prices
mu = mean_returns.values
sigma = returns.std().values

for i in range(simulations):
    Z = np.random.normal(0, 1, len(tickers))
    ST = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    simulated_returns[i] = np.dot((ST - S0)/S0, weights)

mc_var = abs(np.percentile(simulated_returns, 100*(1-confidence_level))*portfolio_value)
mc_cvar = abs(simulated_returns[simulated_returns <= np.percentile(simulated_returns, 100*(1-confidence_level))].mean()*portfolio_value)

# Risk Contribution
annualized_cov = cov_matrix*252
port_vol = np.sqrt(weights.T @ annualized_cov @ weights)
marginal_contrib = annualized_cov @ weights / port_vol
risk_contribution = weights * marginal_contrib * portfolio_value
riskiest_stock = tickers[np.argmax(risk_contribution)]

# Hedging suggestion
stock_price = adj_close[riskiest_stock].iloc[-1]
delta = 0.5
shares = (weights[np.argmax(risk_contribution)] * portfolio_value)/stock_price
options_needed = shares/delta

# ------------------ Display Results ------------------
st.subheader("📑 Summary Report")
st.write(f"Portfolio Historical VaR ({int(confidence_level*100)}%, 1-day): £{hist_var:,.2f}")
st.write(f"Portfolio Historical CVaR ({int(confidence_level*100)}%, 1-day): £{hist_cvar:,.2f}")
st.write(f"Portfolio Monte Carlo VaR ({int(confidence_level*100)}%, 1-day): £{mc_var:,.2f}")
st.write(f"Portfolio Monte Carlo CVaR ({int(confidence_level*100)}%, 1-day): £{mc_cvar:,.2f}")
st.write(f"Riskiest Stock: {riskiest_stock}")
st.write(f"Hedging Recommendation: Buy {options_needed:,.0f} put options on {riskiest_stock}")

st.subheader("📊 Risk Contributions")
risk_df = pd.DataFrame({"Ticker": tickers, "Risk Contribution (£)": risk_contribution})
st.dataframe(risk_df)

# ------------------ Plots ------------------
st.subheader("📈 Portfolio Returns Distribution")
fig, ax = plt.subplots(figsize=(10,6))
ax.hist(portfolio_returns*portfolio_value, bins=50, alpha=0.7, color='blue', label='Historical Returns')
ax.hist(simulated_returns*portfolio_value, bins=50, alpha=0.3, color='green', label='Monte Carlo Returns')
ax.axvline(x=-hist_var, color='red', linestyle='--', label=f'Historical VaR (£{hist_var:,.2f})')
ax.axvline(x=-hist_cvar, color='orange', linestyle='--', label=f'Historical CVaR (£{hist_cvar:,.2f})')
ax.axvline(x=-mc_var, color='darkred', linestyle='--', label=f'Monte Carlo VaR (£{mc_var:,.2f})')
ax.axvline(x=-mc_cvar, color='darkorange', linestyle='--', label=f'Monte Carlo CVaR (£{mc_cvar:,.2f})')
ax.set_xlabel("Portfolio P&L (£)")
ax.set_ylabel("Frequency")
ax.legend()
st.pyplot(fig)

# ------------------ Export Options ------------------
if st.button("📥 Export Summary to CSV"):
    summary = pd.DataFrame({
        "Metric": ["Historical VaR", "Historical CVaR", "Monte Carlo VaR", "Monte Carlo CVaR", "Riskiest Stock", "Put Options Needed"],
        "Value": [f"£{hist_var:,.2f}", f"£{hist_cvar:,.2f}", f"£{mc_var:,.2f}", f"£{mc_cvar:,.2f}", riskiest_stock, f"{options_needed:,.0f}"]
    })
    summary.to_csv("portfolio_risk_summary.csv", index=False)
    st.success("✅ Summary exported as 'portfolio_risk_summary.csv'")
