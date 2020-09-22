"""
Program: coupon_calculations.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to accept the amount of the purchase,
the cash coupon, and the percent coupon.  From these it will
calculate and return the total payment for the order item.
"""


def calculate_order(price, cash_coupon, percent_coupon):
    payment = 0
    tax = price * .06
    shipping = 0
    if price < 10:
        payment += price
        shipping = 5.95
        if cash_coupon == 5:
            payment -= 5
        elif cash_coupon == 10:
            payment -= 10
        payment -= payment * (percent_coupon/100)
    return max(payment, 0) + tax + shipping


def main():
    print('thing 1')
    print('thing 2')
    level = input('doo doo dooo')
    if level:
        print('beep')
    print('stuff')


if __name__ == '__main__':
    main()
