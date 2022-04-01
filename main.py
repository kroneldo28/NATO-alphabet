import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_nato = {row.letter: row.code for (index, row) in data_nato.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Let's catch a KeyError if there is on
incorrect_input = True
while incorrect_input:
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code = [dict_nato[letter] for letter in user_input]
    except KeyError as error:
        print("Sorry, only letters in the alphabet please.")
        print(f"{error} is not in the NATO alphabet.")
    else:
        incorrect_input = False


print(phonetic_code)
