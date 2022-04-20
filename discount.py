import price
class Discount:
    def __init__(self, discount, type, validity, discountedamount):
        self.discount = discount
        self.type = type
        self.validity = validity
        self.discountedamount = discountedamount

discountedprice = .get_price()

"""import from user menu"""
user = Discount(True, "%","valid",5)

if user.discount == True
    if user.type == "%"
        discountedprice = discountedprice*(1 - user.discountedamount)
elif user.type =="flat"
        discountedprice = discountedprice - user.discountedamount
elif
    discountedprice = price


