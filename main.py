MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 70,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24
        },
        "cost" : 200,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 120,
    },
}

resources = {
    "water" : 400,
    "milk" : 400,
    "coffee" : 100,
}

profit = 0
coffe_machine_running = True

def sufficient_ingredients(drink):
    for item in drink["ingredients"]:
        if drink['ingredients'][item] > resources[item]:
            print("Sorry there aren't sufficient ingredients left")
            return False
    return True

def process_coins():
    total = int(input("Enter number of 10 rupee notes: ")) * 10
    total += int(input("Enter number of 20 rupee notes: ")) * 20
    total += int(input("Enter number of 50 rupee notes: ")) * 50
    total += int(input("Enter number of 100 rupee notes: ")) * 100
    total += int(input("Enter number of 200 rupee notes: ")) * 200
    total += int(input("Enter number of 500 rupee notes: ")) * 500
    return total

def sufficient_funds(choice, amount):
    if amount >= choice["cost"]:
        global profit
        profit += choice["cost"]
        if amount > choice["cost"]:
            print(f"“Here is Rs.{amount - choice["cost"]} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(choice, drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {choice}. Enjoy ☕")

while coffe_machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        coffe_machine_running = False
    elif choice == "report":
        for item in resources:
            print(f"Remaining {item} available is {resources[item]}")
        print(f"Profit is Rs. {profit}")
    else:
        if choice not in MENU:
            print("Choose a valid coffee")
        else:
            drink = MENU[choice]
            if sufficient_ingredients(drink):
                print(f"Your drink costs {drink["cost"]}")
                total_cost = process_coins()
                if sufficient_funds(drink, total_cost):
                    make_coffee(choice, drink)
