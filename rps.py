# Write your code here :-)
import random, sys
print("Rock, paper, scissors")
wins = 0
losses = 0
ties = 0
while True:
    print("Choose your move (r)rock, (p)aper, (s)cissors or (q)uit.")
    playerhand = input()
    if playerhand == "r":
        print("You chose rock")
    elif playerhand == "p":
        print("You chose paper")
    elif playerhand == "s":
        print("You chose scissors")
    elif playerhand == "q":
        sys.exit()
    else:
        print("Invalid input, please choose your hand (r, p, s)")
        continue
    hand = ("r","p","s")
    computerhand = random.choice(hand)
    if computerhand == "r":
        print("I choose rock")
        if playerhand == "r":
            print("Its a tie.")
            ties += 1
        elif playerhand == "s":
            print("I won.")
            losses += 1
        else:
            print("You won.")
            wins += 1
    elif computerhand == "p":
        print("I choose paper")
        if playerhand == "r":
            print("I won.")
            losses += 1
        elif playerhand == "s":
            print("You won.")
            wins += 1
        else:
            print("Its a tie.")
            ties += 1
    elif computerhand == "s":
        print("I choose scissors")
        if playerhand == "r":
            print("You won.")
            wins += 1
        elif playerhand == "s":
            print("Its a tie.")
            ties += 1
        else:
            print("I won.")
            losses += 1

    print("Up until now you won " + str(wins) + " times, lost " + str(losses) + " and we had " + str(ties) + " ties." )
