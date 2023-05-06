import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stock_data_analyzer.data_fetch import fetch_stock_data
from stock_data_analyzer.indicators import calculate_moving_averages, calculate_bollinger_bands
from stock_data_analyzer.plotting import plot_stock_data, plot_seasonal_decomposition
from stock_data_analyzer.validation import validate_ticker, validate_date

TICKERS = ['AAPL', 'GOOG', 'MSFT', 'AMZN']


def analyze_stock_data(frame: ttk.Frame, event=None) -> None:
    """
    Analyze stock data by fetching data, calculating indicators, plotting the data,
    and updating the GUI with the results.

    :param frame: The ttk.Frame where the plots will be added.
    :param event: An optional Tkinter event that triggers the function.
    """
    ticker = ticker_combobox.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    if not validate_ticker(ticker):
        result_label['text'] = "Invalid Ticker"
        return

    if not validate_date(start_date) or not validate_date(end_date):
        result_label['text'] = "Invalid Date Format"
        return

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    stock_data = calculate_moving_averages(stock_data)
    stock_data = calculate_bollinger_bands(stock_data)

    plot_width = frame.winfo_width() // 2
    plot_height = frame.winfo_height() - result_label.winfo_height()
    figsize = (plot_width / 80, plot_height / 80)

    fig_stock = plot_stock_data(stock_data, ticker, figsize)
    fig_seasonal = plot_seasonal_decomposition(stock_data, figsize)

    add_plot_to_gui(fig_stock, frame, row=5, column=0)
    add_plot_to_gui(fig_seasonal, frame, row=5, column=1)

    result_label['text'] = "Analysis completed"


def add_plot_to_gui(fig: plt.Figure, frame: ttk.Frame, row: int, column: int) -> None:
    """
    Add a Matplotlib plot to the specified location in the GUI.

    :param fig: The Matplotlib Figure object to add to the GUI.
    :param frame: The ttk.Frame where the plot will be added.
    :param row: The row number in the grid layout where the plot will be added.
    :param column: The column number in the grid layout where the plot will be added.
    """
    canvas = FigureCanvasTkAgg(fig, frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=row, column=column, padx=10,
                       pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))


def create_gui() -> None:
    """
    Create the main GUI for the Stock Data Analyzer application.
    """
    app = tk.Tk()
    app.title("Stock Data Analyzer")

    # Set maximum width and height of the window
    width, height = 1400, 850
    app.maxsize(width, height)
    app.minsize(width, height)

    frame = ttk.Frame(app, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Configure row and column weights for the frame
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    # Configure row and column weights for the widgets in the frame
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(5, weight=1)

    create_widgets(frame)

    app.mainloop()


def create_widgets(frame: ttk.Frame) -> None:
    """
    Create and add widgets to the main GUI frame.

    :param frame: The ttk.Frame where the widgets will be added.
    """
    ticker_label = ttk.Label(frame, text="Ticker:")
    ticker_label.grid(column=0, row=0, sticky=tk.W)
    global ticker_combobox
    ticker_combobox = ttk.Combobox(frame, values=TICKERS)
    ticker_combobox.set(TICKERS[0])  # Set default ticker value
    ticker_combobox.grid(column=1, row=0, sticky=tk.W)

    start_date_label = ttk.Label(frame, text="Start Date (YYYY-MM-DD):")
    start_date_label.grid(column=0, row=1, sticky=tk.W)
    global start_date_entry
    start_date_entry = ttk.Entry(frame)
    start_date_entry.insert(0, "2021-01-01")  # Set default start date
    start_date_entry.grid(column=1, row=1, sticky=tk.W)

    end_date_label = ttk.Label(frame, text="End Date (YYYY-MM-DD):")
    end_date_label.grid(column=0, row=2, sticky=tk.W)
    global end_date_entry
    end_date_entry = ttk.Entry(frame)
    end_date_entry.insert(0, "2021-12-31")  # Set default end date
    end_date_entry.grid(column=1, row=2, sticky=tk.W)

    analyze_button = ttk.Button(
        frame, text="Analyze", command=lambda: analyze_stock_data(frame))
    analyze_button.grid(column=1, row=3, pady="10")

    global result_label
    result_label = ttk.Label(frame, text="")
    result_label.grid(column=0, row=4, columnspan=2, pady="10")


if __name__ == "__main__":
    create_gui()
