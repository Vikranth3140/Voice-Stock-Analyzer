Voice Stock Analyzer
====================

Voice Stock Analyzer is a Python-based tool that allows users to analyze stock data using speech recognition and the [Alpha Vantage](https://www.alphavantage.co/) API.

<img width="607" alt="Screenshot 2024-03-17 145532" src="https://github.com/Vikranth3140/Voice-Stock-Analyzer/assets/122410275/873d3cc1-804b-493a-b2da-9e36b035902d">

Features
--------

*   **Speech Recognition:** Input stock name and time series using speech commands.
*   **Stock Data Fetching:** Fetch stock data from Alpha Vantage API based on user input.
*   **Stock Price Analysis:** Analyze stock prices for open, high, low, close, and volume for a specified date.
*   **GUI Interface:** User-friendly graphical interface for easy interaction.

Requirements
------------

*   Python 3.x
*   SpeechRecognition library
*   Requests library
*   Alpha Vantage API key (premium subscription required)

How to Use
----------

1.  Clone the repository to your local machine.

    ```bash
    git clone https://github.com/Vikranth3140/Voice-Stock-Analyzer.git
    ```

2.  Install the required libraries.

    ```bash
    pip install -r requirements.txt
    ```

3.  Obtain an API key from Alpha Vantage and update it in the code.
4.  Run the program.

    ```bash
    python main.py
    ```

5.  Speak the stock name, time series, and date as prompted.
6.  Use the GUI interface to view stock prices and other details.

Note
----

Please note that the features require an Alpha Vantage premium subscription to access the API endpoints.

Visit [Alpha Vantage](https://www.alphavantage.co/premium/) to subscribe to a premium plan and unlock all premium features.

License
-------

This project is licensed under the [MIT LICENSE](LICENSE).
