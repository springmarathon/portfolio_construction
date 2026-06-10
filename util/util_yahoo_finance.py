import numpy as np
import yfinance as yf


def get_returns(tickers: list[str], start: str, end: str = None):
    """
    Download adjusted daily returns and compute the annualized covariance matrix.

    Parameters
    ----------
    tickers : list of ticker strings
    start   : start date, e.g. "2020-01-01"
    end     : end date (defaults to today)

    Returns
    -------
    returns : DataFrame of daily log returns, shape (T, n)
    cov     : annualized covariance matrix as np.ndarray, shape (n, n)
    """

    # auto_adjust=True (the default) back-adjusts all historical prices for splits and dividends,
    # so returns are clean total returns with no gaps at ex-dividend dates.
    prices = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)["Close"]
    prices = prices[tickers]   # enforce column order

    # Log returns: more additive across time than simple returns
    returns = np.log(prices / prices.shift(1)).dropna()

    return returns


def get_latest_prices(tickers: list[str]) -> dict[str, float]:
    prices = yf.download(tickers, period="5d", auto_adjust=True, progress=False)["Close"]
    latest = prices.squeeze().ffill().iloc[-1]
    if hasattr(latest, "items"):
        return {t: float(latest[t]) for t in tickers}
    return {tickers[0]: float(latest)}


def get_market_caps(tickers: list[str]) -> dict[str, float]:
    caps = {}
    for t in tickers:
        info = yf.Ticker(t).info
        mc = info.get("marketCap")
        if mc is None:
            raise ValueError(f"market cap unavailable for {t}")
        caps[t] = mc
    return caps