import pandas

# Read CSV and create a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (_, row) in data.iterrows()}

# Get user input and convert to uppercase
user_input = input("Enter a word: ").upper()

# Map each letter to the NATO code word
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)
