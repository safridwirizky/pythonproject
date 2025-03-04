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

money = 0

def check_resources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water.")
        exit()
    elif resources['milk'] < MENU[coffee]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        exit()
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        exit()
    
    print("Please insert coins")    
    quarter = .25 * int(input("Quarter: "))
    dime = .1 * int(input("Dime: "))
    nickel = .05 * int(input("Nickel: "))
    penny = .01 * int(input("Penny: "))
    coins = quarter + dime + nickel + penny
    
    if coins < MENU[coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        
    else:
        print(f"Here is your {coffee}. Enjoy!\n")
        
        global money
        money += coins
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['milk'] -= MENU[coffee]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']

dapur = True
while dapur:
    menu = input("What would you like? (espresso/latte/cappuccino): ")
    if menu == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

    elif menu == 'espresso':
        check_resources('espresso')    

    elif menu == 'latte':
        check_resources('latte')

    elif menu == 'cappuccino':
        check_resources('cappuccino')

    else:
        print("Menu not exist.")