print("This is a guessing game, welcome and have some fun")
secret_number = 11
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = int(input("Guess: ")) 
    guess_count += 1

    if guess ==  secret_number:
        print("Congrats buddy, you won!")
        break
else:
    print("Sorry, you failed")
