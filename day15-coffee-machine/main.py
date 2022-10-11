from logo import logo

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

PROFIT = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def print_report():
    """ Prints report of all remaining available resources. """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${PROFIT:.2f}")


def process_coins():
    """ Returns `total` calculated from coins inserted """
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_sufficient_payment(payment, drink_cost):
    """ Returns `True` if payment is greater than cost, `False` otherwise. """
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def is_resource_sufficient(order_ingredients):
    """ Returns `True` if enough resources are available to make the order,
    `False` otherwise. """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def prepare_drink(drink_name, order_ingredients):
    """ Deducts ingredients from resources pool and prints out prepared
    drink """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ Enjoy!")


def main():
    """ Starts coffee machine. Program will exit if user inputs `'off'` command."""
    is_on = True
    print(logo)
    while is_on:
        answer = input("What would you like? (espresso/latte/cappuccino): ")
        if answer == "off":
            is_on = False
            print("Shutdown sequence started. Bye.")
        elif answer == "report":
            print_report()
        elif answer in ["espresso", "latte", "cappuccino"]:
            drink = MENU[answer]
            print(f"{answer.capitalize()} costs ${drink['cost']:.2f}.")
            payment = process_coins()
            print(f"Total = ${payment}")
            if is_sufficient_payment(payment, drink["cost"]):
                change = round(payment - drink["cost"], 2)
                print(f"Here is your ${change:.2f} change.")
                if is_resource_sufficient(drink["ingredients"]):
                    global PROFIT
                    PROFIT += drink['cost']
                    prepare_drink(answer, drink["ingredients"])

        else:
            print("Input Error.")


if __name__ == "__main__":
    main()
