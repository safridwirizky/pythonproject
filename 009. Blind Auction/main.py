# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
bids = {}

def compare_the_bids():
    global bids
    highest_bid = 0
    winner = ''

    for bid in bids:
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]

    for bid in bids:
        if bids[bid] == highest_bid:
            winner = bid
            break

    print(f'The winner is {winner} with bid ${bids[winner]}.')

def blind_auction():
    names = input('Type your name: ').lower()
    prices = int(input('Type your bid: $'))

    global bids

    bids[names] = prices

    should_continue = input('Anyone other bidders? (yes or no)').lower()
    match should_continue:
        case 'yes':
            print('\n' * 20)
            blind_auction()
        case 'no':
            print('\n' * 20)
            compare_the_bids()
        case _:
            print('\n' * 20)
            compare_the_bids()

blind_auction()