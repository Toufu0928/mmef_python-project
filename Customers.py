class Customers:
    '''
    A class to handle a customer's attributes
    '''

    def __init__(self, firstname, surname, username, user_id, password):
        self.firstname = firstname
        self.surname = surname
        self.username = username
        self.password = password
        self.user_id = user_id

    def __str__(self):
        bars = '----------------------------------------------------------------------------------------\n'
        summary_message = bars + f'User details:\n' + bars + f'User ID     : {self.user_id}\nUsername    : {self.username}\nFirst name  : {self.firstname}\nSurname     : {self.surname}'
        return summary_message

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname
    
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_user_id(self):
        return self.user_id

def print_bars():
    '''
    printing functions used to enhance display
    '''
    print('----------------------------------------------------------------------------------------')

    



'''create an instance'''


        