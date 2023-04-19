import random

random_number = random.randint(1, 100)
guess_count = 0

while True:
    guessed_number = int(input("Please enter a number: "))
    guess_count += 1

    if guessed_number == random_number:
        print(f"You guessed the number {guessed_number} in {guess_count} turns!")
        break

    if guessed_number > random_number:
        print("Wrong! Please enter a lower number: ")

    else:
        print("Wrong! Please enter a higher number: ")

