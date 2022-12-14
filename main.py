from menu import MENU, resources
import time

total_money = 0


def order():
    global total_money

    def coins():
        global total_money
        payment_accepted = False
        while not payment_accepted:
            euros = float(input("How many euros do you enter?\n"))
            if choice == "espresso":
                if euros < 1.5:
                    print("I am sorry, you can't afford the coffee.")
                else:
                    payment_accepted = True
                    print("Payment accepted!")
                    total_money += 1.50
                    if euros > 1.51:
                        print("Wait for change...")
                        time.sleep(2)
                        print(f"Your change is {euros - 1.50}.")
                    make_coffee()

            elif choice == "latte":
                if euros < 2.5:
                    print("I am sorry, you can't afford the coffee.")
                else:
                    payment_accepted = True
                    print("Payment accepted!")
                    total_money += 2.50
                    if euros > 2.51:
                        print("Wait for change...")
                        time.sleep(2)
                        print(f"Your change is {euros - 2.50}.")
                    make_coffee()

            elif choice == "cappuccino":
                if euros < 3.0:
                    print("I am sorry, you can't afford the coffee.")
                else:
                    payment_accepted = True
                    print("Payment accepted!")
                    total_money += 3.00
                    if euros > 3.01:
                        print("Wait for change...")
                        time.sleep(2)
                        print(f"Your change is {euros - 3.00}.")
                    make_coffee()

    def check():
        if water_needed < resources["water"]:
            if coffee_needed < resources["coffee"]:
                if milk_needed < resources["milk"]:
                    coins()
                else:
                    print("The machine run out of milk.")
            else:
                print("The machine run out of coffee.")
        else:
            print("The machine run out of water.")

    def make_coffee():
        if choice == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18
            print("Enjoy your Espresso! ☕")
            order()
        elif choice == "latte":
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
            print("Enjoy your Latte! ☕")
            order()
        elif choice == "cappuccino":
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            print("Enjoy your Cappuccino! ☕")
            order()

    water_needed = 0
    coffee_needed = 0
    milk_needed = 0

    choice = input("Would you like 'Espresso', 'Latte' or 'Cappuccino'?\n").lower()
    if choice == "off":
        return
    elif choice == "report":
        for items in resources:
            print(f"{items.title()}: {resources[items]}")
        print(f"Total money: {total_money}")
        order()
    elif choice == "espresso":
        water_needed += MENU["espresso"]["ingredients"]["water"]
        coffee_needed += MENU["espresso"]["ingredients"]["coffee"]
        ingredients_needed = [water_needed, coffee_needed, milk_needed]
        check()
    elif choice == "latte":
        water_needed += MENU["latte"]["ingredients"]["water"]
        coffee_needed += MENU["latte"]["ingredients"]["coffee"]
        milk_needed += MENU["latte"]["ingredients"]["milk"]
        ingredients_needed = [water_needed, coffee_needed, milk_needed]
        check()
    elif choice == "cappuccino":
        water_needed += MENU["cappuccino"]["ingredients"]["water"]
        coffee_needed += MENU["cappuccino"]["ingredients"]["coffee"]
        milk_needed += MENU["cappuccino"]["ingredients"]["milk"]
        ingredients_needed = [water_needed, coffee_needed, milk_needed]
        check()


order()
