# "Eat" the vowels of a given word and display only its consonants

user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    else:
        print(letter)