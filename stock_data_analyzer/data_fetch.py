import os
import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch stock data using yfinance library. Save data to a CSV file, and update
    only the new data points when called again.

    :param ticker: Stock ticker symbol.
    :param start_date: Start date for fetching stock data in 'YYYY-MM-DD' format.
    :param end_date: End date for fetching stock data in 'YYYY-MM-DD' format.
    :return: DataFrame containing stock data.
    """
    file_path = get_file_path(ticker)
    data = load_existing_data(file_path, end_date)

    if data is None:
        data = fetch_and_save_data(ticker, start_date, end_date, file_path)

    return data


def get_file_path(ticker: str) -> str:
    """
    Get the file path for the stock data CSV file.

    :param ticker: Stock ticker symbol.
    :return: File path as a string.
    """
    data_folder = "data"

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    file_path = f"data/{ticker}_stock_data.csv"
    return file_path


def load_existing_data(file_path: str, end_date: str) -> pd.DataFrame:
    """
    Load existing stock data from the CSV file if it exists and is up-to-date.

    :param file_path: File path of the stock data CSV file.
    :param end_date: End date for fetching stock data in 'YYYY-MM-DD' format.
    :return: DataFrame containing stock data if it exists and is up-to-date, None otherwise.
    """
    if os.path.exists(file_path):
        data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        last_date = data.index[-1].strftime('%Y-%m-%d')

        if last_date < end_date:
            return None
        else:
            return data
    else:
        return None


def fetch_and_save_data(ticker: str, start_date: str, end_date: str, file_path: str) -> pd.DataFrame:
    """
    Fetch stock data using the yfinance library and saves it to a CSV file.

    :param ticker: Stock ticker symbol.
    :param start_date: Start date for fetching stock data in 'YYYY-MM-DD' format.
    :param end_date: End date for fetching stock data in 'YYYY-MM-DD' format.
    :param file_path: File path of the stock data CSV file.
    :return: DataFrame containing fetched stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(file_path)
    return data
