from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem('espresso', 50, 0, 18, 1.5)
latte = MenuItem('latte', 200, 150, 24, 2.5)
cappuccino = MenuItem('cappuccino', 200, 150, 24, 2.5)

resources = CoffeeMaker()
moneys = MoneyMachine()

flag = True
while flag:
    menu = input('What would you like? (espresso/latte/cappuccino/): ')

    if menu == 'report':
        resources.report()

    elif menu == 'espresso':
        resources_enough = resources.is_resource_sufficient(espresso)
        if resources_enough:
            payments = moneys.make_payment(espresso.cost)
            if payments:
                resources.make_coffee(espresso)

    elif menu == 'latte':
        resources_enough = resources.is_resource_sufficient(latte)
        if resources_enough:
            payments = moneys.make_payment(latte.cost)
            if payments:    
                resources.make_coffee(latte)

    elif menu == 'cappuccino':
        resources_enough = resources.is_resource_sufficient(cappuccino)
        if resources_enough:
            payments = moneys.make_payment(cappuccino.cost)
            if payments:
                resources.make_coffee(cappuccino)

    elif menu == 'off':
        exit()