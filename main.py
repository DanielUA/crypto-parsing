import requests
import json


YO_BIT_API_BASE_URL = "https://yobit.net/api/3/"
INFO_FILE = "info.txt"
TICKER_FILE = "ticker.txt"
DEPTH_FILE = "depth.txt"
TRADES_FILE = "trades.txt"


class HttpError(Exception):
    pass


def get_info():
    try:
        response = requests.get(url=f"{YO_BIT_API_BASE_URL}info")
        response.raise_for_status()
        with open(INFO_FILE, "w") as file:
            file.write(response.text)
        return response.text
    except requests.exceptions.RequestException as err:
        raise HttpError(f"Error fetching info: {err}")


def get_ticker(coin_1="btc", coin_2="usdt"):
    try:
        response = requests.get(url=f"{YO_BIT_API_BASE_URL}ticker/{coin_1}_{coin_2}")
        response.raise_for_status()
        with open(TICKER_FILE, "w") as file:
            file.write(response.text)
        return response.text
    except requests.exceptions.RequestException as err:
        raise HttpError(f"Error fetching ticker: {err}")


def get_depth(coin_1="eth", coin_2="usdt", limit=150):
    try:
        response = requests.get(
            url=f"{YO_BIT_API_BASE_URL}depth/{coin_1}_{coin_2}?limit={limit}&ignore_invalid=1"
        )
        response.raise_for_status()

        with open(DEPTH_FILE, "w") as file:
            file.write(response.text)

        bids = response.json()[f"{coin_1}_{coin_2}"]["bids"]

        total_bids_amount = 0
        for item in bids:
            price = item[0]
            coin_amount = item[1]
            total_bids_amount += price * coin_amount

        return f"Total bids for {coin_1}: {total_bids_amount:.2f} USD"
    except requests.exceptions.RequestException as err:
        raise HttpError(f"Error fetching depth: {err}")


def get_trades(coin_1="eth", coin_2="usdt", limit=150):
    try:
        response = requests.get(
            url=f"{YO_BIT_API_BASE_URL}trades/{coin_1}_{coin_2}?limit={limit}&ignore_invalid=1"
        )
        response.raise_for_status()

        with open(TRADES_FILE, "w") as file:
            file.write(response.text)

        total_trade_ask = 0
        total_trade_bid = 0

        for item in response.json()[f"{coin_1}_{coin_2}"]:
            if item["type"] == "ask":
                total_trade_ask += item["price"] * item["amount"]
            else:
                total_trade_bid += item["price"] * item["amount"]

        return (
            f"[-] Total {coin_1} Sell: {round(total_trade_ask, 2)} USD\n"
            f"[+] Total {coin_1} Buy: {round(total_trade_bid, 2)} USD"
        )
    except requests.exceptions.RequestException as err:
        raise HttpError(f"Error fetching trades: {err}")

def main():
    try:
        # Uncomment desired functions
        # print(get_info())
        # print(get_ticker())
        # print(get_depth())
        print(get_trades(limit=2000))
    except HttpError as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()
