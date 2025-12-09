#!/usr/bin/python3




def main():

    # beam.txt is real puzzle input
    with open("../puzzle-inputs/beam.txt", "r") as f:
        tree = [list(line.rstrip("\n")) for line in f]

        beam = []
        count = 0

        for row in range(len(tree)):
            for col in range(len(tree[row])):
                if tree[row][col] == 'S':
                    beam.append(col)
                if tree[row][col] == '^' and col in beam:
                    count += 1
                    beam = [x for x in beam if x != col]
                    beam.append(col - 1)
                    beam.append(col + 1)
                    print(beam)

        print(count)




main()
