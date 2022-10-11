# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Pathlib version
from asyncore import write
from pathlib import Path

PLACEHOLDER = '[name]'

cwd = Path.cwd()
input_dir = Path.joinpath(cwd, 'Input/')
output_dir = Path.joinpath(cwd, 'Output/ReadyToSend')
letter_path = Path.joinpath(input_dir, 'Letters/starting_letter.txt')
name_path = Path.joinpath(input_dir, 'Names/invited_names.txt')


with open(name_path, 'r') as read_f:
    names = [line.strip() for line in read_f.readlines()]

with open(letter_path, 'r') as read_f:
    letter = read_f.readlines()

for name in names:
    file_path = f'letter_for_{name}.txt'
    with open(Path.joinpath(output_dir, file_path), 'w') as write_f:
        updated_text = [line.replace(PLACEHOLDER, name) for line in letter]
        write_f.writelines(updated_text)
