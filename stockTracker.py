import yfinance as yf
import json # Javascript Object Notation
from pathlib import Path


investment_file = Path("investments.json")

#The stock variable is an object
def fetch_stock_price(symbol) :
    stock = yf.Ticker(symbol)
    print(stock)
    hist = stock.history(period="3d")
    return hist["Open"][-1]
fetch_stock_price("tsla")

def calculate_shares(investment,price) :
    return investment/price 

def get_curent_value(shares,current_price) :
    return shares*current_price

def get_profit_or_loss (inital_value,current_value) :
    return current_value-inital_value

def load_investments () :
    if investment_file.exists() :
        with investment_file.open("r") as file :
            return json.load(file)
    return [] 




def save_investment (investment) :
    investments = load_investments()
    investments.append(investment)
    with investment_file.open("w") as file :
        return json.dump(investments,file)
        








def display_investments() :
    investments = load_investments()
    for investment in investments   :
        symbol = investment["symbol"]
        amount_invested =
























