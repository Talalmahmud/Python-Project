
import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_df = {row.letter: row.code for (index, row) in df.iterrows()}

#print(dic_df)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_data = input("Enter a word: ").upper()

output = [dic_df[letters] for letters in user_data]
print(output)