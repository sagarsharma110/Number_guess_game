import random

while True:
    choice = input("Do you want to play? (press 'y' Or 'Y') OR If you want to Quit (press 'Q' or 'q'): ").lower()  

    if choice == "y":
        num = random.randint(1,100)
        #print(num)
        while True: 
            try:
                Guess_num = int(input("Guess the number between 1 and 100: "))
                
                if Guess_num > num :
                    print("Too high!")

                elif Guess_num < num :
                    print("Too low!")
    
                else:
                    print("Congrats!...  You Guessed the number")
                    break

            except ValueError:
                print("Please enter a valid number. You entered a character/symbol")  


    elif choice == "q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice.")