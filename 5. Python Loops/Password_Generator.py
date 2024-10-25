import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
]
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
pilihan = [0, 1, 2]

password = ''

i = int(input('berapa angka yang kamu inginkan? '))
j = int(input('berapa huruf yang kamu inginkan? '))
k = int(input('berapa simbol yang kamu inginkan? '))
print()

def acara_random(i, j, k, password):
    while i > 0 or j > 0 or k > 0:
        randomisation = random.choice(pilihan)
        match randomisation:
            case 0:
                if i != 0:
                    random_number = random.choice(numbers)
                    password = password + random_number
                    i -= 1

            case 1:
                if j != 0:
                    random_letters = random.choice(alphabets)
                    password = password + random_letters
                    j -= 1
                
            case 2:
                if k != 0:
                    random_symbols = random.choice(symbols)
                    password = password + random_symbols
                    k -= 1

    return password
    
password = acara_random(i, j, k, password)

print(password, '\n')