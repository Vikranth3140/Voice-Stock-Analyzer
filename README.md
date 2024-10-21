Voice Stock Analyzer
====================

Voice Stock Analyzer is a Python-based tool that allows users to analyze stock data using speech recognition and the [Alpha Vantage](https://www.alphavantage.co/) API.

<img width="607" alt="Screenshot 2024-03-17 145532" src="https://github.com/Vikranth3140/Voice-Stock-Analyzer/assets/122410275/873d3cc1-804b-493a-b2da-9e36b035902d">

Features
--------

* **Speech Recognition:** Input stock name and time series using speech commands.
* **Stock Data Fetching:** Fetch stock data from Alpha Vantage API based on user input.
* **Stock Price Analysis:** Analyze stock prices for open, high, low, close, and volume for a specified date.
* **GUI Interface:** User-friendly graphical interface for easy interaction.

Requirements
------------

* Python 3.x
* `SpeechRecognition` library
* `requests` library
* `python-dotenv` library
* Alpha Vantage API key (premium subscription required)

How to Use
----------

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/Vikranth3140/Voice-Stock-Analyzer.git
    ```

2. Install the required libraries.

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root directory and add your Alpha Vantage API key as follows:

    ```bash
    ALPHAVANTAGE_API_KEY=your_api_key_here
    ```

4. Run the program.

    ```bash
    python main.py
    ```

5. Speak the stock name (e.g., "tata motors"), time series (e.g., "daily"), and date as prompted.

6. Use the GUI interface to view stock prices and other details.

Example
-------

Here is an example of how to run the Voice Stock Analyzer:

1. After running the program, speak the stock name when prompted (e.g., "reliance industries").
2. When prompted for the time series, speak the desired time frame (e.g., "weekly").
3. Enter a specific date in the format `yyyy-mm-dd` to analyze stock data for that day.
4. Use the graphical interface buttons to check the stock's open, high, low, close, or volume for the given date.

```bash
$ python main.py
Speak stock name
> reliance industries
Speak time series
> weekly
Enter the date in the format (yyyy-mm-dd): 
> 2024-03-01
```

**Output in GUI:**
- Open price: ₹2500.00
- High price: ₹2520.50
- Low price: ₹2475.00
- Close price: ₹2510.25
- Volume: 1,200,000

Note
----

Please note that the features require an Alpha Vantage premium subscription to access the API endpoints.

Visit [Alpha Vantage](https://www.alphavantage.co/premium/) to subscribe to a premium plan and unlock all premium features.

License
-------

This project is licensed under the [MIT LICENSE](LICENSE).
