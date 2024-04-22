import requests
import json

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    with open("info.txt", "w") as file:
        file.write(response.text)
    
    return response.text


def get_ticker(coin_1="btc", coin_2="usdt"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin_1}_{coin_2}")
    
    with open("ticker.txt", "w") as file:
        file.write(response.text)

    return response.text

def get_depth(coin_1="eth", coin_2="usdt", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin_1}_{coin_2}?limit={limit}&ignore_invalid=1")

    with open("depth.txt", "w") as file:
        file.write(response.text)

    bids = response.json()[f"{coin_1}_usdt"]["bids"]
    
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_ammount = item[1]

        total_bids_amount += price * coin_ammount

    return f"Total bids for {coin_1}: {total_bids_amount}"
    # return response.text

def get_trades(coin_1="eth", coin_2="usdt", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin_1}_{coin_2}?limit={limit}&ignore_invalid=1")

    with open("trades.txt", "w") as file:
        file.write(response.text)

    total_trade_ask = 0
    total_trade_bit = 0

    for item in response.json()[f"{coin_1}_{coin_2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bit += item["price"] * item["amount"]

    info = f"[-] TOTAl {coin_1} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin_1} BUY: {round(total_trade_bit, 2)} $"


    return info


def main():
    # get_info()
    # get_ticker()
    # print(get_depth())
    # print(get_depth('xrp'))
    # print(get_depth('ltc', limit=2000))
    print(get_trades(limit = 2000))

if __name__=="__main__":
    main()