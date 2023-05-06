
import pandas as pd


def calculate_moving_averages(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate simple moving averages for the given stock data.

    :param data: DataFrame containing stock data.
    :return: DataFrame with added columns for simple moving averages.
    """
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    return data


def calculate_bollinger_bands(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Bollinger Bands for the given stock data.

    :param data: DataFrame containing stock data.
    :return: DataFrame with added columns for Bollinger Bands.
    """
    data['BB_upper'] = data['SMA_20'] + 2 * \
        data['Close'].rolling(window=20).std()
    data['BB_lower'] = data['SMA_20'] - 2 * \
        data['Close'].rolling(window=20).std()
    return data
