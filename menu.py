"""
title: python project - KMX Shipping Platform

contributors/authors:   Thomas Konigkramer

"""


import pandas as pd
import getpass
import os

working_dir = os.getcwd() + '\mmef_python-project'
db_dir = working_dir + '\database'
customers_dir = db_dir + '\db_customers.csv'
packages_dir = db_dir + '\db_packages.csv'
# giftcards_dir = db_dir + '\db_giftcards.csv'
# promocodes_dir = db_dir + '\db_promocodes.csv'

df_customers = pd.read_csv(customers_dir)
df_packages = pd.read_csv(packages_dir)
# df_giftcards = pd.read_csv(giftcards_dir) 
# df_promocodes = pd.read_csv(promocodes_dir)

list_of_customers = df_customers['Username'].to_list()

# print(df_customers.to_string())

def print_bars():
    print('----------------------------------------------------------------------------------------')


def print_welcome_menu():
    print_bars()
    print('Welcome to the KMX Shipping Platform.')
    print('This is the login menu.')
    print('1 -- Sign-in : existing customer')
    print('2 -- sign-up : new customer')
    print('3 -- Exit')
    print_bars()

def print_action_menu(user):
    print_bars()
    print(f'Hi, {user} - welcome back!')
    print(f'This is the action menu.')
    print('1 -- Place a new order')
    print('2 -- View orders in progress')
    print('3 -- View order history')
    print('4 -- View my gift card balance')
    print('5 -- View promo codes used')
    print('6 -- Return to previous menu')
    print_bars()

def username_prompt():
    count = 0
    while(True):
        print_bars()
        try: 
            username = input('Username: ') 
        except:
            print('This user does not exist. Please try again.')
        if username in list_of_customers:
            # encoding? - replace with Customer Class
            password = df_customers[df_customers['Username']==username]['Password'][0]
            # print(str(password))
            # rather return custoemer instance
            password_prompt(username, password)
        elif count == 2:
            print_bars()
            print('You have entered an invalid username 3 times.')
            welcome_menu()
        else:
            print_bars()
            print('You have entered an invalid username - please try again.')
            count += 1

def password_prompt(user, password):
    count = 0
    while True:
        print_bars()
        try:
            p = getpass.getpass()
        except:
            print_bars()
            print('The password you entered is incorrect. Please try again.')
        if p == password:
            print(f'Welcome back, {user} !')
            action_menu(user)
        elif count == 2:
            print_bars()
            print('You have entered an invalid username 3 times.')
            welcome_menu()
        else:
            print_bars()
            print('You have entered an incorrect password - please try again.')
            count += 1

def signin():
    print_bars()
    print('Signing back in:')
    username_prompt()
    #use customer instance and call password

def signup():
    print_bars()
    print('Signing up for the first time:')
    # name
    # surname 
    # username
    # password 
    # prompt to see password

def action_menu(user):
    while(True):
        print_action_menu(user)
        try:
            option = int(input('Enter your choice: '))
        except:
            print_bars()
            print('Wrong input. Please enter a number ...')
        if option == 1:
            new_order()
        elif option == 2:
            orders_in_progress()
        elif option == 3:
            order_history()
        elif option == 4:
            gift_cards()
        elif option == 5:
            promo_codes()
        elif option == 6:
            print_bars()
            print('Returning to welcome menu.')
            welcome_menu()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')

def welcome_menu():
    while(True):
        print_welcome_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print_bars()
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            signin()
        elif option == 2:
            signup()
        elif option == 3:
            print_bars()
            print('Thank you for visiting the KMX Shipping Platform. Enjoy your day.')
            print_bars()
            exit()
        else:
            print_bars()
            print('Invalid option. Please enter a number between 1 and 3.')


if __name__ == '__main__':
    welcome_menu()
    # print('hi')