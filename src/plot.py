"""Plot closing price for a ticker from a saved CSV."""
import pandas as pd
import matplotlib.pyplot as plt

TICKER = "AAPL"
CSV_PATH = "data/aapl.csv"
OUT_PATH = "plots/aapl_close.png"


def load_prices(path: str) -> pd.DataFrame:
    """Load a price CSV saved by fetch.py, indexed by date."""
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df


def plot_close(df: pd.DataFrame, ticker: str, out_path: str) -> None:
    """Save a line chart of the closing price."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df["Close"], linewidth=1.2, color="steelblue")
    ax.set_title(f"{ticker} closing price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    print(f"Saved plot to {out_path}")


if __name__ == "__main__":
    df = load_prices(CSV_PATH)
    plot_close(df, TICKER, OUT_PATH)
