import random
choice = input("This is a game of rock paper and scissor... Also my first python code... ^ _ ^ \n If you wanna play single player type UNO, for multiplayer type DUO \n")

player1 = input("Enter 1st player choice \n 1.Rock \n 2.Paper \n 3.Scissor\n")
if(choice == "UNO"):
    player2 = str(random.randint(1, 3))
else:
    player2 = input("Enter 1st player choice :")

print("choice of player 1: "+player1)
print("choice of player 2: "+player2)

if(player1 == "1" and player2 == "3"):
    print("Player1 wins")

elif(player1 == "2" and player2 == "1"):
    print("Player1 wins")

elif(player1 == "3" and player2 == "2"):
    print("Player1 wins")

elif(player1 == "1" and player2 == "2"):
    print("Player2 wins")

elif(player1 == "2" and player2 == "3"):
    print("Player2 wins")

elif(player1 == "3" and player2 == "1"):
    print("Player2 wins")

elif(player1 == "3" and player2 == "3"):
    print("Draw")

elif(player1 == "2" and player2 == "2"):
    print("Draw")

elif(player1 == "1" and player2 == "1"):
    print("Draw")
