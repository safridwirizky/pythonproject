import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

daftar_pilihan = {
    '0': rock,
    '1': paper,
    '2': scissors,
    }

def main_lagi():
    m_l = input('Mau main lagi? "y" yes, "n" no\n')
    if m_l == 'y':
        main_game()
    elif m_l == 'n':
        exit()
    else:
        main_lagi()

def main_game():
    choose = input('\napa yang kamu pilih? Rock = "0", Paper = "1", Scissors = "2"\n')
    match choose:
        case '0':
            print('You')
            print(rock, '\n\n')
        
            print('Computer')
            pilihan_computer = random.choice(list(daftar_pilihan.keys()))
            print(daftar_pilihan[pilihan_computer], '\n')
            match pilihan_computer:
                case '0':
                    print('Draw\n')
                case '1':
                    print('You lose\n')
                case '2':
                    print('You win\n')
            
            main_lagi()

        case '1':
            print('You')
            print(paper, '\n\n')
        
            print('Computer')
            pilihan_computer = random.choice(list(daftar_pilihan.keys()))
            print(daftar_pilihan[pilihan_computer], '\n')
            match pilihan_computer:
                case '0':
                    print('You win\n')
                case '1':
                    print('Draw\n')
                case '2':
                    print('You lose\n')
            
            main_lagi()

        case '2':
            print('You')
            print(scissors, '\n\n')
        
            print('Computer')
            pilihan_computer = random.choice(list(daftar_pilihan.keys()))
            print(daftar_pilihan[pilihan_computer], '\n')
            match pilihan_computer:
                case '0':
                    print('You lose\n')
                case '1':
                    print('You win\n')
                case '2':
                    print('Draw\n')
            
            main_lagi()

        case _:
            main_game()

main_game()