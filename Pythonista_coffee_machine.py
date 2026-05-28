MENU = {
    "Espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "Latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "Cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}


def report_display():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(round(reserve),2))


def process_coins():
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many Dimes?: "))
    nickles = int(input("How many Nickles?: "))
    pennies = int(input("How many Pennies?: "))
    paid_amount =  0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    return paid_amount


def process_transaction(paid_money, coffee_type, money_pot):
    cost=MENU[coffee_type]["cost"]
    if paid_money < cost:
        print(f"That's not enough money. Money Refunded. Refunded amount: {paid_amount} (Quarters: {quarters}, Dimes: {dimes}, Nickles: {nickles}, Pennies: {pennies})")
        return False, 0
    else:
        refund_amount=paid_money-cost
        money_pot+=cost
        print(f"Here is ${round(refund_amount,2)} in change.")
        return True, money_pot


def check_resources(coffee_type):
    coffee_data=MENU[coffee_type]["ingredients"]
    lack=0
    for ingredient in coffee_data:
        if resources[ingredient] < coffee_data[ingredient]:
            print(f"Sorry, there is no enough {ingredient}")
            lack+=1
    if lack!=0:
        return False
    else:
        return True


def make_coffee(coffee_type):
    coffee_data= MENU[coffee_type]["ingredients"]
    for ingredient in coffee_data:
        resources[ingredient] -= coffee_data[ingredient]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


machine_state = True
reserve = 0

while machine_state:
    user_input=input("What would you like? (Espresso/Latte/Cappuccino): ").title()
    if user_input == "Off":
        machine_state=False
    elif user_input == "Report":
        report_display()
    elif user_input == "Espresso":
        resources_success = check_resources(user_input)
        if resources_success:
            amount=process_coins()
            trans_success_status, reserve = process_transaction(amount, user_input, reserve)
            if trans_success_status:
                make_coffee(user_input)
    elif user_input == "Latte":
        resources_success = check_resources(user_input)
        if resources_success:
            amount = process_coins()
            trans_success_status, reserve = process_transaction(amount, user_input, reserve)
            if trans_success_status:
                make_coffee(user_input)
    elif user_input == "Cappuccino":
        resources_success = check_resources(user_input)
        if resources_success:
            amount = process_coins()
            trans_success_status, reserve = process_transaction(amount, user_input, reserve)
            if trans_success_status:
                make_coffee(user_input)
