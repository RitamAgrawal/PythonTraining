correctNumber = 70
counter = 1
while counter <= 5:
    
    number = int(input("Guess the {} number: ".format(counter)))
    if counter == 5 and number != correctNumber:
        print("Game Over!")
        break
    if number == correctNumber:
        print("Good guess!")
    else:
        print("Try again")
    
    counter += 1