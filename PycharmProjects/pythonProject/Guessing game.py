print("This is a guessing game, guess the right number and go home with a package")
def guessing_game():
    secret_number = 8
    guess_count = 0
    guess_limit = 4
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("Congrats, you won an iphone 14 Pro Max, Call your village people and collect it!")
            break
    else:
        print("Sorry, you failed. No be me do am")

print(guessing_game())