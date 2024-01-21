
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# TODO : 1. Print Report


def print_report():
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}g")
    print(f"Money : ${resources["money"]}")


# TODO : 2. Check resources sufficient?


def resources_check(choice):
    if choice == "espresso":
        if resources["water"] >= 50:
            if resources["coffee"] >= 18:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    if choice == "latte":
        if resources["water"] >= 200:
            if resources["coffee"] >= 24:
                if resources["milk"] >= 150:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    if choice == "cappuccino":
        if resources["water"] >= 250:
            if resources["coffee"] >= 24:
                if resources["milk"] >= 100:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False


# TODO : 3. Process coins

def coin_process(choice):
    print("Please insert coins")
    quarters = float(input("How many quarters? : "))
    dimes = float(input("How many dimes? : "))
    nickles = float(input("How many nickles? : "))
    pennies = float(input("How many pennies? : "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
# TODO : 4. Check Transaction successful?
# TODO : 5. Make Coffee
    if choice == "espresso":
        if total == 1.5:
            resources["water"] -= 50
            resources["coffee"] -= 18
            resources["money"] += 1.5
            print("Here is your espresso, Enjoy!!")
        elif total > 1.5:
            resources["water"] -= 50
            resources["coffee"] -= 18
            resources["money"] += 1.5
            change = total - 1.5
            print(f"Here is ${round(change, 2)} in change.")
            print("Here is your espresso, Enjoy!!")
        elif total < 1.5:
            print("Sorry that's not enough money. Money refunded")

    if choice == "latte":
        if total == 2.5:
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
            resources["money"] += 2.5
            print("Here is your latte, Enjoy!!")
        elif total > 2.5:
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
            resources["money"] += 2.5
            change = total - 2.5
            print(f"Here is ${round(change, 2)} in change.")
            print("Here is your latte, Enjoy!!")
        elif total < 2.5:
            print("Sorry that's not enough money. Money refunded")

    if choice == "cappuccino":
        if total == 3.00:
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            resources["money"] += 3.00
            print("Here is your cappuccino, Enjoy!!")
        elif total > 3.00:
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
            resources["money"] += 3.00
            change = total - 3.00
            print(f"Here is ${round(change, 2)} in change.")
            print("Here is your cappuccino, Enjoy!!")
        elif total < 3.00:
            print("Sorry that's not enough money. Money refunded")


start = True
while start:
    user_input = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if user_input == "report":
        print_report()
    if user_input == "off":
        start = False
    if resources_check(user_input):
        coin_process(user_input)
