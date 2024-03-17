import speech_recognition as sr
import requests
import json
from tkinter import *

class StockAnalyzer:
    def __init__(self):
        self.stock_name = None
        self.time_series = None
        self.data = None
        self.date = None

    def get_stock_name(self):
        print('Speak stock name')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            self.stock_name = r.recognize_google(audio).lower()
            print(self.stock_name)

    def get_time_series(self):
        print('Speak time series')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            self.time_series = r.recognize_google(audio).lower()
            print(self.time_series)

    def fetch_stock_data(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{self.time_series}_ADJUSTED&symbol={self.stock_name}.BSE&outputsize=full&apikey=X6IQZUMIBD421RAY'
        r = requests.get(url)
        self.data = r.json()
        print(self.data)

    def get_stock_price(self):
        date = input('Enter the date in the format (yyyy-mm-dd): ')
        self.date = date
        stock_prices = list(list(self.data.values()))[1][date]
        print(stock_prices)

    def open(self):
        print(list(self.data.values())[1][self.date]['1. open'])

    def high(self):
        print(list(self.data.values())[1][self.date]['2. high'])

    def low(self):
        print(list(self.data.values())[1][self.date]['3. low'])

    def close(self):
        print(list(self.data.values())[1][self.date]['4. close'])

    def volume(self):
        print(list(self.data.values())[1][self.date]['6. volume'])

    def run(self):
        self.get_stock_name()
        self.get_time_series()
        self.fetch_stock_data()
        self.get_stock_price()

        top = Tk()
        top.geometry("100x300")

        b1 = Button(top, text="OPEN", command=self.open, activeforeground="black", activebackground="pink", pady=10)
        b2 = Button(top, text="HIGH", command=self.high, activeforeground="black", activebackground="pink", pady=10)
        b3 = Button(top, text="LOW", command=self.low, activeforeground="black", activebackground="pink", pady=10)
        b4 = Button(top, text="CLOSE", command=self.close, activeforeground="black", activebackground="pink", pady=10)
        b5 = Button(top, text="VOLUME", command=self.volume, activeforeground="black", activebackground="pink", pady=10)
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
        b5.pack()
        top.mainloop()

# Create an instance of the StockAnalyzer class and run the program
analyzer = StockAnalyzer()
analyzer.run()