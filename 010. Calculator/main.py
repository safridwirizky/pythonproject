import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

kamus_kalkulator = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def perhitungan_kedua(number_1):
    print('+\n-\n*\n/')
    operator = kamus_kalkulator[input('Masukkan operator yang ingin kamu gunakan: ')]
    number_2 = float(input('Angka kedua: '))
    hasil = operator(number_1, number_2)
    print(f'Hasilnya adalah {hasil}\n')

    lanjut = input('Apakah ingin melanjutkan perhitungan dengan hasil sebelumnya: (ya / tidak)\n')
    if lanjut == 'ya':
        perhitungan_kedua(hasil)
    else:
        print('\n' * 50)
        perhitungan_pertama()

def perhitungan_pertama():
    print(art.logo)
    number_1 = float(input('Angka pertama: '))
    perhitungan_kedua(number_1)

perhitungan_pertama()