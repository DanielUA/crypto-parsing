# crypto-parsing Yobit API

## Description
This script retrieves data from the Yobit cryptocurrency exchange API. It provides functionality to fetch exchange information, get ticker data for specified cryptocurrencies, check the market depth, and retrieve recent trades for a given pair of cryptocurrencies.

## Requirements
- Python 3.6 or higher
- `requests` library (`pip install requests`)

## Functions
- `get_info()`: Retrieves general information from the Yobit API and saves it to `info.txt`.
- `get_ticker(coin_1="btc", coin_2="usdt")`: Retrieves ticker information for a specified pair of cryptocurrencies and saves it to `ticker.txt`.
- `get_depth(coin_1="eth", coin_2="usdt", limit=150)`: Retrieves market depth for a specified pair of cryptocurrencies with a given limit and saves it to `depth.txt`. It also calculates the total value of bids.
- `get_trades(coin_1="eth", coin_2="usdt", limit=150)`: Retrieves the most recent trades for a specified pair of cryptocurrencies and saves it to `trades.txt`. It calculates the total value for "ask" and "bid" trades.

## How to Use
1. Clone the repository or download the script.
2. Ensure Python and the required libraries are installed.
3. Run the script using `python script_name.py`.
4. To customize the parameters, edit the function calls in the `main()` function.