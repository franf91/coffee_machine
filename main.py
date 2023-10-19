MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

OFF_PROMPT = "off"
REPORT_PROMPT = "report"
ESPRESSO_PROMPT = "espresso"
LATTE_PROMPT = "latte"
CAPPUCCINO_PROMPT = "cappuccino"

TWO_DOLLAR_COIN = 2
ONE_DOLLAR_COIN = 1
QUARTER_COIN = 0.25
NICKLE_COIN = 0.1
DIME_COIN = 0.05

machine_on = True
machine_money = 0


# function to print report

def report(money):
    """Shows current resources of coffee machine"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffer: {resources['coffee']}")
    print(f"Money: ${money}")


# function to process coins
def coins():
    print("Please insert coins")
    two_dollar = int(input("How many two dollar coins: "))
    one_dollar = int(input("How many one dollar coins: "))
    quarters = int(input("How many quarter coins: "))
    nickles = int(input("How many nickle coins: "))
    dimes = int(input("How many dimes coins: "))

    money = TWO_DOLLAR_COIN * two_dollar + ONE_DOLLAR_COIN * one_dollar + QUARTER_COIN * quarters + NICKLE_COIN * nickles + DIME_COIN * dimes
    return money


# function to verify resources


def verify(drink):
    global machine_money
    resources_water = resources['water']
    resources_milk = resources['milk']
    resources_coffee = resources['coffee']

    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    milk = MENU[drink]["ingredients"]["milk"]

    drink_cost = MENU[drink]["cost"]
    money_input = coins()

    if resources_water < water:
        print("Sorry there is not enough water")
    elif resources_milk < milk:
        print("Sorry there is not enough milk")
    elif resources_coffee < coffee:
        print("Sorry there is not enough coffee")
    elif money_input < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= coffee

        change = money_input - drink_cost
        if money_input > drink_cost:
            print(f"Here is ${change} in change.")
        print(f"Here is your {drink}. Enjoy!")
        machine_money += (money_input - change)


# prompt user by asking “What would you like? (espresso/latte/cappuccino):”


# Turn off the Coffee Machine by entering “off” to the prompt.


while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == OFF_PROMPT:
        machine_on = False
    elif user_input == REPORT_PROMPT:
        report(machine_money)
    elif user_input == ESPRESSO_PROMPT:
        verify(user_input)
    elif user_input == LATTE_PROMPT:
        verify(user_input)
    elif user_input == CAPPUCCINO_PROMPT:
        verify(user_input)
