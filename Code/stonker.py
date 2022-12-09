#import matplotlib as ply
#import yfinance
#import pygame
#import numpy as np
from current_stocks import get_stock_price
import csv
import pandas as pd

# back end of the game 
print("Welcome to STONKERS!")

''' This method creates the login screen for the game '''
def account():
    print("LOGIN")
    user_name = input("Please enter a user name: ") # get the username 
    # open the csv file with the users -- databases 
    with open('users.csv', 'r') as check_user:
        reader = csv.DictReader(check_user, delimiter=",")
        for row in reader:
            # if the username exists, log in, else try again 
            if row["USERNAME"] == user_name:
                print("User already exists.")
                password = input("Please enter password for " + user_name + ": ")
                if row["USERNAME"] == user_name and row["PASSWORD"] == password:
                    game(user_name)
                else:
                    print("Incorrect password")
                    account() # ?? why is this recursive? We should use a while loop instead!
    print("Welcome to the game!")
    # enter a new password for the game 
    new_user_pass = input("Enter a new password for " + user_name + ": ")
    user_list = [user_name, new_user_pass, 1000]
    # add the user to the csv file -- database 
    with open('users.csv', 'a') as add_user:
        writer = csv.writer(add_user)
        writer.writerow(user_list)
    account() # there is no base case so this will result in a stack overflow! change this 


'''
This method defines the game 
Parameters: 
- user_name: the username 
'''
def game(user_name):
    # get user input 
    print("You entered the game " + user_name + "!")
    play = input("Do you want to Buy or Sell or Exit: " )
    # if the user selects buy, run buy 
    # elif the user selects sell, run sell 
    # else quit the game 
    if play == "buy" or play == "Buy":
        buy(user_name)
    elif play == "sell" or play == "Sell":
        sell(user_name)
    else:
        quit()
    quit()

'''
This is the buy method for the game 
Parameters: 
- user_name: the user name 
'''
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

'''
This is the sell method for the game 
Parameters: 
- user_name: the user name 
'''
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

'''
This method checks to see the users money 
Parameters: 
- user_name: the user name 
Returns: 
- user_money: the amount of money the user has 
'''
def check_money(user_name):
    with open('users.csv', 'r') as check_money:
        reader = csv.DictReader(check_money, delimiter=",")
        for row in reader:
            if row["USERNAME"] == user_name:
                user_money = row["MONEY"]
    return user_money


account()
