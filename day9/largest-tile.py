#!/usr/bin/python3



def main():

    cords = []

    with open("../puzzle-inputs/rectangle-cords.txt") as f:
        lines = [ line.strip() for line in f if line.strip() ]

        for line in lines:
            x, y= line.split(",")
            cords.append((int(x), int(y))) 


    winning_area = 0

    for i in range(len(cords)):
        x1, y1 = cords[i]
        for j in range(i + 1, len(cords)):
            x2, y2 = cords[j]

            # formula of a rectangle with 2 points
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1

            current_area = width * height

            if current_area > winning_area:
                winning_area = current_area

    print(winning_area)


main()
