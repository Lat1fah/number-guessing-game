import random 


number_to_guess = random.randint(100, 1000)
while True:
    try:
        guess = int(input ("Guess the number between 100 and 1000: "))
    except ValueError:
        print ("Please enter a valid number")
        continue 

    if guess < number_to_guess:
        print ("Too low!")
    elif guess > number_to_guess:
        print ("Too high!")
    else:
        print ("congratulations! You guessed the number.")
        break
   

