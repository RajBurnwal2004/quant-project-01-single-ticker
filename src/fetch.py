"""Fetch daily price history for a single ticker using yfinance."""
import yfinance as yf
import pandas as pd

TICKER = "AAPL"
START = "2020-01-01"
END = "2024-12-31"


def fetch_prices(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Download daily OHLCV data for one ticker."""
    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False,
        multi_level_index=False,  # flatten columns in yfinance >= 1.0
    )
    if df.empty:
        raise ValueError(f"No data returned for {ticker}")
    return df


def print_summary(df: pd.DataFrame, ticker: str) -> None:
    """Print min/max/avg close and total return over the period."""
    close = df["Close"]
    total_return = (close.iloc[-1] / close.iloc[0] - 1) * 100

    print(f"\n=== {ticker} summary ===")
    print(f"Rows:           {len(df)}")
    print(f"Date range:     {df.index.min().date()} -> {df.index.max().date()}")
    print(f"Min close:      {close.min():.2f}")
    print(f"Max close:      {close.max():.2f}")
    print(f"Avg close:      {close.mean():.2f}")
    print(f"Total return:   {total_return:.2f}%")


if __name__ == "__main__":
    prices = fetch_prices(TICKER, START, END)
    print_summary(prices, TICKER)
    prices.to_csv("data/aapl.csv")
    print("\nSaved raw data to data/aapl.csv")
