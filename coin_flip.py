import random


list_lenght = 100
number_of_tries = 1
for j in range(number_of_tries):
    number_of_streaks = 0
    tosses = []

    for i in range(list_lenght):
        x = random.randint(0,1)
        if x == 0:
            tosses.append("H")
        else:
            tosses.append("T")

    T_streak = 0

    for i in tosses:
        if i == "T":
            T_streak += 1
            if T_streak == 6:
                number_of_streaks +=1
        else:
            T_streak = 0

    H_streak =0
    for i in tosses:
        if i == "H":
            H_streak +=1
            if H_streak == 6:
                number_of_streaks += 1
        else:
            H_streak = 0

print('Chance of streak: %s%%' % (number_of_streaks / 100*number_of_tries))


