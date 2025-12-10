#!/usr/bin/python3

def main():

    with open("rotations.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    count = 0
    dial = 50

    for rotation in rotations:

            direction = rotation[0]
            clicks = int(rotation[1:])

            for click in range(clicks):
                # apply one click
                if direction == 'R':
                    dial += 1
                else:
                    dial -= 1

                # wrap around
                if dial > 99:
                    dial -= 100
                elif dial < 0:
                    dial += 100

                # count every time we land on zero
                if dial == 0:
                    count += 1

    print("Here is your secret code:", count)

main()


# Found this creature on advent of code subreddit
# Doesn't work with my input file, this doesn't account for \n

#def crazyAnswer():
#    s, c = 50, 0
#    for x in open("rotations.txt"):
#        print(x)
#        d = x[0] < 'R'
#        v = int(x[1:]) * (1 - 2*d) #mag * sign
#        c += abs((s - d)//100 - (s + v - d)//100)
#        s += v
#    print(c)
#
#crazyAnswer()


