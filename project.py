"""
Author : Shivang  Bagri
Date : 27/10/20
Purpose: Departmental Store Management System

"""
import mysql.connector
from datetime import datetime
import random

mydb = mysql.connector.connect(user='shivangbagri', password='hivang26', database='wisdom',
                               auth_plugin="mysql_native_password", autocommit=True)

cur = mydb.cursor()


def show_category(category):
    """
    Function to show product of desired
    category only
    """
    cmd = "select * from shop where category='" + category + "'"
    cur.execute(cmd)
    result = cur.fetchall()
    if not result:
        print('No such category. Try again. ')
    else:
        print("|Product_ID|", '|Name|', '|Price (Rs)|', '|Available QTY|', '|Discount|', '|Category|')
        for i in result:
            print(i)


def generate_bill(name, ac_no, product, price, qty, discount):
    """
    Function generates bill using given parameters
    """
    print('===============================================')
    print(f'                                  No: {random.randint(111, 999)} ')
    print('               GREAT INDIAN MALL               ')
    print(' 69 ,Marconi Street, WarrenBridge-6969, INDIA  ')
    print()
    print('-----------------------------------------------')
    print(f'Name: {name}                                  ')
    print(f'A/c number: {ac_no[:5]}****                   ')
    print(f'Time: {datetime.now()}                        ')
    print('-----------------------------------------------')
    print('Product                      Qty.       Price  ')
    print(f'{product}                   {qty}      {price}')
    print()
    print('---------------------------------------------- ')
    print(f'Discount = {discount}                         ')
    if discount != '-':
        print(f'Total                {price - int(discount[:2])}')
    else:
        print(f'Total                              {price}')

    print('-----------------------------------------------')

    print('Dealer signature:___________________________   ')
    print('===============================================')


def buy(prod_id, quantity):
    """
    Function handles buying of specific
    product by id
    """
    cmd = "select* from shop where Pid='" + str(prod_id) + "'"
    cur.execute(cmd)
    pot = cur.fetchone()
    if pot is not None:
        cmd = "select* from shop where Pid='" + str(prod_id) + "'"
        cur.execute(cmd)
        result = cur.fetchall()
        print('Here is your product -')
        print("|Product_ID|", '|Name|', '|Price (Rs)|', '|Available QTY|', '|Discount|', '|Category|')
        for i in result:
            print(i)
        if quantity > result[0][3]:
            print('Not enough quantities available. ')
            return
        else:
            price = result[0][2] * quantity
            discount = result[0][4]
            confirm = input(f'Are you sure you want to buy {result[0][1]}  (y/n) ')
            if confirm == 'y':
                cur.execute("update shop set available_units=available_units-'" + str(quantity) + "' where pid='" + str(
                    prod_id) + "'")
                name = input('Enter your Name ')
                num = input('Enter Card Number ')
                pay = int(input('Enter amount to pay '))

                if pay < price:
                    print('Not enough amount! Try again')
                else:
                    print(f'{abs(price - pay)} rs Change returned with {discount} rs discount. Payment '
                          f'Successful! ')
                    print('Your bill generated successfully!\n ')
                    generate_bill(name, num, result[0][1], price, quantity, discount)

    else:
        print('No such product ID. Try again.')


def login(user, password):
    """
    Function handles login of authenticated users
    only in admin panel
    """
    valid_user = 'hivang26'
    valid_pwd = 26262
    while user != valid_user:
        return False
    if user == valid_user and password == valid_pwd:
        return True


def update_info(p_id, new, choice):
    """
    Function to update product specifications
    """
    if choice == 1:
        cmd = "update shop set price='" + str(new) + "' where Pid='" + str(p_id) + "'"
        cur.execute(cmd)
    elif choice == 2:
        cmd = "update shop set available_units=available_units+'" + str(new) + "' where Pid='" + str(p_id) + "'"
        cur.execute(cmd)
    print('Update successful. New Results: ')
    print("|Product_ID|", '|Name|', '|Price (Rs)|', '|Available QTY|', '|Discount|', '|Category|')
    cmd = "select * from shop where Pid='" + str(p_id) + "'"
    cur.execute(cmd)
    result = cur.fetchall()
    for i in result:
        print(i)


def add_product(p_id, p_name, price, qty, discount, category):
    """
    Function to add new product to database
    """
    cmd = "insert into shop values('" + str(p_id) + "','" + str(p_name) + "','" + str(price) + "','" + str(
        qty) + "','" + str(discount) + "','" + str(category) + "')"
    cur.execute(cmd)
    print(f'{p_name} added successfully. ')


if __name__ == '__main__':
    while True:
        print('What do you want to do? ')
        try:
            choice = int(
                input(
                    '1: Show available products\n2: Choose Category\n3: Ongoing Discounts\n4: Buy Now\n5: Admin '
                    'Panel\n6: Exit\n'
                ))
        except ValueError:
            choice = 6
        if choice == 1:   # Available products
            cmd = 'select * from  shop;'
            cur.execute(cmd)
            result = cur.fetchall()
            print("|Product_ID|", '|Name|', '|Price (Rs)|', '|Available QTY|', '|Discount|', '|Category|')
            for i in result:
                print(i)
        elif choice == 2:  # Choose Category
            print('Available Categories:\n>Food \n>Daily Use\n>Home ')
            cate = input('Choose category ')
            show_category(cate)

        elif choice == 3:  # Discounts
            cmd = '''select * from shop where discount!='-' '''
            cur.execute(cmd)
            result = cur.fetchall()
            print("|Product_ID|", '|Name|', '|Price (Rs)|', '|Available QTY|', '|Discount|', '|Category|')
            for i in result:
                print(i)
        elif choice == 4:  # Buy
            try:
                product_ID = int(input('Enter Product ID '))
                qty = int(input('Enter quantity '))
                buy(prod_id=product_ID, quantity=qty)
            except ValueError:
                print('Invalid entry. Try again.')

        elif choice == 5:  # Admin controls
            username = input('Enter username ')
            try:
                pwd = int(input('Enter 5 digit password '))
            except ValueError:
                pwd = None
            if login(username, pwd):
                print('Logged in successfully. ')
                while True:
                    print('What do you want to do? ')
                    try:
                        admin_choice = int(input(
                            '1: Update Product Prices\n2: Update Product Quantity\n3: Add '
                            'new Products\n4: Log out\n'
                        ))
                    except ValueError:
                        print('Invalid Entry. ')
                        admin_choice = None
                    if admin_choice == 1:
                        p_id = int(input('Enter Product ID '))
                        new_price = int(input('Enter new price '))
                        update_info(p_id, new_price, admin_choice)
                    elif admin_choice == 2:
                        p_id = int(input('Enter Product ID '))
                        new_qty = int(input('Enter quantity to be added '))
                        update_info(p_id, new_qty, admin_choice)
                    elif admin_choice == 3:
                        p_id = int(input('Enter Product ID '))
                        name = input('Enter Product name ')
                        price = int(input('Enter Product price '))
                        qty = int(input('Enter Product quantity '))
                        disc = input('Enter Products discount (if any else -) ')
                        cat = input('Enter Product Category ')
                        add_product(p_id, name, price, qty, disc, cat)
                    elif admin_choice == 4:
                        print('Logged out successfully. ')
                        break
            else:
                print('Incorrect Username or password. Please try again later. ')
        elif choice == 6: # Exit
            print('Thanks for visiting GREAT INDIAN MALL :) ')
            break
        else:
            print('Invalid entry ')
