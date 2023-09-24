#rock paper scissors game/roshambo

#initializing arrays and libraries
from random import choice
rps = ['scissors','rock','paper']

while 1:
    player = input("Rock, paper, or scissors? : ") #player's choice
    bot = choice(rps)
    if bot == 'scissors':
        if player == 'rock' or player == 'Rock':
            print("Player chose", player, "and bot chose", bot, ",player wins!")
        elif player == 'paper' or player == 'Paper':
            print("Player chose", player, "and bot chose", bot, ",player loses.")
        else:
            print("Player chose", player, "and bot chose", bot, ",it's a draw!")

    elif bot == 'rock':
         if player == 'rock' or player == 'Rock':
            print("Player chose", player, "and bot chose", bot, ",it's a draw!")
         elif player == 'paper' or player == 'Paper':
            print("Player chose", player, "and bot chose", bot, ",player wins!")
         else:
            print("Player chose", player, "and bot chose", bot, ",player loses.")

    elif bot == 'paper':
         if player == 'rock' or player == 'Rock':
            print("Player chose", player, "and bot chose", bot, ",player loses.")
         elif player == 'paper' or player == 'Paper':
            print("Player chose", player, "and bot chose", bot, ",it's a draw!")
         else:
            print("Player chose", player, "and bot chose", bot, ",player wins!")

    #checking if player would like to play again
    replay = input("\nWould you like to play again?(Y/N) ").strip()
    if replay == 'Y' or replay == 'y':
        pass
    else:
        break
        
