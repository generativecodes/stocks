# Stock Data Analyzer

Stock Data Analyzer is a Python-based application that allows users to analyze stock data, calculate various indicators, and visualize the results using interactive plots. The application uses a simple graphical user interface (GUI) built with Tkinter.

![Stock Data Analyzer Screenshot](screenshot.png)

## Features

- Fetch stock data using the yfinance library
- Calculate simple moving averages (SMA) and Bollinger Bands
- Visualize stock data with moving averages and Bollinger Bands
- Perform seasonal decomposition of stock data
- Validate user input for stock ticker and date range

## Installation

1. Clone the repository:

```bash
git clone https://github.com/generativecodes/stocks.git
cd stocks
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to start the Stock Data Analyzer GUI:

```bash
python main.py
```

Follow these steps to analyze stock data:

1. Select a stock ticker from the dropdown menu or type in a custom ticker
2. Enter the start date (YYYY-MM-DD) and end date (YYYY-MM-DD) for fetching stock data
3. Click the "Analyze" button to fetch stock data, calculate indicators, and display the plots

## Dependencies

- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
