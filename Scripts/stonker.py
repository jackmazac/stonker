#import matplotlib as ply
#import yfinance
#import pygame
#import numpy as np
from current_stocks import get_stock_price
import csv
import pandas as pd

print("Welcome to STONKERS!")

def account():
    print("LOGIN")
    user_name = input("Please enter a user name: ")
    with open('users.csv', 'r') as check_user:
        reader = csv.DictReader(check_user, delimiter=",")
        for row in reader:
            if row["USERNAME"] == user_name:
                print("User already exists.")
                password = input("Please enter password for " + user_name + ": ")
                if row["USERNAME"] == user_name and row["PASSWORD"] == password:
                    game(user_name)
                else:
                    print("Incorrect password")
                    account()
    print("Welcome to the game!")
    new_user_pass = input("Enter a new password for " + user_name + ": ")
    user_list = [user_name, new_user_pass, 1000]
    with open('users.csv', 'a') as add_user:
        writer = csv.writer(add_user)
        writer.writerow(user_list)
    account()



def game(user_name):
    print("You entered the game " + user_name + "!")
    play = input("Do you want to Buy or Sell or Exit: " )
    if play == "buy" or play == "Buy":
        buy(user_name)
    elif play == "sell" or play == "Sell":
        sell(user_name)
    else:
        quit()
    quit()


def buy(user_name):
    user_money = check_money(user_name)
    print("You currently have $" + user_money + " USD.")
    buy_stock = input("Would you like to BUY? (Y/N): ")
    user_ticker = input("What stock would you like to buy (Enter stock ticker): ")
    current_price = get_stock_price(user_ticker)
    can_buy = float(check_money(user_name)) // current_price
    if buy_stock == "y" or buy_stock == "Y":
        print("You can buy " + str(can_buy) + user_ticker + " stocks.")
        want_buy = input("How much " + user_ticker + " do you want to buy: ")
        confirm = input("Confirm? (Y/N): ")
        if confirm == 'y' or confirm == 'Y':
            print("ADD STOCK NOW")
            #dd_stock(user_name, user_ticker, user_money, want_buy, current_price)
        else:
            game()
    else:
        game()

def sell(user_name):
    print("SELL")


# def add_stock(user_name, user_ticker, user_money, want_buy, current_price):
#     stocks = pd.read_csv("user_stocks.csv")# NEED TO FIX:
#     if user_ticker in stocks.columns: #checks to see if column for ticker was already created
#         if user_name in stocks[0]: #checks to see if row for user was already created
#             stocks.loc[user_name, user_ticker] = (want_buy + ":" + current_price) #find user and tikcet and update value to how much stock they bought and what the current price is
#         else: #if user was not created
#             --- stocks.at[len(stocks.index), 0] = [user_nme]
#             #add for loop
#             --- stocks.loc[user_name, user_ticker] = (want_buy + ":" + current_price)
#     else: #if column for ticker was not created
#         -- stocks[user_ticker] = [-1] #add column to end with all values of NA




def check_money(user_name):
    with open('users.csv', 'r') as check_money:
        reader = csv.DictReader(check_money, delimiter=",")
        for row in reader:
            if row["USERNAME"] == user_name:
                user_money = row["MONEY"]
    return user_money


account()
