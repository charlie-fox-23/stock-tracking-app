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
        amount_invested = investment["amount_invested"]
        purchase_price = investment["purchase_price"]
        shares_purchased = calculate_shares(amount_invested,purchase_price)
        current_price = fetch_stock_price(symbol)
        current_value = get_curent_value(shares_purchased,current_price)
        profit_or_loss = get_profit_or_loss(amount_invested,current_value)
        
        print(f"Stock symbol:{symbol}")
        print(f"Amount invested:{amount_invested}")
        print(f"Purchase price:{purchase_price}")
        print(f"Current price:{current_price}")
        print(f"Current value:{current_value}")
        print(f"Profit or loss:{profit_or_loss}")
        print("-"*30)
        
action = input("type in 1 to add a investment or type in 2 to view previus investments")
if action =="1" :
    stock_symbol = input("type in a stock symbol").upper()
    investment_amount = float(input("type enter amount you want to invest"))
    purchase_price = float(input("enter the purchase price of the stock"))
    investment = {
        "symbol":stock_symbol,
        "amount_invested":investment_amount,
        "purchase_price":purchase_price
    }
    save_investment(investment)
    print("saved investment")
elif action == "2" :
    print("These are your investments!")














#not needed code

# key_value = {
# 1:"jo mama",
# 2:"jo dada",
# 3:"jo grandma"
# }
# print (key_value[1])
# print("-"*50)
# print(key_value[2])
# print("-"*50)
# print(key_value[3])
# print("-"*50)








