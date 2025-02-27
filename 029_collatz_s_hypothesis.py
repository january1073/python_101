# Calculate Lothar Collatz's hypothesis

number_c0 = int(input("Enter a non-negative and non-zero integer number: "))
steps = 0

while number_c0 != 1:
    if number_c0 % 2 == 0:
        number_c0 = number_c0 / 2
        print(int(number_c0))
        steps += 1
    else:
        number_c0 = 3 * number_c0 + 1
        print(int(number_c0))
        steps += 1

print("Steps:", steps)
