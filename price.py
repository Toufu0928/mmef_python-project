"""
title : python project KMX Shipping Platform, Pricing Model

author: Sukanya Mukherjee

Pricing Model - we use this to present the three shipping method price options and to calculate the pre-tax and discount price.
"""
#import neworderclass

'''will get all these from neworderclass'''

distance_code = 2 #range circles 1 to 5
shipping_method = 1.5 #Priority(1.5) /Express(1) /Standard (0)"
shipping_style = 1 #Air/Train" just display?
shipping_destination = 1 #"Domestic(0)/International(1)"
package_size = 1.5 #Small 0/ Medium 1/ Big 1.5"


baseprice = 8

"""price pre VAT/discounts"""
price = baseprice + 5*shipping_destination + 2.5*package_size + 2.5*distance_code
print(price)

class Price:
    def __init__(self, type):
        self.type = type

    def get_price(self):
         if self.type == "Priority":
             price = price + 5
         elif self.type == "Express":
             price = price + 2.5
         return price

user = user.Price("Priortiy")
finalprice = user.get_price
print(finalprice)