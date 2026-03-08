# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
from pathlib import Path

data_path = Path(__file__).parent / "nato_phonetic_alphabet.csv"

data = pandas.read_csv(data_path)

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_game_on = True
while is_game_on:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Maaf harus huruf!")
    else:
        is_game_on = False