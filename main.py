import os
import speech_recognition as sr
import requests
from tkinter import *
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class StockAnalyzer:
    def __init__(self):
        self.stock_name = None
        self.time_series = None
        self.data = None
        self.date = None
        self.api_key = os.getenv('ALPHAVANTAGE_API_KEY')  # Use API key from environment variables

    def recognize_speech(self, prompt):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print(prompt)
            audio = r.listen(source)
            try:
                return r.recognize_google(audio).lower()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the input.")
                return None
            except sr.RequestError:
                print("Error connecting to the Google Speech Recognition service.")
                return None

    def get_stock_name(self):
        self.stock_name = self.recognize_speech('Speak stock name')
        if self.stock_name:
            print(f"Recognized stock name: {self.stock_name}")
        else:
            print("Stock name recognition failed.")

    def get_time_series(self):
        self.time_series = self.recognize_speech('Speak time series (e.g. daily, weekly, etc.)')
        if self.time_series:
            print(f"Recognized time series: {self.time_series}")
        else:
            print("Time series recognition failed.")

    def fetch_stock_data(self):
        if not self.stock_name or not self.time_series:
            print("Stock name or time series not set. Cannot fetch data.")
            return

        function = f'TIME_SERIES_{self.time_series.upper()}_ADJUSTED'
        symbol = f'{self.stock_name.upper()}.BSE'
        base_url = 'https://www.alphavantage.co/query'
        params = {
            'function': function,
            'symbol': symbol,
            'outputsize': 'full',
            'apikey': self.api_key  # Use environment variable for API key
        }
        r = requests.get(base_url, params=params)

        if r.status_code == 200:
            self.data = r.json()
            if 'Time Series' not in self.data:
                print("Error: No 'Time Series' data found in the API response.")
            else:
                print("Stock data fetched successfully.")
        else:
            print(f"Error fetching data: {r.status_code} - {r.text}")

    def get_stock_price(self):
        self.date = input('Enter the date in the format (yyyy-mm-dd): ')
        if 'Time Series' in self.data:
            time_series_data = self.data['Time Series']
            if self.date in time_series_data:
                stock_prices = time_series_data[self.date]
                print(stock_prices)
            else:
                print(f"No data available for date {self.date}")
        else:
            print("Error: No 'Time Series' data found.")

    def open(self):
        try:
            print(list(self.data.values())[1][self.date]['1. open'])
        except KeyError:
            print("No data available for this date.")

    def high(self):
        try:
            print(list(self.data.values())[1][self.date]['2. high'])
        except KeyError:
            print("No data available for this date.")

    def low(self):
        try:
            print(list(self.data.values())[1][self.date]['3. low'])
        except KeyError:
            print("No data available for this date.")

    def close(self):
        try:
            print(list(self.data.values())[1][self.date]['4. close'])
        except KeyError:
            print("No data available for this date.")

    def volume(self):
        try:
            print(list(self.data.values())[1][self.date]['6. volume'])
        except KeyError:
            print("No data available for this date.")

    def run(self):
        self.get_stock_name()
        if not self.stock_name:
            print("Failed to get stock name. Exiting...")
            return
        
        self.get_time_series()
        if not self.time_series:
            print("Failed to get time series. Exiting...")
            return
        
        self.fetch_stock_data()
        if not self.data:
            print("Failed to fetch stock data. Exiting...")
            return
        
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
if __name__ == "__main__":
    analyzer = StockAnalyzer()
    analyzer.run()