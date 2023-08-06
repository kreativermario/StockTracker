import yfinance as yf
import tkinter as tk
from tkinter import messagebox


class App:

    def __init__(self):

        # Create the main application window
        self.previous_close_label = None
        self.exchange_label = None
        self.price_label = None
        self.country_label = None
        self.name_label = None
        self.search_button = None
        self.ticker_entry = None
        self.ticker_label = None

        self.frame = tk.Tk()
        self.init_frame()
        # Start the main event loop
        self.frame.mainloop()

    def init_frame(self):
        self.frame.title("Stock Portfolio Tracker")

        # Create and arrange widgets
        self.ticker_label = tk.Label(self.frame, text="Enter Ticker Symbol:")
        self.ticker_label.pack()

        self.ticker_entry = tk.Entry(self.frame)
        self.ticker_entry.pack()

        self.search_button = tk.Button(self.frame, text="Search", command=self.get_stock_data)
        self.search_button.pack()

        self.name_label = tk.Label(self.frame, text="Name: ")
        self.name_label.pack()

        self.price_label = tk.Label(self.frame, text="Price: ")
        self.price_label.pack()

        self.previous_close_label = tk.Label(self.frame, text='Previous Close: ')
        self.previous_close_label.pack()

        self.country_label = tk.Label(self.frame, text="Country: ")
        self.country_label.pack()

        self.exchange_label = tk.Label(self.frame, text="Exchange: ")
        self.exchange_label.pack()

    def get_stock_data(self):
        ticker = self.ticker_entry.get().upper()
        try:
            stock = yf.Ticker(ticker)
            # get stock info
            stock_info = stock.info

            # debug items in info
            for item in stock_info:
                print(item)

            self.name_label.config(text="Name: " +
                                        stock_info['longName'])
            self.country_label.config(text="Country: " +
                                           stock_info['country'])
            self.previous_close_label.config(text="Previous close: " +
                                                  str(stock_info['currentPrice'])
                                                  + ' ' +
                                                  stock_info['currency']
                                             )
            self.price_label.config(text="Price: " +
                                         str(stock_info['currentPrice']) + ' ' +
                                         stock_info['currency'])
            self.exchange_label.config(text="Exchange: " + stock_info['exchange'])
        # TODO - change to custom exception!
        except Exception as e:
            messagebox.showerror("Error", "Invalid ticker symbol or connection error!")


App()