import random
randint = random.randint(1,9)
print(randint)
chances = 3

while chances > 0:   
    number = int(input("Enter a number between 1 and 9: "))
    if number != randint:
        print("Try again!")      
        chances -= 1
        print("You have " + str(chances) + " chances left.")

    if number == randint:
        print("Congratulations! You Won!")
        chances = 3


if chances <= 0:
    print("You Lose")

  
if number != randint:
    print("Try again!")      
    chances -= 1
    print("You have " + str(chances) + " chances left.")

    



    






    
