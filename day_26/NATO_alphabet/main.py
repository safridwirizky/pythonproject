import pandas
from pathlib import Path

df = pandas.read_csv(Path(__file__).with_name("nato_phonetic_alphabet.csv"))
df_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}

user_word = input("Input your word: ").upper()
nato = [df_dict[word] for word in user_word]
print(nato)