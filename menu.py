"""
title: python project - KMX Shipping Platform

authors:        Thomas Konigkramer

contributors:   

"""


import pandas as pd
import getpass
import os


'''
1 -- database functions
'''

## directories/locations
working_dir = os.getcwd() + '\mmef_python-project'
db_dir = working_dir + '\database'
customers_dir = db_dir + '\db_customers.csv'
orders_dir = db_dir + '\db_orders.csv'
# giftcards_dir = db_dir + '\db_giftcards.csv'
# promocodes_dir = db_dir + '\db_promocodes.csv'

## creating dataframes
df_customers = pd.read_csv(customers_dir)
df_packages = pd.read_csv(orders_dir)
# df_giftcards = pd.read_csv(giftcards_dir) 
# df_promocodes = pd.read_csv(promocodes_dir)

def retrieve_list_from_db(database, item):
    '''
    function that retrieves lists of column values in csv database 
    parameters: database - dataframe of csv file. Of form df_name
                item - column name we want in list
    '''
    retrieved_list = database[item].to_list()
    return retrieved_list


'''
2 -- printing/formating functions
'''

def print_bars():
    '''
    printing functions used to enhance display
    '''
    print('----------------------------------------------------------------------------------------')


def print_welcome_menu():
    '''
    printing function - welcome menu
    '''
    print_bars()
    print('Welcome to the KMX Shipping Platform.')
    print('This is the login menu.')
    print('1 -- Sign-in : existing customer')
    print('2 -- Sign-up : new customer')
    print('3 -- Exit')
    print_bars()


def print_customer_menu():
    '''
    printing function - customer menu
    '''
    print_bars()
    print('This is the customer menu.')
    print('1 -- Place a new order')
    print('2 -- View orders in progress')
    print('3 -- View order history')
    print('4 -- View my gift card balance')
    print('5 -- View promo codes used')
    print('6 -- Return to previous menu')
    print_bars()


'''
3 -- menu functions
'''

def signin():
    '''
    function used for user sign-in
    '''
    print_bars()
    print('Signing back in:')

    usernames = retrieve_list_from_db(df_customers, 'Username')
    user_verification = info_prompt_check('Username', usernames, False, 'Welcome')
    if not usernames:
        print('yeah')
    if user_verification is True:
        passwords = retrieve_list_from_db(df_customers, 'Password')
        password_verification = verify_hidden_info('Password', passwords)
    else:
        back_menu('welcome')

def signup():
    '''
    fucntion used for user sign-up
    '''
    print_bars()
    print('Signing up for the first time:')

    name = info_prompt_check('First name')
    surname = info_prompt_check('Surname')
    usernames = retrieve_list_from_db(df_customers, 'Username')
    username = info_prompt_check('Username', usernames)
    password = hidden_prompt('password')
    # initialise and then check: confirm = ask whether happy with everything




# def verify_hidden_info()

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
            print_bars()
            print(f'Welcome back, {user} !')
            action_menu()
            # something here?
        elif count == 2:
            print_bars()
            print('You have entered an invalid password 3 times.')
            welcome_menu()
        else:
            print_bars()
            print('You have entered an incorrect password - please try again.')
            count += 1



# request: str with first letter capital, requests: str for check, check: boolean for if check needed
def info_prompt_check(request, requests = [], new = True, last_menu = ''):
    '''
    function to receive new information, check against database, and return to previous menu
    parameters: request - information requested from user
                requests - database list to check information against
                new - defaults to F. Used to determine whether requested info is expected to be in db or not
                    - F used if we expect data to be in db, e.g. when signing in and checking user exists
                    - T used if we don't expect data to be in db, e.g. confirming that a new username does not already exist in db
                last_menu - return to last menu if incorrect information provided 3 times
    '''
    count = 0
    while True:
        print_bars()
        try:
            prompt = input(f'{request}: ')
        except:
            pass
        # check if list is not empty
        if requests:
            if new is True:
                if prompt in requests:
                    print_bars()
                    print(f'{request} already exists - please choose a different one.')
                    
                else:
                    return prompt
            else:
                if prompt in requests:
                    print_bars()
                    print(f'{request} provided is invalid - please try again.')
        if last_menu is True:
            if count == 2:
                print_bars()
                print(f'{request} provided invalid. 3 attempts failed.')
                back_menu(last_menu)
        else:
            return prompt

# request: lower case str
def hidden_prompt(request):
    while True:
        print_bars()
        try:
            prompt = getpass.getpass()
            print_bars()
            check = getpass.getpass(f'Please confirm your {request}: ')
        except:
            pass
        if prompt != check:
            print_bars()
            print("Your entries don't match - please try again.")
        else:
            return prompt



# needs back menu added
def option_menu(menu):
    no_options = len(menu) - 1
    while True:
        # printing function called
        menu.get(0)()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print_bars()
            print('Input incorrect - please enter a number.')
        if option == 1:
            # list under menu_dic item 1
            for action in menu.get(1):
                if type(action) == str:
                    print(action)
                else:
                    action()
        # loop over 2->n items in menu_dic
        for i in range(2, no_options):
            if option == i:
                # since values are lists of actions
                actions = menu.get(i)
                for action in actions:
                    if type(action) == str:
                        print(action)
                    else:
                        action()
        else:
            print_bars()
            print(f'Invalid option. Please enter a number between 1 and {no_options}.')


def back_menu(menu):
    if menu == 'welcome':
        option_menu(welcome_menu_dic)

### dictionaries used for menues ###
''''
description of menu dictionaries
0 : printing function name
1 - n : list of actions to perform, either parameterless functions or strings to print
'''

welcome_menu_dic = {
    0 : print_welcome_menu,
    1 : [signin],
    2 : [signup],
    3 : [print_bars, 
    'Thank you for visiting the KMX Shipping Platfrom. Enjoy your day.',
    print_bars,
    exit]
}

customer_menu_dic = {
    0 : print_customer_menu,
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [print_bars,
    'Returning to welcome menu',
    back_menu]

}

option_menu(welcome_menu_dic)

