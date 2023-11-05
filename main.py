MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

# TODO: 1.Prompt user by asking "What would you like? (Espresso/Latte/Cappuccino)"
machine_off = False
profit = 0
while not machine_off:
    action_completed = False
    user_input = input("What would you like? (Espresso/Latte/Cappuccino) ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        machine_off = True

    # TODO: 3. Print report.
    elif user_input == "report":
        print(f"Water: {resources['water']}mL\nMilk: {resources['milk']}mL\nCoffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    # TODO: 4. Check resources sufficient?
    else:
        if MENU[user_input]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there isn't enough water")
            action_completed = True
        if MENU[user_input]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there isn't enough milk")
            action_completed = True
        if MENU[user_input]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there isn't enough coffee")
            action_completed = True
        if action_completed:
            continue

        # TODO 5. Process coins.
        print("Please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))
        total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
        if total < MENU[user_input]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            change = round(total - MENU[user_input]["cost"], 2)
            print(f"Here is ${change} in change.")
            resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
            resources["water"] -= MENU[user_input]["ingredients"]["water"]
            print(f"Here is your {user_input} ☕️. Enjoy!")
            profit += MENU[user_input]["cost"]
