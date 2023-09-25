# random guessing game in python.
from random import randint

#random number
random_num = randint(1,10)

#displaying instructions
print("Guess the number between 1 and 10! You'll have 3 tries and 2 hints to guess it!")
print("To use a hint, just ask 'is given number  higher/lower than n', n being any given number between 1 and 10!")
print("--------------------------------------------------")

#number of guesses and hints at beginning
num_of_guesses = 1
num_of_hints = 1

#main code
while 1:
    if num_of_guesses >= 4:
        print("Game over!")
        break
    
    else:
        player = input("Guess or hint? : ") #asking whether player wants to guess a number or ask for a hint
        player.strip()
    
        #code if player wants to guess
        if player == "guess" or player == "Guess":
            while num_of_guesses<5: 
                num = int(input("Guess the number: "))
                if num == random_num:
                    print("Congrats! You guessed the number!")               
                    num_of_guesses += 3
                else:          
                    print("Oops! You have", 3 - num_of_guesses," left")
                num_of_guesses += 1
                break


        #code if player wants to ask for a hint
        elif player == "hint" or player == "Hint":
            while num_of_hints < 4:
                if num_of_hints == 3:
                    print("You're out of hints!")
                    num_of_hints += 4
                    break
                else:
                    hint,hint_num = input("Ask a hint: ").split('than')
                    hint.strip()
                    hint_num.strip()
                    hint_num = int(hint_num)
                        
                    if hint == "is given number higher " or hint == "Is given number higher ":
                        if hint_num < random_num:
                            print("Yes, you have", (2-num_of_hints), "hints remaining")
                        else:
                            print("No, you have", (2-num_of_hints), "hints remaining")
                        num_of_hints += 1
                        break
                
                            
                    elif hint == "is given number lower " or hint == "Is given number lower ":
                        if hint_num > random_num:
                            print("Yes, you have", (2-num_of_hints), "hints remaining")
                        else:
                            print("No, you have", (2-num_of_hints), "hints remaining")
                        num_of_hints += 1
                        break
                        
                    else:
                        print("Please ask your hint again")
                        break

