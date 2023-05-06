import re
from datetime import datetime


def validate_ticker(ticker: str) -> bool:
    """
    Check if the input ticker is valid.

    :param ticker: Stock ticker symbol.
    :return: True if the ticker is valid, False otherwise.
    """
    return re.match(r"^[A-Z]{1,5}$", ticker) is not None


def validate_date(date: str) -> bool:
    """
    Check if the input date is valid and in the correct format (YYYY-MM-DD).

    :param date: Date string in 'YYYY-MM-DD' format.
    :return: True if the date is valid, False otherwise.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
