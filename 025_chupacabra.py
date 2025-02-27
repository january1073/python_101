# Exit the loop with the secret word

word = str(input("Enter the secret word: "))

while True:
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    else:
        word = str(input("You're stuck in a loop. To exit the loop, enter the secret word: "))