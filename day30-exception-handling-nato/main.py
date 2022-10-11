import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}


def generate_phonetic():
    word = input('Enter your word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as err:
        print(f'KeyError: {err}\nSorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
