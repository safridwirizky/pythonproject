import art, random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'y':
    print(art.logo)

    user_cards = []
    dealer_cards = []

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {dealer_cards[0]}")

    first_blackjack = False
    blackjack = False
    if sum(user_cards) == 22:
        user_cards[1] = 1
    elif sum(user_cards) == 21:
        first_blackjack = True
        blackjack = True
        print("Blackjack!\n")
    if sum(dealer_cards) == 22:
        dealer_cards[1] = 1

    while not blackjack:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        print()
        if hit == 'y':
            user_cards.append(random.choice(cards))
            if sum(user_cards) < 21:
                print(f"Your cards: {user_cards}\n")
            elif sum(user_cards) == 21:
                blackjack = True
            else:
                print(f"Your cards {user_cards}= {sum(user_cards)}")
                print(f"Computer's cards {dealer_cards}= {sum(dealer_cards)}\n")
                print(f"BUST\nYou Lose!")
                exit()
        else:
            break

    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))

    if sum(dealer_cards) > 21:
        print(f"Your cards {user_cards}= {sum(user_cards)}")
        print(f"Computer's cards {dealer_cards}= {sum(dealer_cards)}\n")
        if first_blackjack:
            print("You Win!")
        else:
            print("Computer BUST\nYou Win!")
        exit()

    print(f"Your cards {user_cards}= {sum(user_cards)}")
    print(f"Computer's cards {dealer_cards}= {sum(dealer_cards)}\n")
    if sum(user_cards) > sum(dealer_cards):
        print("You Won!")
    elif sum(user_cards) == sum(dealer_cards):
        print("PUSH")
    else:
        print("You Lose!")

else:
    exit()