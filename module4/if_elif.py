"""
Program: if_elif.py
Author: Rachael Wolf
Last date modified: 09/21/2020

The purpose of this program is to ask for the user to sign up for
Programmer's Toolkit Monthly Subscription Box.
They must select level of membership they want.
"""


def main():
    print('Welcome to Programmer\'s Toolkit Monthly Subscription Box!')
    print('Membership levels available: \nPlatinum, Gold, Silver, Bronze, Free Trial')
    level = input('Which membership level are you purchasing? ')
    lev_name = 'Free Trial'
    price = 0
    if level in ['Platinum', 'platinum', 'P', 'p']:
        lev_name = 'Platinum'
        price = 60
    elif level in ['Gold', 'gold', 'G', 'g']:
        lev_name = 'Gold'
        price = 50
    elif level in ['Silver', 'silver', 'S', 's']:
        lev_name = 'Silver'
        price = 40
    elif level in ['Bronze', 'bronze', 'B', 'b']:
        lev_name = 'Bronze'
        price = 40
    print('The price for ' + lev_name + ' membership is $' + str(price))


if __name__ == '__main__':
    main()
