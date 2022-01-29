from menu import MENU, resources

quarters = 0.50
dimes = 0.10
nickles = 0.05
pennies = 0.01
turn_off = True


def resource_check(user_choice):
    """Takes user_choice Input and checks if resources are enough"""
    # check if enough resources are in the machine
    if resources["water"] > MENU[user_choice]["ingredients"]["water"] and \
            resources["milk"] > MENU[user_choice]["ingredients"]["milk"] and \
            resources["coffee"] > MENU[user_choice]["ingredients"]["coffee"]:
        return True
    elif resources["water"] < MENU[user_choice]["ingredients"]["water"]:
        print("There is not enough water")
        return False
    elif resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
        print("There is not enough milk")
        return False
    elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
        print("There is not enough coffee")
        return False


def operation(user_choice):
    """"Checks payment and manage resources"""
    print("Please insert coins.")
    user_quarters = float(input("How many quarters?: "))
    user_dimes = float(input("How many dimes?: "))
    user_nickles = float(input("How many nickles?: "))
    user_pennies = float(input("How many pennies?: "))
    # add user_coins together
    user_coins_total = (
                (user_quarters * quarters) + (user_dimes * dimes) + (user_nickles * nickles) + (user_pennies * pennies))
    # get cost for user drink
    user_drink_cost = MENU[user_choice]["cost"]
    # check if user_coins_total is enough for drink, calculate change and add it to the resources dict
    if user_coins_total > user_drink_cost:
        user_coins_change = user_coins_total - user_drink_cost
        resources.update({"water": (resources["water"] - MENU[user_choice]["ingredients"]["water"])})
        resources.update({"milk": (resources["milk"] - MENU[user_choice]["ingredients"]["milk"])})
        resources.update({"coffee": (resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"])})
        resources.update({"money": (resources["money"] + user_drink_cost)})
        print(f"Here is ${user_coins_change} in change.")
        print("Have fun with your drink!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return


while turn_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_choice == "off":
        break
    elif user_choice == "report":
        print(resources)
    elif user_choice == "espresso" or "latte" or "cappuccino":
        if resource_check(user_choice) is False:
            continue
        else:
            operation(user_choice)
