# Write your code here :-)
import time, copy, random
width = 60
height = 20
new_field=[]

for i in range(width):
    column = []
    for j in range(height):
        if random.randint(0,1) == 0:
            column.append(" ")
        else:
            column.append("#")
    new_field.append(column)

while True:
    field = copy.deepcopy(new_field)

    for i in range(width):
        for j in range(height):
            print(new_field[i][j], end="")
        print()

    for i in range(width):
        for j in range(height):
            neighbours_alive = 0
            above = i -1
            below = i + 1
            right = j + 1
            left = j - 1

            if i < width-1 and j > 0:
                if field[i+1][j-1] == "#":
                    neighbours_alive += 1

            if i > 0 and j > 0:
                if field[i-1][j-1] == "#":
                    neighbours_alive += 1

            if i < width-1 and j < height - 1:
                if field[i+1][j+1] == "#":
                    neighbours_alive += 1

            if i > 0 and j < height - 1:
                if field[i-1][j+1] == "#":
                    neighbours_alive += 1

            if i < width-1:
                if field[i+1][j] == "#":
                    neighbours_alive += 1

            if i > 0:
                if field[i-1][j] == "#":
                    neighbours_alive += 1

            if j < height-1:
                if field[i][j+1] == "#":
                    neighbours_alive += 1

            if j > 0:
                if field[i][j-1] == "#":
                    neighbours_alive += 1


            if field[i][j] == "#":
                if neighbours_alive == 2 or neighbours_alive == 3:
                    new_field[i][j] = "#"
                else:
                    new_field[i][j] = " "
            if field[i][j] == " ":
                if neighbours_alive == 3:
                    new_field[i][j] = "#"
                else:
                    new_field[i][j] = " "

    time.sleep(1)

