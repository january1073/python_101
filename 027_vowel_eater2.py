# "Eat" the vowels of a given word and display only its consonants
word_without_vowels = ""

user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in "AEIOU":
        continue # Skip vowels
    word_without_vowels += letter # Concatenate consonants

print(word_without_vowels)