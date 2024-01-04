import random


def guess_number():
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Guess a number between {lower_bound} and {upper_bound}:")

    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the correct number, which was {target_number}.")
            break


if __name__ == "__main__":
    guess_number()
