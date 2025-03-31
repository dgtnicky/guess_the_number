>>> def guess_the_number():
...     secret_number = random.randint(1, 100)
...     attempts = 0
...     print("welcome to the guess the number game!")
...     print("i'm thinking of a number between 1 and 100.")
... while True:
...     try:
...         guess = int(input("take a guess:")
...         attempts += 1
...         if guess < secrect_number:
...             print("too low, try again.")
...         elif guess > secret_number:
...             print("too high, try again.")
...         else:
...             print("congratulations, you guess the number in {attempts} attempts.")
...             break
...         except valueError:
...             print("that is not a valid number. please enter an integar.")
... if _name_=="_main_":
...     guess_the_number()
