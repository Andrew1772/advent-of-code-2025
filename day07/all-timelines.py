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
                    beam.append((row, col))
                if tree[row][col] == '^' and (row, col) in beam:
                    count += 1
                    beam = [x for x in beam if x != (row, col)]
                    beam.append((row, col - 1))
                    beam.append((row, col + 1))
                    print(beam)

        print(count)




main()
