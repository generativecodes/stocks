import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def plot_stock_data(data: pd.DataFrame, ticker: str, figsize=(6, 4)) -> plt.Figure:
    """
    Plot stock data with moving averages and Bollinger Bands.

    :param data: DataFrame containing stock data.
    :param ticker: Stock ticker symbol.
    :param show: Whether to show the plot or not.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(data.index, data['Close'],
            label='Close', color='blue', linewidth=0.5)
    plt.plot(data.index, data['SMA_20'],
             label='SMA 20', color='red', linewidth=0.5)
    plt.plot(data.index, data['SMA_50'],
             label='SMA 50', color='green', linewidth=0.5)
    plt.plot(data.index, data['BB_upper'],
             label='Bollinger Bands', linestyle='--', color='grey', linewidth=0.5)
    plt.plot(data.index, data['BB_lower'],
             linestyle='--', color='grey', linewidth=0.5)
    plt.legend()

    plt.title(
        f'{ticker} Stock Price with Moving Averages and Bollinger Bands', fontsize=10)
    # plt.xlabel('Date', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    ax.tick_params(axis='both', which='major', labelsize=6)
    fig.tight_layout()
    return fig


def plot_seasonal_decomposition(data: pd.DataFrame, figsize=(6, 8)) -> plt.Figure:
    """
    Plot seasonal decomposition components for the given stock data.

    :param data: DataFrame containing stock data.
    :param show: Whether to show the plot or not.
    """
    decomposition = seasonal_decompose(
        data['Close'], model='multiplicative', period=252)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=figsize)
    ax1.plot(data.index, trend, label='Trend', color='blue', linewidth=0.5)
    ax2.plot(data.index, seasonal, label='Seasonality',
             color='green', linewidth=0.5)
    ax3.plot(data.index, residual, label='Residuals',
             color='red', linewidth=0.5)

    # Add vertical titles to the right side of each subplot
    for ax, title in zip([ax1, ax2, ax3], ['Trend Component', 'Seasonal Component', 'Residual Component']):
        ax.text(1.02, 0.5, title, fontsize=8, rotation=90,
                transform=ax.transAxes, ha='left', va='center')

    for ax in [ax1, ax2, ax3]:
        ax.tick_params(axis='both', which='major', labelsize=6)

    fig.tight_layout()
    return fig
