secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter an integer number: "))

while number != 777:
    number = int(input("Ha ha! You're stuck in my loop! Enter another integer number: "))

print("Well, done, muggle! You are free now.")