secret_word = "Assembly"
guess = ""
limit = 3
while secret_word != guess and limit != 0:
    guess = input("Enter your guess: ")
    limit -= 1
if limit == 0 and secret_word != guess:
    print("Out of guesses... You loose :(😭):")
else:
    print("Bravo!! You won")
