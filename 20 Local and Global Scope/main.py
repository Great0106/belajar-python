items = [('diapers', 10.00), ('peanuts', 5.00), ('butter', 6.25), ('cheese', 3.00), ('milk', 3.5), ('yoghurt', 1.99), ('eggs', 4.5), ('bread', 4), ('shrimp', 2.5), ('coffee', 1.5)]

money = 50
cartlist = []
menu = "" #buy, return, quit

def buyProduct (product,price):
    global money
    money = money - price
    cartlist.insert(0,product)
    print(f"Your money left = {money}")
    print(f"Your shopping cart = {cartlist}")

def returnProduct(product,price):
    global money
    money = money + price
    cartlist.remove(product)
    print(f"Your money left = {money}")
    print(f"Your shopping cart = {cartlist}")


while menu != quit:
    print("""

        Diapers ....10.00
        Peanuts ....5.00
        Butter .....6.25
        Cheese .....3.00
        Milk .......3.50
        Yogurt .....1.99
        Eggs .......4.50
        Bread ......4.00
        Shrimp .....2.50
        Coffee .....1.50

        """)
    menu = input("Do you want to buy, return, or quit? ").lower()

    if menu == 'buy':
        ask = input("What item would you like to buy? ").lower()
        for item in items:
            if ask == item[0]:
                print(f"{ask} is $ {item[1]}")
                confirm = input("Do you want to proceed? Answer with 'Y' to proceed or 'N' to cancel. ").lower()
                if confirm == 'Y':
                    buyProduct(item,item[1])
                else:
                    pass
            else:
                pass

    elif menu == 'return':
        returnask = input("What would you like to return to the shop? ").lower()
        for item in items:
            if returnask == item[0]:
                print(f"{returnask} is $ {item[1]}")
                confirm = input("Do you want to proceed? Answer with 'Y' to proceed or 'N' to cancel. ")
                if confirm == 'y':
                    returnProduct(item,item[1])
                else:
                    pass
            else:
                pass

    elif menu == 'quit':
        print("Thank you for using our products! See you again!")

    else:
        print("Invalid input.")