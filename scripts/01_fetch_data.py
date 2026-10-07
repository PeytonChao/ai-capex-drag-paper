import pandas as pd
import yfinance as yf

SOFTWARE_TICKERS = ["MSFT", "ORCL", "CRM", "ADBE", "PANW", "SNOW", "NOW", "PLTR"]
HARDWARE_TICKERS = ["NVDA", "AMD", "AVGO", "INTC", "CSCO", "AMAT", "MU", "DELL"]

def fetch_ticker_data(ticker, is_software):
    stock = yf.Ticker(ticker)
    financials = stock.quarterly_financials.T
    cashflow = stock.quarterly_cashflow.T
    balance = stock.quarterly_balance_sheet.T
    
    df = pd.DataFrame()
    df['Operating_Income'] = financials.get('Operating Income', pd.Series())
    df['Total_Revenue'] = financials.get('Total Revenue', pd.Series())
    df['RD_Expense'] = financials.get('Research And Development', pd.Series())
    df['CapEx'] = cashflow.get('Capital Expenditure', pd.Series()).abs()
    df['Total_Assets'] = balance.get('Total Assets', pd.Series())
    df['Total_Liabilities'] = balance.get('Total Liabilities Net Minority Interest', pd.Series())
    df['Total_Equity'] = balance.get('Stockholders Equity', pd.Series())
    
    df['Ticker'] = ticker
    df['Is_Software'] = 1 if is_software else 0
    return df

all_data = []
for ticker in SOFTWARE_TICKERS:
    all_data.append(fetch_ticker_data(ticker, is_software=True))
for ticker in HARDWARE_TICKERS:
    all_data.append(fetch_ticker_data(ticker, is_software=False))

panel_raw = pd.concat(all_data)
panel_raw.to_csv("data/raw_financials.csv")
print("Raw data successfully saved to data/raw_financials.csv")
