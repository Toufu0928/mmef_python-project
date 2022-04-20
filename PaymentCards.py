"""
title: python project - KMX Shipping Platform, PaymentCards class

authors:        Thomas Konigkramer  

PaymentCards class
"""

'''importing parent classes'''
import Customers

class PaymentCards(Customers.Customers):
    '''
    A class to handle gift cards/payment cards
    '''

    def __init__(self, firstname, surname, username, user_id, password, card_number, expiry_date, card_balance):
        super().__init__(firstname, surname, username, user_id, password)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.card_balance = card_balance

    def get_cardholder(self):
        cardholder_name = self.firstname + ' ' + self.surname
        return cardholder_name

    def withdraw(self, amount):
        # Cannot withdraw: amount is greater than balance
        if self.card_balance < amount:
            return 0
        else:
            self.card_balance -= amount
            return self.card_balance

    def is_expired(self, today):
        # Card is expired and credited amounts are lost.
        if self.expiry_date > today:
            return 1
        # f'Card expiry not reached. Balance of {self.card_balance} remaining and valid until {self.expiry_date}.
        else:
            return 0

    

card1 = PaymentCards('Alex', 'Tester', 'tester', '000000003', 'test', '111111111111', '01/01/2022', 500)
print(card1.get_cardholder())

        

    